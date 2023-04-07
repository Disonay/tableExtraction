from fastapi import APIRouter, Depends

from gateway.dto.coordinates_dto import TableCoordinates
from gateway.dto.image_dto import Image
from gateway.services.detector import DetectorService

router = APIRouter(prefix="/detector", tags=["Services"])


@router.post("/detect-table_area")
def detect_table_area(
        image: Image,
        detector_service: DetectorService = Depends(DetectorService),
) -> TableCoordinates:
    table_coordinates = detector_service.detect_table_area(image.image_url)

    return TableCoordinates(table_coordinates=table_coordinates)
