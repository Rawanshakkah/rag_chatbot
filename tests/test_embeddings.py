from src.embeddings import create_embedding_model


model = create_embedding_model()

text = "What is the project budget?"

embedding = model.encode(text)

print("Embedding created successfully!")
print("Vector dimensions:", len(embedding))