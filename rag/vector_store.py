import hashlib
from pathlib import Path

from langchain_chroma import Chroma

from rag.embedding_model import load_embedding_model

VECTOR_STORE_DIR = "data/vector_store"
COLLECTION_NAME = "aanchal_knowledge_base"


def generate_chunk_ids(chunks):
    """
    Generate stable IDs for document chunks.
    """

    chunk_ids = []

    for chunk in chunks:
        source_file = chunk.metadata.get("source_file", "unknown")
        start_index = chunk.metadata.get("start_index", 0)

        unique_content = (
            f"{source_file}:{start_index}:{chunk.page_content}"
        )

        chunk_id = hashlib.sha256(
            unique_content.encode("utf-8")
        ).hexdigest()

        chunk_ids.append(chunk_id)

    return chunk_ids


def create_vector_store(
    chunks,
    persist_directory=VECTOR_STORE_DIR
):
    """
    Create or update a persistent Chroma vector store.
    Uses stable IDs to avoid duplicate insertion.
    """

    if not chunks:
        raise ValueError("No document chunks provided.")

    embedding_model = load_embedding_model()

    chunk_ids = generate_chunk_ids(chunks)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        ids=chunk_ids,
        collection_name=COLLECTION_NAME,
        persist_directory=str(Path(persist_directory))
    )

    return vector_store


def load_vector_store(
    persist_directory=VECTOR_STORE_DIR
):
    """
    Load an existing persistent Chroma vector store.
    """

    if not Path(persist_directory).exists():
        raise FileNotFoundError(
            "Vector store not found. Create it first."
        )

    embedding_model = load_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=str(Path(persist_directory))
    )

    return vector_store