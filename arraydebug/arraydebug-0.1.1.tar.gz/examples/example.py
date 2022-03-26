import numpy as np
import torch
import pandas as pd

# import arraydebug after numpy, torch, and pandas
# you may add '# noqa' comment to suppress "imported but unused" warning
import arraydebug  # noqa


def fn():
    arr = np.arange(24).reshape(6, 4) + 1000

    tensor = torch.rand(6, 4, requires_grad=True)

    df = pd.DataFrame(arr, index=pd.date_range("20130101", periods=6), columns=list("ABCD"))

    print(repr(arr), "\n")
    print(repr(tensor), "\n")
    print(repr(df), "\n")


fn()
