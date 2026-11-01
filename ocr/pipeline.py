from pathlib import Path
from ocr.image_loader import load_image
from ocr.image_preprocessing import convert_to_grayscale
from ocr.text_recognizer import (
    extract_text,
    extract_text_with_confidence,
    calculate_average_confidence
)
from ocr.nutrition_extractor import (
    extract_nutrition_data,
    parse_nutrition_values,
    validate_nutrition_data
)

def process_nutrition_label(image_path):
    """
    Process a nutrition label image and return extracted nutrition data.
    """
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(
            f"Nutrition label image not found: {image_path}"
        )

    if not image_path.is_file():
        raise ValueError(
            f"Expected a file, received: {image_path}"
        )
    
    # 1. Load image
    image = load_image(image_path)

    # 2. Preprocess image
    processed_image = convert_to_grayscale(image)

    # 3. Extract text
    extracted_text = extract_text(processed_image)

    # 4. Extract OCR confidence scores
    confidence_data = extract_text_with_confidence(processed_image)

    # 5. Extract raw nutrition values
    nutrition_data = extract_nutrition_data(extracted_text)
    average_confidence = calculate_average_confidence(confidence_data)

    # 6. Parse amounts and Daily Values
    parsed_nutrition = parse_nutrition_values(nutrition_data)

    # 7. Validate extracted values
    validation_warnings = validate_nutrition_data(parsed_nutrition)

    # 8. Check for low-confidence OCR words
    low_confidence_words = [
        item for item in confidence_data
        if item["confidence"] < 80
    ]

    # 9. Determine whether manual review is required
    review_required = (
        len(validation_warnings) > 0
        or len(low_confidence_words) > 0
    )

    return {
        "extracted_text": extracted_text,
        "confidence_data": confidence_data,
        "average_confidence": average_confidence,
        "low_confidence_words": low_confidence_words,
        "nutrition_data": parsed_nutrition,
        "validation_warnings": validation_warnings,
        "review_required": review_required
    }