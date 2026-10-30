import cv2
import numpy as np

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_threshold(
        gray_image: np.ndarray,
        threshold_value: int = 150,
) -> np.ndarray:
    _, binary_image = cv2.threshold(
        gray_image,
        threshold_value,
        255,
        cv2.THRESH_BINARY,
    )

    return binary_image

def apply_adaptive_threshold(
        gray_image: np.ndarray,
        block_size: int = 31,
        constant: int = 10,
) -> np.ndarray:
    if block_size < 3 or block_size % 2 == 0:
         raise ValueError("block_size must be an odd integer >= 3.")

    return cv2.adaptiveThreshold(
        gray_image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        block_size,
        constant,
    )

def resize_image(
    image: np.ndarray,
    scale_factor: float = 2.0,
) -> np.ndarray:
    """Resize an image using cubic interpolation."""
    if scale_factor <= 0:
        raise ValueError("scale_factor must be greater than 0.")

    return cv2.resize(
        image,
        None,
        fx=scale_factor,
        fy=scale_factor,
        interpolation=cv2.INTER_CUBIC,
    )

