import numpy
import cupy

from numbers import Number
from typing import Optional, Tuple, Union, Iterable
from ..array import ArrayType, register_array_type
from ..device import Device

__all__ = ['CrossPyArray', 'BasicIndexType', 'IndexType']

import logging


def _get_logger(name=None, *, level=logging.WARNING, fmt=logging.BASIC_FORMAT):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(fmt))
    logger.addHandler(ch)
    return logger


logger = _get_logger(
    __name__,
    # level=logging.DEBUG,
    fmt=
    '%(asctime)s [\033[1;4m%(levelname)s\033[0m %(processName)s:%(threadName)s] %(filename)s:%(lineno)s %(message)s'
)

BasicIndexType = Union[int, slice, Iterable[int]]  # non-recursive
IndexType = Union[BasicIndexType, Tuple[BasicIndexType, ...]]  # recursive


def dim_to_concat(shapes, expected) -> Optional[int]:
    # a boolean list of size #dimensions, true for dimension of same size
    mask = [len(set(d)) == 1 for d in zip(*shapes)]
    if len(mask) == 0:  # all scalars
        return None
    if all(mask): # can be concat by any dim
        if expected is None:
            logger.info("Concat dim not specified; use 0 by default")
            return 0
        return expected
    elif sum(mask) == len(mask) - 1:
        _dim = mask.index(False)
        if expected is not None and expected != _dim:
            raise ValueError(
                "Cannot concat on dim %s, but %s is feasible" %
                (expected, _dim)
            )
        return _dim
    raise ValueError(
        "Incompatible shapes with %s different dims" % (len(mask) - sum(mask))
    )


HANDLED_FUNCTIONS = {}


