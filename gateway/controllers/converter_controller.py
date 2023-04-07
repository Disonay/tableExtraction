from fastapi import APIRouter, Depends

from gateway.dto.pdf_dto import Pdf
from gateway.dto.image_dto import Image
from gateway.services.converter import ConverterService

router = APIRouter(prefix="/converter", tags=["Services"])


@router.post("/convert-pdf-to-image")
def convert_pdf_to_image(
        pdf: Pdf,
        converter_service: ConverterService = Depends(ConverterService),
) -> Image:
    return converter_service.convert_pdf_to_image(pdf.pdf_url)
