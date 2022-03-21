from abottle.base_model import BaseModel


class PytorchModel(BaseModel):
    class Config:
        model = None

    def infer(self, X={}, Y=[]):
        return model(**X)
