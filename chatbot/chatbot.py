from llm.model_loader import load_llm
from chatbot.prompt_templates import create_chatbot_messages

def get_chatbot_response(question, context=""):
    """
    Generate a response to a child nutrition question
    using the AANCHAL chatbot and Groq LLM.

    Args:
        question (str): User's question.
        context (str): Retrieved nutrition information.
                      Will be supplied by the RAG pipeline later.

    Returns:
        str: Generated chatbot response.

    Raises:
        ValueError: If the question is empty or invalid.
        RuntimeError: If LLM initialization or generation fails.
    """

    if not isinstance(question, str) or not question.strip():
        raise ValueError("Please provide a valid question.")

    if not isinstance(context, str) or not context.strip():
        return (
            "I don't currently have verified information "
            "to answer this question reliably. "
            "Please consult a qualified healthcare "
            "professional or your local Anganwadi worker."
        )

    try:
        messages = create_chatbot_messages(
            context = context,
            question = question
        )

        llm = load_llm()
        response = llm.invoke(messages)

        return response.content.strip()

    except Exception as error:
        raise RuntimeError(
            "Failed to generate chatbot response. "
            "Check your Groq API key, model configuration, "
            "internet connection, and API availability."
        ) from error