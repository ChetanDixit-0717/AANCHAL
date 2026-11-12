from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_knowledge_documents(
    documents,
    chunk_size=800,
    chunk_overlap=100
):
    """
    Split knowledge documents into smaller overlapping chunks.

    Args:
        documents: List of LangChain Document objects.
        chunk_size: Maximum target chunk size in characters.
        chunk_overlap: Number of overlapping characters.

    Returns:
        list: Split LangChain Document objects.
    """

    if not documents:
        raise ValueError("No documents provided for splitting.")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be non-negative "
            "and smaller than chunk_size."
        )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
        add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)

    if not chunks:
        raise ValueError("Document splitting produced no chunks.")

    return chunks