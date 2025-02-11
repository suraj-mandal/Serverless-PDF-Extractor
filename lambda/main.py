import asyncio

from services import ImageService
from services import PdfService


async def process(pdf_url: str):
    try:
        print('Processing')
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

