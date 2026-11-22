from rag.retriever import retrieve_relevant_documents
from rag.evidence_checker import check_evidence
from chatbot.chatbot import get_chatbot_response


def generate_grounded_answer(query, evidence):
    """
    Generate an answer using only verified evidence.

    Do not invoke the LLM when evidence is insufficient
    or explicitly outside the knowledge-base scope.
    """

    status = evidence["status"]

    # 1. Handle unsupported questions without calling the LLM
    if status == "explicitly_out_of_scope":
        return (
            "I don't currently have verified information "
            "about this topic in the AANCHAL knowledge base. "
            "Please consult a qualified healthcare professional "
            "or your local Anganwadi worker."
        )

    if status == "insufficient_evidence":
        return (
            "I don't currently have enough verified information "
            "to answer this question reliably. "
            "Please consult your local Anganwadi worker."
        )

    # 2. Prepare only verified supporting passages
    supporting_evidence = evidence["supporting_evidence"]

    if not supporting_evidence:
        return (
            "I couldn't verify sufficient supporting information "
            "to answer this question reliably."
        )

    context_parts = [
        "The following passages have been verified "
        "against their original source documents."
    ]

    for item in supporting_evidence:
        context_parts.append(
            f"Source: {item['source_file']}\n"
            f"Evidence: {item['quote']}"
        )

    # 3. Inform the chatbot if evidence is partial
    if status == "partially_supported":
        context_parts.append(
            "IMPORTANT: The available evidence only partially "
            "answers the question. Answer only the supported "
            "part and clearly explain what information is missing."
        )

        missing_information = evidence.get(
            "missing_information", []
        )

        if missing_information:
            context_parts.append(
                "Missing information:\n"
                + "\n".join(
                    f"- {item}" for item in missing_information
                )
            )

    context = "\n\n".join(context_parts)

    # 4. Generate the grounded response
    return get_chatbot_response(
        question=query,
        context=context
    )


def retrieve_and_check(query, vector_store=None, k=3):
    """Retrieve documents, evaluate evidence and generate an answer."""

    documents = retrieve_relevant_documents(
        query=query,
        vector_store=vector_store,
        k=k
    )

    evidence_result = check_evidence(
        query=query,
        documents=documents
    )

    answer = generate_grounded_answer(
        query=query,
        evidence=evidence_result
    )

    # Extract source filenames from verified evidence.
    sources = sorted({
        item["source_file"]
        for item in evidence_result["supporting_evidence"]
    })

    return {
        "query": query,
        "documents": documents,
        "evidence": evidence_result,
        "sources": sources,
        "answer": answer
    }