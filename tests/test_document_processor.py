from src.document_processor import process_documents


chunks = process_documents()

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print("\n" + "=" * 60)
    print(f"Chunk {i}")
    print("=" * 60)
    print("Source:", chunk["source"])
    print("Page:", chunk["page"])
    print("Text:")
    print(chunk["text"][:200])