from pathlib import Path

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader
)

def load_knowledge_documents(
    knowledge_base_dir="data/knowledge_base"
):
    """
    Load Markdown knowledge documents from the AANCHAL
    knowledge base using LangChain DirectoryLoader.

    Returns:
        list: LangChain Document objects with source metadata.
    """
    knowledge_base_path = Path(knowledge_base_dir)

    if not knowledge_base_path.exists():
        raise FileNotFoundError(
            f"Knowledge base directory not found: "
            f"{knowledge_base_path}"
        )

    loader = DirectoryLoader(
        str(knowledge_base_path),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        recursive=True
    )

    documents = loader.load()

    # Exclude source registry and add metadata.
    filtered_documents = []

    for document in documents:

        source_path = Path(document.metadata["source"])

        if source_path.name == "source_registry.md":
            continue

        document.metadata.update({
            "source_file": source_path.name,
            "source_id": source_path.stem,
            "category": source_path.parent.name,
            "source_path": source_path.relative_to(
                knowledge_base_path
            ).as_posix()
        })

        filtered_documents.append(document)

    if not filtered_documents:
        raise ValueError(
            "No knowledge documents found in the knowledge base."
        )

    return filtered_documents