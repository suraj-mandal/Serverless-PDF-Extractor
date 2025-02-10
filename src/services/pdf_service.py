import requests

from tenacity import retry, wait_random_exponential, stop_after_attempt

from pdf2image import convert_from_bytes
from PIL import Image
from io import BytesIO

from typing import List

from exceptions.invalid_url_exceptions import InvalidUrlException


class PdfService:

    def __init__(self, pdf_url):
        self._pdf_url = pdf_url
        self._content = None

    @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(3), reraise=True)
    async def extract_content(self):
        response = requests.get(self._pdf_url, timeout=30)
        response.raise_for_status()
        if response.headers.get('content-type') != 'application/pdf':
            raise InvalidUrlException('URL provided does not contain a PDF')
        self._content = response.content

    def extract_pages_from_pdf(self) -> List[Image.Image]:
        pdf_buffer = BytesIO()
        pdf_buffer.write(self._content)
        pdf_buffer.seek(0)

        return convert_from_bytes(pdf_buffer.read())
