import base64
from concurrent import futures

import grpc
import requests
from pdf2image import convert_from_bytes

from gen.pdf_table_converter_pb2 import Image
from gen.pdf_table_converter_pb2_grpc import (
    Pdf2ImgConverterServiceServicer,
    add_Pdf2ImgConverterServiceServicer_to_server,
)
from image_store import imagekit
from services.converter.utils import image_to_bytes

from services.converter.consts import POPPLER_PATH, FILE_NAME, MAX_WORKERS, INSECURE_PORT


class Pdf2ImgConverterService(Pdf2ImgConverterServiceServicer):
    def Convert(self, request, context):
        pdf = requests.get(request.pdf_url, stream=True)
        image = convert_from_bytes(
            pdf.content,
            poppler_path=POPPLER_PATH,
        )[0]

        image_bytes = image_to_bytes(image)
        result = imagekit.upload_file(base64.b64encode(image_bytes), file_name=FILE_NAME)

        return Image(image_url=result.url)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    add_Pdf2ImgConverterServiceServicer_to_server(Pdf2ImgConverterService(), server)
    server.add_insecure_port(INSECURE_PORT)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
