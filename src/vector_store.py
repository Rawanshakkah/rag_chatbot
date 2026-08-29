import chromadb
from sentence_transformers import SentenceTransformer


# Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_store(chunks):
    """
    Create a ChromaDB collection and store document chunks with embeddings.
    """

    client = chromadb.PersistentClient(path="chroma_db")

    collection = client.get_or_create_collection(
        name="almamlaka_documents"
    )

    documents = []
    metadatas = []
    ids = []

    for index, chunk in enumerate(chunks):
        documents.append(chunk["text"])

        metadatas.append({
            "source": chunk["source"],
            "page": chunk["page"]
        })

        ids.append(f"chunk_{index}")

    embeddings = embedding_model.encode(documents).tolist()

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    return collection