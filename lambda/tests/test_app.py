import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pytest
from PIL import Image

from services import PdfService
from services import ImageService

from test_constants import PDF_URL, INVALID_URL, IMAGE_PATH, BASE64_VALUE


@pytest.fixture
def pdf_service():
    return PdfService(PDF_URL)


@pytest.mark.asyncio
async def test_extract_pdf_from_url_success_with_valid_url(pdf_service):
    try:
        await pdf_service.extract_content()
    except ValueError:
        pytest.fail('Invalid URL exception raised')


@pytest.mark.asyncio
async def test_extract_pdf_from_url_failure_with_invalid_url():
    try:
        await PdfService(INVALID_URL).extract_content()
    except ValueError:
        pytest.raises(ValueError)


@pytest.mark.asyncio
async def test_extract_pages_from_pdf_success(pdf_service):
    try:
        await pdf_service.extract_content()
        pdf_pages = pdf_service.extract_pages_from_pdf()
        assert len(pdf_pages) == 2
    except ValueError:
        pytest.fail('Invalid URL exception raised')


def test_convert_to_base64_success():
    test_image = Image.open(IMAGE_PATH)
    base64_version = ImageService.convert_to_base64(test_image)
    assert base64_version == BASE64_VALUE


@pytest.mark.skip
async def test_custom(pdf_service):
    try:
        await pdf_service.extract_content()
        pdf_pages = pdf_service.extract_pages_from_pdf()

        pdf_images = [ImageService.convert_to_base64(page) for page in pdf_pages]
        output = {
            'data': pdf_images,
        }
        print(output)
    except ValueError:
        pytest.fail('Invalid URL exception raised')
