from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def create_embedding_model():
    model = SentenceTransformer(MODEL_NAME)

    return model