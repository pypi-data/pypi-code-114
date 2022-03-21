try:
    from abottle.trt_model import TensorRTModel
except ImportError:
    print("TensorRTModel import failed, ignoreing...")

try:
    from abottle.onnx_model import ONNXModel
except ImportError:
    print("ONNXModel import failed, ignoreing...")

try:
    from abottle.triton_model import TritonModel
except ImportError:
    print("TritonModel import failed, ignoreing...")

try:
    from abottle.pytorch_model import PytorchModel
except ImportError:
    print("PytorchModel import failed, ignoreing...")

from abottle.base_model import BaseModel
