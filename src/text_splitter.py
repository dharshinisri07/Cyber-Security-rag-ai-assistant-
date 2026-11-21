
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents, chunk_size=1000, chunk_overlap=200):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = []

    for document in documents:

        text = document["content"]

        # Keep each Q&A pair together as one chunk
        if document.get("type") == "qa":
            chunks.append(document.copy())
            continue

        # Split PDF documents into smaller chunks
        split_texts = splitter.split_text(text)

        for chunk in split_texts:

            chunk_data = document.copy()
            chunk_data["content"] = chunk

            chunks.append(chunk_data)

    return chunks


if __name__ == "__main__":

    sample_documents = [
        {
            "content": "Question: What is SQL Injection?\nAnswer: SQL Injection is a web application vulnerability.",
            "source": "cybersecurity_qa.json",
            "type": "qa",
            "question_id": 1,
            "category": "Web Security"
        }
    ]

    result = split_documents(sample_documents)

    print("Text splitting completed!")
    print("Total chunks generated:", len(result))

    for index, chunk in enumerate(result[:3], start=1):
        print(f"\nChunk {index}:")
        print("Source:", chunk["source"])
        print("Content:", chunk["content"])
