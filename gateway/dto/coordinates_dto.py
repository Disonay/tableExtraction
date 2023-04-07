from pydantic import BaseModel


class TableCoordinates(BaseModel):
    table_coordinates: list[float]
