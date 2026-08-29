from src.retriever import retrieve_documents
from src.generator import generate_answer


query = "What platforms are included in the Digital Expansion Initiative?"


# Retrieve relevant documents
results = retrieve_documents(query, top_k=3)


# Extract retrieved text
documents = results["documents"][0]


# Combine the retrieved chunks into one context
context = "\n\n".join(documents)


# Generate answer using Gemini
answer = generate_answer(query, context)


print("Query:")
print(query)

print("\n" + "=" * 60)
print("Generated Answer:")
print("=" * 60)

print(answer)