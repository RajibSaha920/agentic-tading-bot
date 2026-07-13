from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import time

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "trading-bot"

print("Existing:", pc.list_indexes().names())
print(pc.describe_index("trading-bot"))

pc.create_index(
    name="trading-bot",
    dimension=3072,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ),
)

while not pc.describe_index(index_name).status["ready"]:
    print("Waiting...")
    time.sleep(2)

print("Done")
print(pc.list_indexes().names())