
from ocr.pipeline import process_nutrition_label
from llm.model_loader import load_llm
from llm.prompt_templates import create_messages


def analyze_nutrition_label(
    image_path,
    child_age="Not provided",
    serving_size="Not provided"
):
    """
    Analyze a nutrition label using OCR and Groq LLM.

    Returns:
        dict: Nutrition analysis and OCR quality information.

    Raises:
        FileNotFoundError / ValueError: If OCR processing fails.
        RuntimeError: If LLM initialization or generation fails.
    """

    # 1. Process nutrition label using OCR
    # OCR errors are allowed to propagate from the pipeline.
    ocr_result = process_nutrition_label(image_path)

    # 2. Prepare OCR quality information
    ocr_quality_info = {
        "average_confidence": ocr_result["average_confidence"],
        "validation_warnings": ocr_result["validation_warnings"],
        "low_confidence_words": ocr_result["low_confidence_words"],
        "review_required": ocr_result["review_required"]
    }

    # 3. Create dynamic prompt
    messages = create_messages(
        nutrition_data=ocr_result["nutrition_data"],
        child_age=child_age,
        serving_size=serving_size,
        ocr_quality_info=ocr_quality_info
    )

    # 4. Initialize LLM and generate analysis
    try:
        llm = load_llm()
        response = llm.invoke(messages)

    except Exception as error:
        raise RuntimeError(
            "Failed to generate nutrition analysis. "
            "Check your Groq API key, model configuration, "
            "internet connection, and API availability."
        ) from error

    # 5. Return analysis and OCR information
    return {
        "analysis": response.content,
        "ocr_result": ocr_result
    }