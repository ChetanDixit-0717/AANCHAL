import os
import pytesseract
import numpy as np

tesseract_path = os.getenv("TESSERACT_CMD")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

def extract_text(image: np.ndarray) -> str:
    """Extract text from an image using Tesseract OCR."""
    return pytesseract.image_to_string(image)

def extract_text_with_confidence(image: np.ndarray) -> dict:
    ocr_data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )

    results = []

    for word, confidence in zip(
        ocr_data["text"],
        ocr_data["conf"]
    ):
        if word.strip() and float(confidence) >= 0:
            results.append({
                "word": word,
                "confidence": float(confidence)
            })

    return results