from llm.model_loader import load_llm
from llm.prompt_templates import create_messages

nutrition_data = {
    "calories": "180 kcal",
    "total_fat": "6g",
    "saturated_fat": "2g",
    "sodium": "300mg",
    "total_carbohydrates": "25g",
    "dietary_fiber": "2g",
    "total_sugar": "15g",
    "added_sugar": None,
    "protein": "3g"
}

child_age = "4 years"
serving_size = "30g"

llm = load_llm()
messages = create_messages(
    nutrition_data=nutrition_data,
    child_age=child_age,
    serving_size=serving_size
)

response = llm.invoke(messages)

print(response.content)