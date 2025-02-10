import asyncio

from services.pdf_service import PdfService


async def async_main():
    pdf_service = PdfService('https://www.antennahouse.com/hubfs/xsl-fo-sample/pdf/basic-link-1.pdf')
    await pdf_service.extract_content()
    res = pdf_service.extract_pages_from_pdf()
    print(len(res))
    # print(res)


if __name__ == '__main__':
    asyncio.run(async_main())
