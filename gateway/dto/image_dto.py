from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    image_url: HttpUrl
