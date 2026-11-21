
# Fix SSL certificate verification using Windows certificate store
import truststore
truststore.inject_into_ssl()

from langchain_huggingface import HuggingFaceEmbeddings


def create_embedding_model():

    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    return model


def generate_embeddings(chunks):

    model = create_embedding_model()

    texts = [
        chunk["content"] for chunk in chunks
    ]

    embeddings = model.embed_documents(texts)

    return embeddings
