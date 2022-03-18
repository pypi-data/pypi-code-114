"""
CrossPy
=======

Provides
  1. Arbitrary slicing

"""

from typing import Iterable
import numpy
import cupy

from types import ModuleType

from crosspy.core.ndarray import IndexType

from .cpu import cpu
from .gpu import gpu

from .core import CrossPyArray

from .ldevice import PartitionScheme

# from .device import get_all_devices
# print(get_all_devices())

__all__ = ['numpy', 'cupy', 'array', 'cpu', 'gpu', 'PartitionScheme']


def fromarrays(
    arrayList,
    dtype=None,
    shape=None,
    formats=None,
    names=None,
    titles=None,
    aligned=False,
    byteorder=None,
    dim=None
):
    return CrossPyArray(arrayList, dim)


def array(
    obj: Iterable,
    dtype=None,
    shape=None,
    # offset=0,
    # strides=None,
    # formats=None,
    # names=None,
    # titles=None,
    # aligned=False,
    # byteorder=None,
    # copy=True,
    dim: int = None,
    *,
    partition=None,
    placement=None
):
    """
    Create a CrossPy array.

    :param obj: Same to ``numpy.array``.
    :param dtype: Same to ``numpy.array``.
    :param shape: Same to ``numpy.array``.
    :param dim: If ``obj`` has multiple arrays, merge them along dimension ``dim``.
    :param partition: A tuple of partitioning scheme.
    :return: A CrossPy array.
    """
    if obj is None:
        raise NotImplementedError("array with no content not supported")

    from .array import is_array
    if isinstance(obj, (list, tuple)):
        if all(is_array(a) for a in obj):
            arr = fromarrays(obj, dtype=dtype, shape=shape, dim=dim)
        else:
            # TODO: recursive iterables
            raise NotImplementedError
    else:
        arr = fromarrays(
            (obj if is_array(obj) else
             numpy.asarray(obj), ),  # TODO: hinted by placement
            dtype=dtype,
            shape=shape,
            dim=dim
        )

    if partition is None and placement is None:
        return arr

    if placement is not None:
        from .ldevice import LDeviceSequenceBlocked
        Partitioner = LDeviceSequenceBlocked
        mapper = Partitioner(len(placement), placement=placement)
        arr_p = mapper.partition_tensor(arr)
        return CrossPyArray(arr_p, dim)

    if partition is not None:
        from .ldevice import LDeviceSequenceArbitrary
        Partitioner = LDeviceSequenceArbitrary
        mapper = Partitioner(partition)
        arr_p = mapper.partition_tensor(arr)
        return CrossPyArray(arr_p, dim)


def asnumpy(input: CrossPyArray):
    return numpy.asarray(input)


def to(input, device: int):
    """
    Move CrossPy arrays to the device identified by device.

    :param input: The input array
    :type input: CrossPy array
    :param device: If ``device`` is a negative integer, the target device is CPU; otherwise GPU with the corresponding ID.
    :type device: int | cupy.cuda.Device
    :return: NumPy array if ``device`` refers to CPU, otherwise CuPy array.
    """
    return input.to(device)


def config_backend(backend):
    if isinstance(backend, ModuleType):
        backend = backend.__name__
    import sys
    submodules = {}
    for k, v in sys.modules.items():
        if k.startswith(f"{backend}."):
            setattr(sys.modules[__name__], k[len(backend) + 1:], v)
            submodules[k.replace(backend, __name__)] = v
    sys.modules.update(submodules)


config_backend(numpy)
