import io

from PIL import Image


def image_to_bytes(image: Image) -> bytes:
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")

    return image_bytes.getvalue()
