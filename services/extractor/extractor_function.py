import pandas as pd
import PyPDF2
import tempfile

import camelot

from services.extractor.utils import crop_pdf_to_table


def get_table_df(page: PyPDF2.PageObject, table_coordinates: list) -> pd.DataFrame:
    pdf_writer = PyPDF2.PdfWriter()

    crop_pdf_to_table(page, table_coordinates)
    pdf_writer.add_page(page)

    with tempfile.NamedTemporaryFile(suffix='.pdf', mode='wb', delete=False) as fo:
        pdf_writer.write(fo)
        fo.close()
        tables = camelot.read_pdf(fo.name)

    return tables[0].df.replace('\\n', ' ', regex=True)
