from rag.qa_pipeline import retrieve_and_check


def test_qa_pipeline():

    questions = [
        "What is the capital of Japan?",
        "What foods should I give my 8-month-old baby, and exactly how many calories should the baby consume daily?",
        "At what age should complementary feeding begin?",
        "Should breastfeeding continue after 6 months?",
        "What is responsive feeding?",
        "What medicine should I give my child to treat severe malnutrition?"
    ]

    for question in questions:

        print("\n" + "=" * 75)
        print("QUESTION:", question)

        result = retrieve_and_check(
            query=question,
            k=3
        )

        print("\nEVIDENCE STATUS:")
        print(result["evidence"]["status"])

        print("\nVERIFIED SOURCES:")
        print(result["sources"])

        print("\nVERIFIED EVIDENCE:")

        for item in result["evidence"]["supporting_evidence"]:
            print(f"\nSource: {item['source_file']}")
            print(f"Quote: {item['quote']}")

        print("\nAANCHAL RESPONSE:")
        print(result["answer"])


if __name__ == "__main__":
    test_qa_pipeline()