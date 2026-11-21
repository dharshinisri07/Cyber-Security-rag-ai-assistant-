
import json
from pathlib import Path
from pypdf import PdfReader


def load_pdf_documents(data_folder):
    documents = []

    data_path = Path(data_folder)

    for pdf_file in data_path.rglob("*.pdf"):
        try:
            reader = PdfReader(str(pdf_file))

            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text()

                if text and text.strip():
                    documents.append({
                        "content": text,
                        "source": str(pdf_file),
                        "page": page_number,
                        "type": "pdf"
                    })

            print(f"Loaded PDF: {pdf_file.name}")

        except Exception as error:
            print(f"Error reading {pdf_file.name}: {error}")

    return documents


def load_qa_documents(json_file):
    documents = []

    json_path = Path(json_file)

    with open(json_path, "r", encoding="utf-8") as file:
        qa_records = json.load(file)

    for record in qa_records:
        question = record.get("question", "").strip()
        answer = record.get("answer", "").strip()

        if not question or not answer:
            continue

        documents.append({
            "content": f"Question: {question}\nAnswer: {answer}",
            "source": json_path.name,
            "type": "qa",
            "question_id": record.get("id"),
            "category": record.get("category", "Uncategorized"),
            "question": question
        })

    print(f"Loaded Q&A records: {len(documents)}")

    return documents


def load_all_documents(data_folder):
    data_path = Path(data_folder)

    pdf_documents = load_pdf_documents(data_path)

    qa_file = data_path / "QA" / "cybersecurity_qa.json"
    qa_documents = load_qa_documents(qa_file)

    all_documents = pdf_documents + qa_documents

    print("\nKnowledge Base Loading Summary")
    print("--------------------------------")
    print("PDF documents:", len(pdf_documents))
    print("Q&A documents:", len(qa_documents))
    print("Total documents:", len(all_documents))

    return all_documents


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    data_folder = project_root / "data"

    documents = load_all_documents(data_folder)
