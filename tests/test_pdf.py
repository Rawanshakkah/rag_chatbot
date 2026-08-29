from src.pdf_loader import load_pdf


pdf_files = [
    "data/Almamlaka_Budget_Timeline.pdf",
    "data/Almamlaka_Project_Overview.pdf",
    "data/Almamlaka_Team_Governance.pdf"
]


for pdf_path in pdf_files:
    print("\n" + "#" * 60)
    print(f"FILE: {pdf_path}")
    print("#" * 60)

    pages = load_pdf(pdf_path)

    print(f"Number of pages: {len(pages)}")

    for page in pages:
        print("\n" + "=" * 50)
        print(f"Page: {page['page']}")
        print(page["text"][:300])