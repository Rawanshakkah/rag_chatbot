import chromadb
from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "almamlaka_documents"


# Load the embedding model once
embedding_model = SentenceTransformer(MODEL_NAME)

# Create ChromaDB client once
client = chromadb.PersistentClient(path=CHROMA_PATH)

# Get the collection once
collection = client.get_collection(
    name=COLLECTION_NAME
)


def retrieve_documents(query, top_k=3):
    """
    Search the vector database and return
    the most relevant document chunks.
    """

    query_embedding = embedding_model.encode(
        [query]
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results