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

        return results

    except Exception as e:
        return []


# entry point of the lambda
def lambda_handler(event, context):
    # proper changes have been made so that the code
    # can be executed by an event as well as via API Gateway.
    # event will not come via an api gateway call
    payload = event.get("body", None)

    if payload is None:
        url = event.get("pdf_url")
    else:
        json_payload = json.loads(payload)
        # get the url from the payload
        url = json_payload.get("pdf_url", None)

    # existing functionality
    loop = asyncio.get_event_loop()
    image_results = loop.run_until_complete(process(url))

    if len(image_results) > 0:
        response = {
            "status": 200,
            "body": json.dumps(image_results)
        }
    else:
        response = {
            "status": 500,
            "error": "Issues happened, please check logs"
        }

    return response