def implements(np_function):
    "Register an __array_function__ implementation."
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class CrossPyArray(numpy.lib.mixins.NDArrayOperatorsMixin):
    """
    Heterougeneous N-dimensional array compatible with the numpy API with custom implementations of numpy functionality.

    https://numpy.org/doc/stable/user/basics.dispatch.html#basics-dispatch
    """
    def __init__(self, array_list: list, dim=None) -> None:
        if len(array_list) == 0:
            raise NotImplementedError("array with no values not supported")

        try:
            shapes: tuple[tuple] = tuple(a.shape for a in array_list)
        except AttributeError:
            raise AttributeError("Arrays are required to have 'shape'")
            # TODO: __len__?
        if not all([len(s) == len(shapes[0]) for s in shapes]):
            # TODO: could have added 1 dimension
            raise ValueError("Array dimensions mismatch")
        logger.debug(shapes)

        # concat dim; TODO: support topological concat
        self._dim = dim_to_concat(shapes, dim)
        logger.debug(self._dim)
        if self._dim is None:  # scalar
            self._shape = ()
        else:
            # merge shapes
            shape = list(shapes[0])
            shape[self._dim] = sum([s[self._dim] for s in shapes])
            shape = tuple(shape)
            self._shape: tuple[int, ...] = shape
        logger.debug(self._shape)

        self._array_map = {}
        offsets = [
            0 for _ in range(len(self._shape))
        ]  # TODO topological concat
        for array in array_list:
            logger.debug(type(array))
            key = list(array.shape)  # list[int]
            for i in range(len(offsets)):
                key[i] = (
                    offsets[i], offsets[i] + key[i]
                )  # gradually to list[tuple[int, int]]
                if i == self._dim:
                    offsets[i] = key[i][1]
            key = tuple(key)  # tuple[tuple[int, int]]
            self._array_map[key] = array

    # @classmethod
    # def from_partition(self, partitions: dict[IndexType, ]):

    @property
    def shape(self):
        return tuple(self._shape)

    @property
    def devices(self):
        return {
            k: getattr(v, 'device', 'cpu')
            for k, v in self._array_map.items()
        }

    @property
    def types(self):
        return {k: type(v) for k, v in self._array_map.items()}

    def to_dict(self):
        return self._array_map

    def values(self):
        return list(self._array_map.values())

    def keys(self):
        return list(self._array_map.keys())

    def __repr__(self) -> str:
        return str("array %s" % self._array_map)

    def _index_intersection(
        self, part_range: tuple[int, int], target: BasicIndexType
    ) -> Union[BasicIndexType, None]:
        '''On one dimension, given the source range and target index, return

        TODO move to utils
        '''
        l, r = part_range
        if isinstance(
            target, int
        ) and l <= target < r:  # TODO negative indexing
            return (target - l)  # global to local
        elif isinstance(target, Iterable):
            in_range = [
                (i - l) for i in target if l <= i < r
            ]  # TODO negative indexing
            return in_range if len(in_range) else None
        elif isinstance(target, slice):
            new_start = None
            new_stop = None
            for i in range(
                target.start or 0, target.stop or r, target.step or 1
            ):
                if new_start is None and l <= i:
                    new_start = i
                if i < r:
                    new_stop = i + 1
            return slice(
                new_start - l, new_stop -
                l if new_stop is not None else None, target.step
            ) if new_start is not None else None
        return None

    def __getitem__(self, index: IndexType):  # -> Union[Array, List[Array]]
        """
        Note: CuPy handles out-of-bounds indices differently from NumPy. 
        NumPy handles them by raising an error, but CuPy wraps around them.
        """
        if self._shape == ():
            raise IndexError("scalar is not subscriptable")

        # unify the form to list of slices
        if not isinstance(index, tuple):
            index = (index, )

        if len(index) - len(self.shape) == 1 and index[-1] is Ellipsis:
            index = index[:-1]
        ret = []
        for k, v in self._array_map.items():
            local_indices = [
                self._index_intersection(
                    k[d], i if i is not Ellipsis else slice(None)
                ) for d, i in enumerate(index)
            ]
            if all([i is not None for i in local_indices]):
                ret.append(v[tuple(local_indices)])
        # TODO check out of range in advance
        if len(ret) == 0:
            raise IndexError("Index out of range")
        # FIXME: shape may change!!!
        return CrossPyArray(ret)

    def item(self):
        if self._shape != ():
            raise IndexError("cannot get item from non-scalars")
        return self._array_map.get(())

    def _check_index(self, index: Tuple[BasicIndexType]):
        def _meta_check(target, max):
            if isinstance(target,
                          int) and (0 <= target < max or 0 > target >= -max):
                return True
            elif isinstance(target, Iterable):
                return all([(0 <= i < max or 0 > i >= -max) for i in target])
            elif isinstance(target, slice):
                return all(
                    [
                        i < max for i in range(
                            target.start or 0, target.stop or max,
                            target.step or 1
                        )
                    ]
                )
            raise TypeError("index out of range", target, "vs", max)

        if not all(
            [_meta_check(i, self._shape[d]) for d, i in enumerate(index)]
        ):
            raise TypeError("index out of range")

    def __setitem__(self, index: IndexType, value):
        """
        Assign :param:`value` to a partition which may not on the current device.

        :param index: index of the target partition(s)

        .. todo:
            Assignment of different values to multiple partitions (ndarrays) are currently NOT supported. The :param:`value` is assigned as a whole to each of the target partition(s).
        """
        # unify the form to list of slices
        if not isinstance(index, tuple):
            index = (index, )

        self._check_index(index)

        def _target_shape(index, caps):
            def _target_dim_shape(target, max):
                if isinstance(target, int):
                    return 1
                elif isinstance(target, Iterable):
                    return sum(
                        [1 for _ in target]
                    )  # len() may not be available
                elif isinstance(target, slice):
                    return sum(
                        [
                            1 for _ in range(
                                target.start or 0, target.stop or max,
                                target.step or 1
                            )
                        ]
                    )
                raise TypeError("unknown index type")

            return [_target_dim_shape(i, caps[d]) for d, i in enumerate(index)]

        source_shape_start = None
        for k, v in self._array_map.items():
            local_indices = [
                self._index_intersection(k[d], i) for d, i in enumerate(index)
            ]
            if all([i is not None for i in local_indices]):
                target_shape = _target_shape(local_indices, [r[1] for r in k])
                for i in range(len(target_shape), len(k)):
                    target_shape.append(k[i][1] - k[i][0])
                if source_shape_start is None:
                    source_shape_start = [0 for _ in range(len(value.shape))]
                source_shape_end = [
                    a + b for a, b in
                    zip(source_shape_start, target_shape[-len(value.shape):])
                ]
                source_indices = [
                    slice(start, stop) for start, stop in
                    zip(source_shape_start, source_shape_end)
                ]
                source_shape_start = source_shape_end
                src = value[tuple(source_indices)
                           ] if len(source_indices) else value.item()
                if hasattr(v, 'device'):  # target is cupy array
                    with v.device:
                        v[tuple(local_indices)] = cupy.asarray(src)
                elif hasattr(value, 'device'):  # numpy <= cupy
                    v[tuple(local_indices)] = cupy.asnumpy(src)
                else:  # numpy <= numpy
                    v[tuple(local_indices)] = src

    def to(self, placement):
        if isinstance(placement, Iterable):
            return self._to_multidevice(placement)
        else:
            return self.all_to(placement)
    
    def _to_multidevice(self, placement):
        from ..ldevice import LDeviceSequenceBlocked
        Partitioner = LDeviceSequenceBlocked
        mapper = Partitioner(len(placement), placement=placement)
        arr_p = mapper.partition_tensor(self)
        return CrossPyArray(arr_p)

    def all_to(self, device):
        def _aggregate(concat, pull_op):
            output = None
            for k, v in sorted(self._array_map.items()):
                pulled = pull_op(v)
                if output is None:
                    output = pulled
                else:
                    diff_dim = -1
                    shape = [(0, s) for s in output.shape]
                    assert len(shape) == len(k)
                    for i, (range1, range2) in enumerate(zip(shape, k)):
                        if range1 != range2:
                            diff_dim = i
                            break
                    output = concat((output, pulled), axis=diff_dim)
            return output

        if (isinstance(device, Device) and device.__class__.__name__ == "_CPUDevice") or (isinstance(device, int) and device < 0):
            return _aggregate(numpy.concatenate, cupy.asnumpy)

        try:
            device = getattr(device, "cupy_device")
        except AttributeError:
            device = cupy.cuda.Device(device)
        with device:
            return _aggregate(cupy.concatenate, cupy.asarray)

    def __array__(self, dtype=None):
        """
        `numpy.array` or `numpy.asarray` that converts this array to a numpy array
        will call this __array__ method to obtain a standard numpy.ndarray.
        """
        return self.all_to(-1)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        """
        :param ufunc:   A function like numpy.multiply
        :param method:  A string, differentiating between numpy.multiply(...) and
                        variants like numpy.multiply.outer, numpy.multiply.accumulate,
                        and so on. For the common case, numpy.multiply(...), method == '__call__'.
        :param inputs:  A mixture of different types
        :param kwargs:  Keyword arguments passed to the function
        """
        # One might also consider adding the built-in list type to this
        # list, to support operations like np.add(array_like, list)
        _HANDLED_TYPES = (numpy.ndarray, Number, cupy.core.core.ndarray)
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of _HANDLED_TYPES.
            # Use ArrayLike instead of type(self) for isinstance to
            # allow subclasses that don't override __array_ufunc__ to
            # handle ArrayLike objects.
            if not isinstance(x, _HANDLED_TYPES + (CrossPyArray, )):
                logger.debug("not handling", type(x))
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        # inputs = tuple(x.values() if isinstance(x, CrossPyArray) else x
        #                for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.values() if isinstance(x, CrossPyArray) else x for x in out
            )

        if method == '__call__':
            scalars = []
            arrays = []
            mappings = None
            for input in inputs:
                if isinstance(input, Number):
                    scalars.append(input)
                elif isinstance(input, self.__class__):
                    arrays.append(input)
                    if mappings is not None:
                        if mappings != self.keys():
                            raise TypeError("inconsistent mappings")
                    else:
                        mappings = self.keys()
                else:
                    return NotImplemented
            # result = getattr(ufunc, method)(*inputs, **kwargs)
            result = [
                getattr(ufunc,
                        method)(*[numpy.asarray(a) for a in arrays], **kwargs)
            ]

            if type(result) is tuple:
                # multiple return values
                return tuple(type(self)(x) for x in result)
            elif method == 'at':
                # no return value
                return None
            else:
                # one return value
                return type(self)(result)  # self.__class__(result)
        else:
            raise NotImplementedError(method)
        return NotImplemented

    def __array_function__(self, func, types, args, kwargs):
        if func not in HANDLED_FUNCTIONS:
            return NotImplemented
        # Note: this allows subclasses that don't override
        # __array_function__ to handle DiagonalArray objects.
        if not all(issubclass(t, self.__class__) for t in types):
            return NotImplemented
        return HANDLED_FUNCTIONS[func](*args, **kwargs)


@implements(numpy.sum)
def x_sum(arr):
    "Implementation of np.sum for DiagonalArray objects"
    return arr  # FIXME


class _CrossPyArrayType(ArrayType):
    def can_assign_from(self, a, b):
        # TODO: We should be able to do direct copies from numpy to cupy arrays, but it doesn't seem to be working.
        # return isinstance(b, (cupy.ndarray, numpy.ndarray))
        raise NotImplementedError
        return isinstance(b, _Array)

    def get_memory(self, a):
        raise NotImplementedError
        return gpu(a.device.id).memory()

    def get_array_module(self, a):
        import sys
        return sys.modules[__name__]


register_array_type(CrossPyArray)(_CrossPyArrayType())
