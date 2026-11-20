from pathlib import Path
from langchain_chroma import Chroma

from rag.embedding_model import load_embedding_model

VECTOR_STORE_DIR = "data/vectore_store"
COLLECTION_NAME = "aanchal_knowledge_base"

def create_vector_store(
    chunks,
    persist_directory=VECTOR_STORE_DIR
):

    if not chunks:
        raise ValueError("No document chunks provided.")

    embedding_model = load_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name=COLLECTION_NAME,
        persist_directory=str(Path(persist_directory))
    )

    return vector_store