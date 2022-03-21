import onnxruntime as ort
from abottle.base_model import BaseModel


class ONNXModel(BaseModel):
    class Config:
        ort_file = ""

    def __init__(self):
        self.session = ort.InferenceSession(
            self.Config.ort_file,
            providers=["CUDAExecutionProvider"],
        )

    def infer(self, X={}, Y=[]):
        return self.session.run(None, X)
