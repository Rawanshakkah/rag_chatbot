from pathlib import Path

from src.pdf_loader import load_pdf
from src.text_splitter import split_pages


DATA_DIR = Path("data")


def process_documents():
    all_chunks = []

    pdf_files = sorted(DATA_DIR.glob("*.pdf"))

    for pdf_path in pdf_files:
        pages = load_pdf(str(pdf_path))
        chunks = split_pages(pages)
        all_chunks.extend(chunks)

    return all_chunks