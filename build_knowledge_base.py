
import sys
from pathlib import Path

# Make the src folder available for imports
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root / "src"))

from document_loader import load_all_documents
from text_splitter import split_documents
from vector_store import create_vector_store


def build_knowledge_base():

    data_folder = project_root / "data"
    database_path = project_root / "vector_database"

    print("\nCYBERSECURITY RAG KNOWLEDGE BASE")
    print("=" * 45)

    # Step 1: Load documents
    print("\nStep 1: Loading documents...")

    documents = load_all_documents(data_folder)

    if not documents:
        raise ValueError("No documents found!")

    # Step 2: Split documents
    print("\nStep 2: Processing documents...")

    chunks = split_documents(documents)

    print("Total chunks:", len(chunks))

    # Step 3: Create FAISS vector database
    print("\nStep 3: Creating FAISS vector database...")

    vector_store = create_vector_store(chunks)

    # Step 4: Save database
    print("\nStep 4: Saving vector database...")

    vector_store.save_local(str(database_path))

    print("\nKnowledge base created successfully!")
    print("Total documents:", len(documents))
    print("Total chunks:", len(chunks))
    print("Database location:", database_path)


if __name__ == "__main__":
    build_knowledge_base()

