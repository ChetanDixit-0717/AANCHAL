from llm.model_loader import load_llm

llm = load_llm()

response = llm.invoke(
    "Explain why understanding nutrition labels is important in 2 sentences."
)

print("\nLLM RESPONSE:\n")
print(response.content)