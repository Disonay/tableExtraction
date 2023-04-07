from concurrent import futures
from io import BytesIO

import grpc
import requests
from PIL import Image

from gen.pdf_table_detector_pb2 import TableCoordinates
from gen.pdf_table_detector_pb2_grpc import (
    TableAreaDetectorServiceServicer,
    add_TableAreaDetectorServiceServicer_to_server,
)
from services.detector.detector_function import get_table_coordinates
from services.detector.consts import MAX_WORKERS, INSECURE_PORT


class TableAreaDetectorService(TableAreaDetectorServiceServicer):
    def Detect(self, request, context):
        response = requests.get(request.image_url)
        img = Image.open(BytesIO(response.content))
        table_coordinates = get_table_coordinates(img)

        return TableCoordinates(table_coordinates=table_coordinates)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(MAX_WORKERS))
    add_TableAreaDetectorServiceServicer_to_server(TableAreaDetectorService(), server)
    server.add_insecure_port(INSECURE_PORT)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
