from gateway.clients.clients_instances import extractor_client
from gen.pdf_table_extractor_pb2 import TableExtractionRequest
import json


class ExtractorService:
    def extract_table_from_pdf(self, pdf_url: str, table_coordinates: list):
        response = extractor_client.Extract(TableExtractionRequest(
            pdf_url=pdf_url,
            table_coordinates=table_coordinates,
        ))
        table_data = response.table_data

        return json.loads(table_data)
