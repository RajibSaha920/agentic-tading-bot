from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    raise ValueError("PINECONE_API_KEY not found in .env file")

# Initialize Pinecone
pc = Pinecone(api_key=api_key)

# List all indexes
print("Available Indexes:", pc.list_indexes().names())

# Optional: Show details if the index exists
index_name = "trading-bot"

if index_name in pc.list_indexes().names():
    print(f"\n'{index_name}' exists.")
    print(pc.describe_index(index_name))
else:
    print(f"\n'{index_name}' does not exist.")


    from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

pc.delete_index("trading-bot")
print("Deleted")