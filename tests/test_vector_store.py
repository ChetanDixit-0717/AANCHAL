
from rag.document_loader import load_knowledge_documents
from rag.text_splitter import split_knowledge_documents
from rag.vector_store import create_vector_store


def test_vector_store():

    # 1. Load knowledge documents
    documents = load_knowledge_documents()

    # 2. Split documents into chunks
    chunks = split_knowledge_documents(documents)

    # 3. Create vector store
    vector_store = create_vector_store(chunks)

    # 4. Check stored document count
    collection_count = vector_store._collection.count()

    print("Vector store created successfully!")
    print("Chunks processed:", len(chunks))
    print("Vectors stored:", collection_count)

    assert collection_count == len(chunks)


if __name__ == "__main__":
    test_vector_store()