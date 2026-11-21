
from pathlib import Path
from functools import lru_cache

from langchain_community.vectorstores import FAISS
from embeddings import create_embedding_model


@lru_cache(maxsize=1)
def load_vector_database():

    print("Loading embedding model and FAISS database...")

    project_root = Path(__file__).resolve().parent.parent
    database_path = project_root / "vector_database"

    model = create_embedding_model()

    vector_store = FAISS.load_local(
        str(database_path),
        model,
        allow_dangerous_deserialization=True
    )

    print("Knowledge base loaded successfully!")

    return vector_store


def retrieve_information(question, k=3):

    vector_store = load_vector_database()

    results = vector_store.similarity_search(
        question,
        k=k
    )

    return results


if __name__ == "__main__":

    question = "How can I prevent SQL Injection attacks?"

    print("Searching cybersecurity knowledge base...")

    results = retrieve_information(question)

    for index, result in enumerate(results, start=1):

        print(f"\nResult {index}")
        print("Source:", result.metadata.get("source"))
        print("Content:", result.page_content)

    print("\nRetrieval completed successfully!")
