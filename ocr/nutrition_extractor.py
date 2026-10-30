import re


NUTRIENTS = [
    "Calories",
    "Total Fat",
    "Saturated Fat",
    "Cholesterol",
    "Sodium",
    "Total Carbohydrate",
    "Dietary Fiber",
    "Total Sugar",
    "Protein",
    "Calcium",
    "Iron",
    "Potassium"
]


def extract_nutrition_data(text: str) -> dict:
    """
    Extract raw nutrition values from OCR text.
    """

    nutrition_data = {}

    for nutrient in NUTRIENTS:

        pattern = rf"^\s*{re.escape(nutrient)}\s+(.+?)\s*$"

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE | re.MULTILINE
        )

        if match:
            nutrition_data[nutrient] = match.group(1).strip()
        else:
            nutrition_data[nutrient] = None

    return nutrition_data

def parse_nutrition_values(nutrition_data: dict) -> dict:
    """
    Separate nutrient amounts from Daily Value percentages.
    """

    parsed_nutrition = {}

    for nutrient, value in nutrition_data.items():

        if value is None:
            parsed_nutrition[nutrient] = {
                "amount": None,
                "daily_value": None
            }
            continue

        match = re.match(
            r"^\s*(.*?)\s+(\d+(?:\.\d+)?)%\s*$",
            value
        )

        if match:
            amount = match.group(1).strip()
            daily_value = match.group(2) + "%"
        else:
            amount = value.strip()
            daily_value = None

        parsed_nutrition[nutrient] = {
            "amount": amount,
            "daily_value": daily_value
        }

    return parsed_nutrition

def validate_nutrition_data(parsed_nutrition: dict) -> list[str]:
    """
    Validate extracted nutrition values and flag suspicious results.
    """
    validation_warnings = []

    for nutrient, details in parsed_nutrition.items():
        amount = details["amount"]

        if amount is None:
            validation_warnings.append(
                f"{nutrient}: Value not found."
            )
            continue

        if nutrient != "Calories" and not re.search(r"\d", amount):
            validation_warnings.append(
                f"{nutrient}: No numeric value detected."
            )

        if nutrient == "Saturated Fat" and not re.search(
            r"\d+(?:\.\d+)?\s*g\b",
            amount,
            flags=re.IGNORECASE
        ):
            validation_warnings.append(
                f"{nutrient}: Amount or unit looks suspicious: {amount}"
            )

        if nutrient == "Potassium" and not re.search(
            r"\d+(?:\.\d+)?\s*(?:mg|g)\b",
            amount,
            flags=re.IGNORECASE
        ):
            validation_warnings.append(
                f"{nutrient}: Check the recognized amount and unit: {amount}"
            )

    return validation_warnings