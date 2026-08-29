from src.pdf_loader import load_pdf
from src.text_splitter import split_pages
from src.vector_store import create_vector_store


# Load the three PDF files
pdf_files = [
    "data/Almamlaka_Budget_Timeline.pdf",
    "data/Almamlaka_Project_Overview.pdf",
    "data/Almamlaka_Team_Governance.pdf"
]

documents = []

for pdf_file in pdf_files:
    documents.extend(load_pdf(pdf_file))


# Create chunks
chunks = split_pages(documents)

print("Total chunks:", len(chunks))


# Create vector store
collection = create_vector_store(chunks)

print("Vector store created successfully!")
print("Number of chunks stored:", collection.count())