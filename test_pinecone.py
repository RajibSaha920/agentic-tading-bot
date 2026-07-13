from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import time

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

pc.create_index(
    name="trading-bot",
    dimension=3072,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1",
    ),
)

while not pc.describe_index("trading-bot").status["ready"]:
    print("Waiting...")
    time.sleep(2)

print(pc.describe_index("trading-bot"))


# from pinecone import Pinecone
# import os
# from dotenv import load_dotenv

# load_dotenv()

# pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# pc.delete_index("trading-bot")
# print("Deleted")