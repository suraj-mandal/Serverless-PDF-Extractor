import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pytest

from exceptions.invalid_url_exceptions import InvalidUrlException
from services.pdf_service import PdfService

PDF_URL = 'https://www.antennahouse.com/hubfs/xsl-fo-sample/pdf/basic-link-1.pdf'
INVALID_URL = 'https://jsonplaceholder.typicode.com/'


@pytest.fixture
def pdf_service():
    return PdfService(PDF_URL)


@pytest.mark.asyncio
async def test_extract_pdf_from_url_success_with_valid_url(pdf_service):
    try:
        await pdf_service.extract_content()
    except InvalidUrlException:
        pytest.fail('Invalid URL exception raised')


@pytest.mark.asyncio
async def test_extract_pdf_from_url_failure_with_invalid_url():
    try:
        await PdfService(INVALID_URL).extract_content()
    except InvalidUrlException:
        pytest.raises(InvalidUrlException)


@pytest.mark.asyncio
async def test_extract_pages_from_pdf_success(pdf_service):
    try:
        await pdf_service.extract_content()
        pdf_pages = pdf_service.extract_pages_from_pdf()
        assert len(pdf_pages) == 2
    except InvalidUrlException:
        pytest.fail('Invalid URL exception raised')
