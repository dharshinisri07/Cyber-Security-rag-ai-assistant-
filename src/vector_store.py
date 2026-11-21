
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from embeddings import create_embedding_model


def create_vector_store(chunks):

    model = create_embedding_model()

    documents = []

    for chunk in chunks:

        metadata = {
            key: value
            for key, value in chunk.items()
            if key != "content" and value is not None
        }

        documents.append(
            Document(
                page_content=chunk["content"],
                metadata=metadata
            )
        )

    vector_store = FAISS.from_documents(
        documents,
        model
    )

    return vector_store


if __name__ == "__main__":

    sample_chunks = [
        {
            "content": "SQL Injection is a web application vulnerability.",
            "source": "OWASP",
            "type": "pdf",
            "page": 1
        },
        {
            "content": "Phishing attacks trick users into revealing sensitive information.",
            "source": "CISA",
            "type": "pdf",
            "page": 2
        }
    ]

    print("Creating FAISS vector database...")

    vector_store = create_vector_store(sample_chunks)

    project_root = Path(__file__).resolve().parent.parent
    database_path = project_root / "vector_database"

    vector_store.save_local(str(database_path))

    print("FAISS database created successfully!")
    print("Database location:", database_path)
