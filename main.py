import asyncio
import base64

from services.image_service import ImageService
from services.pdf_service import PdfService

from PIL import Image
from base64 import b64encode
import os

import io


async def process(pdf_url: str):
    try:
        pdf_service = PdfService(pdf_url)
        await pdf_service.extract_content()
        pages = pdf_service.extract_pages_from_pdf()

        return [
            ImageService.convert_to_base64(page) for page in pages
        ]

    except Exception as e:
        print(e)

# entry point of the lambda
def lambda_handler(event, context):
    asyncio.run(process(event.get("pdf_url")))

if __name__ == '__main__':
    # print(os.getcwd())
    im = Image.open('./tests/test_assets/placeholder.png')
    buffer = io.BytesIO()
    im.save(buffer, format='PNG')
    buffer.seek(0)
    print(base64.b64encode(buffer.getvalue()).decode())

