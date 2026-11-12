
from rag.document_loader import load_knowledge_documents
from rag.text_splitter import split_knowledge_documents


def main():

    documents = load_knowledge_documents()

    print("Original documents:", len(documents))

    chunks = split_knowledge_documents(documents)

    print("Total chunks generated:", len(chunks))

    for index, chunk in enumerate(chunks, start=1):

        print(f"\n{'=' * 60}")
        print(f"CHUNK {index}")
        print(f"{'=' * 60}")

        print("Source:", chunk.metadata["source_file"])
        print("Start index:", chunk.metadata.get("start_index"))
        print("Length:", len(chunk.page_content))

        print("\nFULL CONTENT:")
        print(chunk.page_content)


if __name__ == "__main__":
    main()