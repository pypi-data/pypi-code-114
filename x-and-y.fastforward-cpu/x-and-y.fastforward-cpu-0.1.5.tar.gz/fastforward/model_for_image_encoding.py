from typing import List, Tuple, Optional

import numpy as np
import onnxruntime
from PIL.Image import Image

# TODO: handle grayscale images
mean = np.array([0.485, 0.456, 0.406]).reshape(-1, 1, 1)
std = np.array([0.229, 0.224, 0.225]).reshape(-1, 1, 1)


def transform(image: Image, size: (int, int)):
    # DINO models are size invariant (only has to be multiple of patch size)
    # there is of course a tradeoff between speed and accuracy
    # 288 is the same as used for the CLIP model
    image = image.resize(size, Image.BILINEAR)

    array = np.asarray(image)
    array = array / 255
    array = array.transpose((2, 0, 1))
    array = array - mean
    array = array / std
    array = np.expand_dims(array, axis=0).astype("float32")

    return array


class ModelForImageEncoding:

    def __init__(self, onnx_model_path: str, output_name: Optional[str] = None):
        self.model = onnxruntime.InferenceSession(onnx_model_path)
        self.output_name = output_name

    def __call__(self, images: List[Image]):
        squeeze = not isinstance(images, list)
        images = images if isinstance(images, list) else [images]

        batch = [transform(image, self.get_input_dim()) for image in images]
        batch = np.concatenate(batch, axis=0)

        result = self.model.run([self.get_output_name()], {self.get_input_name(): batch})[0]
        return np.squeeze(result) if squeeze else result

    def get_input_name(self) -> str:
        return self.model.get_inputs()[0].name

    def get_output_name(self) -> str:
        return self.output_name or self.model.get_outputs()[0].name

    def get_input_dim(self) -> Tuple[int, int]:
        shape = self.model.get_inputs()[0].shape
        return shape[-2], shape[-1]

    def get_output_dim(self):
        return self.model.get_outputs()[0].shape[-1]
