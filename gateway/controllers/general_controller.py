from fastapi import APIRouter, Depends
from gateway.dto.pdf_dto import Pdf
from fastapi.responses import JSONResponse

from gateway.services.general import GeneralService

router = APIRouter(prefix="/pipeline", tags=["General"])


@router.post("/extract")
def full_extraction_process(
        pdf: Pdf,
        general_service: GeneralService = Depends(GeneralService),
) -> JSONResponse:
    data = general_service.full_extraction_process(pdf.pdf_url)

    return JSONResponse(data)
