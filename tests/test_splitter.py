from src.pdf_loader import load_pdf
from src.text_splitter import split_pages


pdf_path = "data/Almamlaka_Budget_Timeline.pdf"

pages = load_pdf(pdf_path)

chunks = split_pages(pages)

print(f"Number of pages: {len(pages)}")
print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print("\n" + "=" * 60)
    print(f"Chunk {i}")
    print("=" * 60)

    print("Source:", chunk["source"])
    print("Page:", chunk["page"])
    print("Text:")
    print(chunk["text"])