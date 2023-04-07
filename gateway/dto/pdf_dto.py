from pydantic import BaseModel, HttpUrl


class Pdf(BaseModel):
    pdf_url: HttpUrl
