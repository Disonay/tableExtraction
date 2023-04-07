from gateway.clients.clients_instances import detector_client
from gen.pdf_table_detector_pb2 import Image


class DetectorService:
    def detect_table_area(self, image_url: str):
        response = detector_client.Detect(Image(image_url=image_url))

        return list(response.table_coordinates)
