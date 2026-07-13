import os
import tempfile
import hashlib
import logging
import sys
from typing import List

from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

from utils.model_loaders import ModelLoader
from utils.config_loader import load_config
from exception.exceptions import TradingBotException


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataIngestion:

    def __init__(self):
        self.model_loader = ModelLoader()
        self.config = load_config()
        self._load_env()

        self.pc = Pinecone(api_key=self.pinecone_api_key)

        self.index_name = self.config["vector_db"]["index_name"]

        self.embedding_model = self.model_loader.load_embeddings()

    def _load_env(self):

        load_dotenv()

        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")

        if not self.google_api_key:
            raise Exception("GOOGLE_API_KEY missing")

        if not self.pinecone_api_key:
            raise Exception("PINECONE_API_KEY missing")

    def _create_index(self):

        if self.index_name not in self.pc.list_indexes().names():

            logger.info(f"Creating index : {self.index_name}")

            self.pc.create_index(
                name=self.index_name,
                dimension=3072,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                ),
            )

    def load_documents(self, uploaded_files) -> List[Document]:

        docs = []

        for file in uploaded_files:

            suffix = os.path.splitext(file.filename)[1].lower()

            temp_path = None

            try:

                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:

                    tmp.write(file.file.read())
                    temp_path = tmp.name

                if suffix == ".pdf":
                    loader = PyPDFLoader(temp_path)

                elif suffix == ".docx":
                    loader = Docx2txtLoader(temp_path)

                else:
                    logger.warning(f"Unsupported file : {file.filename}")
                    continue

                loaded_docs = loader.load()

                for i, doc in enumerate(loaded_docs):

                    doc.metadata["source"] = file.filename
                    doc.metadata["page"] = i

                docs.extend(loaded_docs)

            finally:

                if temp_path and os.path.exists(temp_path):
                    os.remove(temp_path)

        logger.info(f"Loaded {len(docs)} pages")

        return docs

    def split_documents(self, docs):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            length_function=len,
        )

        chunks = splitter.split_documents(docs)

        logger.info(f"Chunks created : {len(chunks)}")

        return chunks

    def store_in_vector_db(self, chunks):

        self._create_index()

        index = self.pc.Index(self.index_name)

        vector_store = PineconeVectorStore(
            index=index,
            embedding=self.embedding_model,
        )

        ids = []

        for chunk in chunks:

            source = chunk.metadata.get("source", "unknown")

            page = chunk.metadata.get("page", 0)

            content_hash = hashlib.sha256(
                chunk.page_content.encode()
            ).hexdigest()

            ids.append(f"{source}_{page}_{content_hash}")

        batch_size = 100

        for i in range(0, len(chunks), batch_size):

            vector_store.add_documents(
                documents=chunks[i:i + batch_size],
                ids=ids[i:i + batch_size],
            )

        stats = index.describe_index_stats()

        logger.info(stats)

    def run_pipeline(self, uploaded_files):

        docs = self.load_documents(uploaded_files)

        if not docs:
            logger.warning("No documents loaded")
            return

        chunks = self.split_documents(docs)

        self.store_in_vector_db(chunks)

        logger.info("Ingestion completed successfully.")