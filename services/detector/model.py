from transformers import TableTransformerForObjectDetection
from transformers import DetrFeatureExtractor
from PIL import Image
import torch

from services.detector.consts import PRETRAINED


class TableAreaDetectionModel:
    def __init__(self):
        self.model = TableTransformerForObjectDetection.from_pretrained(PRETRAINED)
        self.feature_extractor = DetrFeatureExtractor()
        self.img = None

    def predict(self, threshold=0.7):
        self._prepare_img()
        encoding = self.feature_extractor(self.img, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**encoding)

        results = self.feature_extractor.post_process_object_detection(
            outputs,
            threshold=threshold,
            target_sizes=[self.img.size],
        )[0]

        return results['boxes'].tolist()[0]

    def fit(self, image: Image):
        self.img = image.copy()

    def _prepare_img(self):
        width, height = self.img.size
        self.img.resize((int(width * 0.5), int(height * 0.5)))
