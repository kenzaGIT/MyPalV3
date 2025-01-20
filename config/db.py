from pinecone import Pinecone, ServerlessSpec
from pymongo import MongoClient
import logging

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "mypal_database"

def init_mongo():
    """Initialize MongoDB connection and return the database instance."""
    try:
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        logging.info(f"Connected to MongoDB: {DATABASE_NAME}")
        return db
    except Exception as e:
        logging.error(f"Error connecting to MongoDB: {e}")
        raise

# Pinecone API configuration
PINECONE_API_KEY = "pcsk_5A2bac_em52xH4JqjtvTutTvXtiBEQGBNTAcVXLo3GA1tZhhGoFddYChBJ5vE4atwbJMS"  # Replace with your actual Pinecone API key
PINECONE_INDEX_NAME = "course-content"

def init_pinecone():
    """Initialize and return Pinecone index."""
    try:
        pc = Pinecone(api_key=PINECONE_API_KEY)

        # Check if the index exists, if not, create it
        existing_indexes = [index["name"] for index in pc.list_indexes()]
        if PINECONE_INDEX_NAME not in existing_indexes:
            pc.create_index(
                name=PINECONE_INDEX_NAME,
                dimension=384,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
            logging.info(f"Created Pinecone index: {PINECONE_INDEX_NAME}")
        else:
            logging.info(f"Pinecone index '{PINECONE_INDEX_NAME}' already exists.")

        return pc.Index(PINECONE_INDEX_NAME)
    except Exception as e:
        logging.error(f"Error initializing Pinecone: {e}")
        raise
