from src.retriever import retrieve_documents


query = "What platforms are included in the Digital Expansion Initiative?"

results = retrieve_documents(query, top_k=3)

print("Query:")
print(query)

print("\n" + "=" * 60)
print("Retrieved Documents:")
print("=" * 60)

for i, document in enumerate(results["documents"][0], start=1):
    print(f"\nResult {i}")
    print("-" * 60)
    print("Text:")
    print(document)

    print("Metadata:")
    print(results["metadatas"][0][i - 1])