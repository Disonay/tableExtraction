from concurrent import futures

import grpc

from gen.pdf_table_extractor_pb2 import TableData
from gen.pdf_table_extractor_pb2_grpc import (
    TableExtractionServiceServicer,
    add_TableExtractionServiceServicer_to_server,
)
from services.extractor.extractor_function import get_table_df
from services.extractor.utils import get_pdf_bytes, get_pdf_page, table_df_to_json
from services.extractor.consts import INSECURE_PORT, MAX_WORKERS


class TableExtractionService(TableExtractionServiceServicer):
    def Extract(self, request, context):
        pdf_bytes = get_pdf_bytes(request.pdf_url)
        pdf_page = get_pdf_page(pdf_bytes)
        table_df = get_table_df(pdf_page, request.table_coordinates)

        return TableData(table_data=table_df_to_json(table_df))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(MAX_WORKERS))
    add_TableExtractionServiceServicer_to_server(TableExtractionService(), server)
    server.add_insecure_port(INSECURE_PORT)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
