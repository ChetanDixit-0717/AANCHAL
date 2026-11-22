from rag.vector_store import load_vector_store


def retrieve_relevant_documents(
    query,
    vector_store=None,
    k=3
):

    if not isinstance(query, str) or not query.strip():
        raise ValueError("Please provide a valid query.")

    if k <= 0:
        raise ValueError("k must be greater than zero.")

    if vector_store is None:
        vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": 10,
            "lambda_mult": 0.7
        }
    )

    results = retriever.invoke(query)

    return results