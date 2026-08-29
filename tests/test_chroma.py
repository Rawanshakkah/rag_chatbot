import chromadb

client = chromadb.Client()

collection = client.create_collection(name="test_collection")

collection.add(
    ids=["1", "2"],
    documents=[
        "Almamlaka TV Digital Expansion Initiative",
        "The project includes a mobile application and web streaming portal."
    ]
)

results = collection.query(
    query_texts=["What platforms are included in the project?"],
    n_results=2
)

print("ChromaDB test successful!")
print("Results:")
print(results["documents"])