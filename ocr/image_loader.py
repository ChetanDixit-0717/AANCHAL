from pathlib import Path

import cv2

def load_image(image_path: str | Path):
    """Load an image and raise an error if it can't be read."""
    image_path = Path(image_path)

    image = cv2.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(
            f"Unable to load image: {image_path}"
        )

    return image

def main():
    project_root = Path(__file__).resolve().parents[1]

    image_path = (
        project_root
        / "data"
        / "sample_images"
        / "nutrition_label.png"
    )

    image = load_image(image_path)

    print("Image loaded successfully!")
    print("Shape:", image.shape)
    print("Data type:", image.dtype)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    import matplotlib.pyplot as plt

    plt.imshow(image_rgb)
    plt.title("Nutrition Label")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()