
from rag.embedding_model import load_embedding_model


def test_embedding_model():

    embedding_model = load_embedding_model()

    text = "Complementary feeding begins at around six months."

    embedding = embedding_model.embed_query(text)

    print("Embedding model loaded successfully!")
    print("Embedding dimensions:", len(embedding))
    print("First five values:", embedding[:5])

    assert len(embedding) == 384


if __name__ == "__main__":
    test_embedding_model()