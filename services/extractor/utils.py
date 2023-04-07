from io import BytesIO

import PyPDF2
import pandas as pd
import requests

from services.extractor.consts import COEFFICIENT


def get_pdf_bytes(pdf_url: str) -> BytesIO:
    pdf_response = requests.get(pdf_url, stream=True)

    return BytesIO(pdf_response.content)


def get_pdf_page(pdf_bytes):
    pdf_reader = PyPDF2.PdfReader(pdf_bytes)
    page = pdf_reader.pages[0]

    return page


def crop_pdf_to_table(page: PyPDF2.PageObject, table_coordinates: list):
    upper_left = float(page.cropbox.upper_left[1])

    page.cropbox.upper_right = (table_coordinates[0] / COEFFICIENT, upper_left - table_coordinates[1] / COEFFICIENT)
    page.cropbox.lower_left = (table_coordinates[2] / COEFFICIENT, upper_left - table_coordinates[3] / COEFFICIENT)


def table_df_to_json(table_df: pd.DataFrame) -> str:
    return table_df.to_json(orient="records")
