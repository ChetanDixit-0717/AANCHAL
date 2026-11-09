import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def load_llm():
    api_key = os.getenv("GROQ_API_KEY")
    model_name = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")

    llm = ChatGroq(
        model=model_name,
        api_key=api_key,
        temperature=0.3,
        max_tokens=2048
    )

    return llm