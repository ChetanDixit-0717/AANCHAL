from rag.retriever import retrieve_relevant_documents


def test_retriever():

    question = (
        "What medicine should I give my child to treat severe malnutrition?"
    )

    results = retrieve_relevant_documents(
        query=question,
        k=3
    )

    print("\nUser Question:", question)
    print("\nRetrieved Documents:")

    for index, document in enumerate(results, start=1):

        print(f"\n--- Result {index} ---")

        print("Source:", document.metadata.get("source_file"))
        print("Category:", document.metadata.get("category"))

        print("Content:")
        print(document.page_content)

    assert len(results) > 0


if __name__ == "__main__":
    test_retriever()