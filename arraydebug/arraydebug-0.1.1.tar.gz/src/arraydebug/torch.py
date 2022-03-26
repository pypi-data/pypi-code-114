import torch

tensor_repr = torch.Tensor.__repr__


def tensor_info(tensor: torch.Tensor) -> str:
    """Return human-friendly debug info of the torch.tensor.
    :param tensor torch.Tensor: The tensor to look into.
    :return str: The string representation of the tensor.

    >>> tensor = torch.arange(3*4).reshape(3, 4)
    >>> print(tensor_info(tensor))
    <Tensor: shape=(3, 4), dtype=int64, device='cpu'>
    tensor([[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]])
    """
    attributes = [
        f"shape={tuple(tensor.shape)}",
        f"dtype={repr(tensor.dtype)[6:]}",
        f"device='{tensor.device}'",
    ]
    if tensor.requires_grad:
        attributes.append("requires_grad=True")

    return f"""\
<{tensor.__class__.__name__}: {', '.join(attributes)}>
{tensor.__repr__()}"""


# torch.Tensor.__repr__ = tensor_info
