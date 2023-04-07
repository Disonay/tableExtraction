from fastapi import Depends

from gateway.services.converter import ConverterService
from gateway.services.detector import DetectorService
from gateway.services.extractor import ExtractorService

import json


class GeneralService:
    def __init__(
            self,
            converter_service: ConverterService = Depends(ConverterService),
            extractor_service: ExtractorService = Depends(ExtractorService),
            detector_service: DetectorService = Depends(DetectorService)
    ):
        self._converter_service = converter_service
        self._extractor_service = extractor_service
        self._detector_service = detector_service

    def full_extraction_process(self, pdf_url):
        img_url = self._converter_service.convert_pdf_to_image(pdf_url)
        table_coordinates = self._detector_service.detect_table_area(img_url)
        table_data = self._extractor_service.extract_table_from_pdf(pdf_url, table_coordinates)

        return table_data
