from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from gateway.services.extractor import ExtractorService

from gateway.dto.extractor_dto import ExctractorRequestDTO

router = APIRouter(prefix="/extractor", tags=["Services"])


@router.post("/extract_table_from_pdf")
def extract_table_from_pdf(
        request: ExctractorRequestDTO,
        extractor_service: ExtractorService = Depends(ExtractorService),
) -> JSONResponse:
    data = extractor_service.extract_table_from_pdf(request.pdf_url, request.table_coordinates)

    return JSONResponse(data)
