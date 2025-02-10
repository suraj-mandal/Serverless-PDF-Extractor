import base64
import io

from PIL import Image


class ImageService:

    @staticmethod
    def convert_to_base64(image: Image.Image, image_format: str = "PNG"):
        buffer = io.BytesIO()
        image.save(buffer, format=image_format)
        buffer.seek(0)
        return base64.b64encode(buffer.getvalue()).decode()
