from pypdf import PdfReader


def load_pdf(file_path):
    reader = PdfReader(file_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        pages.append({
            "text": text or "",
            "source": file_path,
            "page": page_number
        })

    return pages