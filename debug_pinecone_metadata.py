from pinecone import Pinecone, ServerlessSpec

# Pinecone API Key and Index Name
PINECONE_API_KEY = "pcsk_5A2bac_em52xH4JqjtvTutTvXtiBEQGBNTAcVXLo3GA1tZhhGoFddYChBJ5vE4atwbJMS"
PINECONE_INDEX_NAME = "gemini-embeddings"

def fetch_pinecone_metadata():
    try:
        # Initialize Pinecone client
        pc = Pinecone(api_key=PINECONE_API_KEY)

        # Get the Pinecone index
        pinecone_index = pc.Index(PINECONE_INDEX_NAME)

        # Fetch metadata from Pinecone
        results = pinecone_index.describe_index_stats()
        print("Pinecone Metadata Details:")
        print(results)
    except Exception as e:
        print(f"Error fetching Pinecone metadata: {e}")

if __name__ == "__main__":
    fetch_pinecone_metadata()
