from PIL import Image
from model import TableAreaDetectionModel


def get_table_coordinates(img: Image) -> list:
    model = TableAreaDetectionModel()
    model.fit(img)

    return model.predict()
