import tritonclient.http as httpclient
from tritonclient.utils import np_to_triton_dtype
from abottle.base_model import BaseModel


class TritonModel(BaseModel):
    class Config:
        name = ""
        version = ""
        triton_url = "trition.trition-system"

    def __init__(self):
        self.triton_client = httpclient.InferenceServerClient(
            url=self.Config.triton_url, insecure=True
        )

    def infer(self, X={}, Y=[]):
        inputs = []
        for x_name, x in X.items():
            infer_input = httpclient.InferInput(
                x_name, x.shape, np_to_triton_dtype(x.dtype)
            )
            infer_input.set_data_from_numpy(x)
            inputs.append(infer_input)

        outputs = []
        for y in Y:
            outputs.append(httpclient.InferRequestedOutput(y))
        results = self.triton_client.infer(
            self.Config.name,
            inputs,
            model_version=str(self.Config.version),
            outputs=outputs,
        )

        outputs = {}
        for y in Y:
            outputs[y] = results.as_numpy(y)
        return outputs
