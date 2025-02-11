import asyncio
import json

from src.services import ImageService
from src.services import PdfService


async def process(pdf_url: str):
    try:
        print('Processing')
        pdf_service = PdfService(pdf_url)
        await pdf_service.extract_content()
        pages = pdf_service.extract_pages_from_pdf()

        print('Pages generated:', pages)

        results = [
            ImageService.convert_to_base64(page) for page in pages
        ]

        print(results)

        return {
            "statusCode": 200,
            "body": results
        }

    except Exception as e:
        return {
            "statusCode": 200,
            "body": [],
            "errors": str(e)
        }

# entry point of the lambda
def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(process(event['pdf_url']))
    return json.loads(json.dumps(response, default=str))

