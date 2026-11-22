from tempfile import TemporaryDirectory

from rag.document_loader import load_knowledge_documents
from rag.text_splitter import split_knowledge_documents
from rag.vector_store import create_vector_store


def test_vector_store():

    # 1. Load knowledge documents
    documents = load_knowledge_documents()

    # 2. Split documents into chunks
    chunks = split_knowledge_documents(documents)

    # 3. Use a temporary vector store for testing
    with TemporaryDirectory() as temp_dir:

        # First ingestion
        vector_store = create_vector_store(
            chunks,
            persist_directory=temp_dir
        )

        first_count = vector_store._collection.count()

        print("First ingestion:", first_count)

        assert first_count == len(chunks)

        # Second ingestion of identical chunks
        vector_store = create_vector_store(
            chunks,
            persist_directory=temp_dir
        )

        second_count = vector_store._collection.count()

        print("Second ingestion:", second_count)

        assert second_count == first_count

        print("Idempotent ingestion test passed!")

        # Close the Chroma database system before temporary cleanup.
        vector_store._client._system.stop()


if __name__ == "__main__":
    test_vector_store()