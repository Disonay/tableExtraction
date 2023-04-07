from pydantic import BaseModel, HttpUrl


class ExctractorRequestDTO(BaseModel):
    pdf_url: HttpUrl
    table_coordinates: list[float]
