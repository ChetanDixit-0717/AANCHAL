
from rag.document_loader import load_knowledge_documents


def main():

    documents = load_knowledge_documents()

    print(f"\nTotal documents loaded: {len(documents)}")

    for index, document in enumerate(documents, start=1):

        print(f"\n--- Document {index} ---")

        print("Source:", document.metadata["source_file"])
        print("Category:", document.metadata["category"])
        print("Source ID:", document.metadata["source_id"])
        print("Content length:", len(document.page_content))

        print("\nContent preview:")
        print(document.page_content[:300])


if __name__ == "__main__":
    main()