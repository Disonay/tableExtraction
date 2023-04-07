import grpc

from gen.pdf_table_converter_pb2_grpc import Pdf2ImgConverterServiceStub
from gen.pdf_table_detector_pb2_grpc import TableAreaDetectorServiceStub
from gen.pdf_table_extractor_pb2_grpc import TableExtractionServiceStub

converter_client = Pdf2ImgConverterServiceStub(grpc.insecure_channel('localhost:50051'))
detector_client = TableAreaDetectorServiceStub(grpc.insecure_channel('localhost:50052'))
extractor_client = TableExtractionServiceStub(grpc.insecure_channel('localhost:50053'))
