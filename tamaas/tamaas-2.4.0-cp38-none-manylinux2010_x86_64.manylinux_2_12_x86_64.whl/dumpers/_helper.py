# -*- mode:python; coding: utf-8 -*-
#
# Copyright (©) 2016-2022 EPFL (École Polytechnique Fédérale de Lausanne),
# Laboratory (LSMS - Laboratoire de Simulation en Mécanique des Solides)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Helper functions for dumpers
"""
from os import PathLike
from functools import wraps
from pathlib import Path

import io
import numpy as np

from .. import model_type, type_traits, mpi

__all__ = ["step_dump", "directory_dump"]

_basic_types = [t for t, trait in type_traits.items() if trait.components == 1]


def _is_surface_field(field, model):
    bn = model.boundary_shape
    gn = mpi.global_shape(bn)
    shape = list(field.shape)

    # Also test number of components to weed out cases where shape is the same
    # in all directions
    if model.type not in _basic_types:
        bn.append(type_traits[model.type].components)
        gn.append(bn[-1])

    # Testing works for both local and global fields
    return shape == bn or shape == gn


def local_slice(field, model):
    n = model.shape
    bn = model.boundary_shape

    gshape = mpi.global_shape(bn)
    offsets = np.zeros_like(gshape)
    offsets[0] = mpi.local_offset(gshape)

    if not _is_surface_field(field, model) and len(n) > len(bn):
        gshape = [n[0]] + gshape
        offsets = np.concatenate(([0], offsets))

    shape = bn if _is_surface_field(field, model) else n
    if len(field.shape) > len(shape):
        shape += field.shape[len(shape):]

    def sgen(pair):
        offset, size = pair
        return slice(offset, offset + size, None)

    def sgen_basic(pair):
        offset, size = pair
        return slice(offset, offset + size)

    slice_gen = sgen_basic if model_type in _basic_types else sgen
    return tuple(map(slice_gen, zip(offsets, shape)))


def step_dump(cls):
    """
    Decorator for dumper with counter for steps
    """
    orig_init = cls.__init__
    orig_dump = cls.dump

    @wraps(cls.__init__)
    def __init__(obj, *args, **kwargs):
        orig_init(obj, *args, **kwargs)
        obj.count = 0

    def postfix(obj):
        return "_{:04d}".format(obj.count)

    @wraps(cls.dump)
    def dump(obj, *args, **kwargs):
        orig_dump(obj, *args, **kwargs)
        obj.count += 1

    cls.__init__ = __init__
    cls.dump = dump
    cls.postfix = property(postfix)

    return cls


def directory_dump(directory=""):
    "Decorator for dumper in a directory"
    directory = Path(directory)

    def actual_decorator(cls):
        orig_dump = cls.dump
        orig_filepath = cls.file_path.fget

        @wraps(cls.dump)
        def dump(obj, *args, **kwargs):
            if mpi.rank() == 0:
                directory.mkdir(parents=True, exist_ok=True)

            orig_dump(obj, *args, **kwargs)

        @wraps(cls.file_path.fget)
        def file_path(obj):
            return str(directory / orig_filepath(obj))

        cls.dump = dump
        cls.file_path = property(file_path)

        return cls

    return actual_decorator


def hdf5toVTK(inpath, outname):
    """Convert HDF5 dump of a model to VTK."""
    from . import UVWDumper  # noqa
    from . import H5Dumper   # noqa
    UVWDumper(outname, all_fields=True) << H5Dumper("").read(inpath)


def file_handler(mode):
    """Decorate a function to accept path-like or file handles."""
    def _handler(func):
        @wraps(func)
        def _wrapped(self, fd, *args, **kwargs):
            if isinstance(fd, (str, PathLike)):
                with open(fd, mode) as fd:
                    return _wrapped(self, fd, *args, **kwargs)
            elif isinstance(fd, io.TextIOBase):
                return func(self, fd, *args, **kwargs)

            raise TypeError(
                f"Expected a path-like or file handle, got {type(fd)}")

        return _wrapped
    return _handler
