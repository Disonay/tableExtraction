from gen.pdf_table_converter_pb2 import PdfFile
from gateway.clients.clients_instances import converter_client
from gen.pdf_table_detector_pb2 import Image


class ConverterService:
    def convert_pdf_to_image(self, pdf_url: str) -> Image:
        response = converter_client.Convert(PdfFile(pdf_url=pdf_url))

        return Image(image_url=response.image_url)
