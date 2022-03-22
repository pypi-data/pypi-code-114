# -*- mode: python; coding: utf-8 -*-
# vim: set ft=python:
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

"""Convenience utilities."""

import numpy as np
from contextlib import contextmanager
from typing import Iterable, Union
from . import (
    ContactSolver,
    Model,
    SurfaceGenerator1D,
    SurfaceGenerator2D,
    dtype,
    set_log_level,
    get_log_level,
    LogLevel
)


class NoConvergenceError(RuntimeError):
    """Convergence not reached exception."""


@contextmanager
def log_context(log_level: LogLevel):
    """Context manager to easily control Tamaas' logging level."""
    current = get_log_level()
    set_log_level(log_level)
    try:
        yield
    finally:
        set_log_level(current)


def load_path(solver: ContactSolver,
              loads: Iterable[Union[float, np.ndarray]],
              verbose: bool = False,
              callback=None) -> Iterable[Model]:
    """
    Generate model objects solutions for a sequence of applied loads.

    :param solver: a contact solver object
    :param loads: an iterable sequence of loads
    :param verbose: print info output of solver
    :param callback: a callback executed after the yield
    """
    log_level = LogLevel.info if verbose else LogLevel.warning

    with log_context(log_level):
        for load in loads:
            if solver.solve(load) > solver.tolerance:
                raise NoConvergenceError("Solver error exceeded tolerance")

            yield solver.model

            if callback is not None:
                callback()


def seeded_surfaces(generator: Union[SurfaceGenerator1D, SurfaceGenerator2D],
                    seeds: Iterable[int]) -> Iterable[np.ndarray]:
    """
    Generate rough surfaces with a prescribed seed sequence.

    :param generator: surface generator object
    :param seeds: random seed sequence
    """
    for seed in seeds:
        generator.random_seed = seed
        yield generator.buildSurface()


def hertz_surface(system_size: Iterable[float],
                  shape: Iterable[int],
                  radius: float) -> np.ndarray:
    """
    Construct a parabolic surface.

    :param system_size: size of the domain in each direction
    :param shape: number of points in each direction
    :param radius: radius of surface
    """
    coords = map(lambda L, N: np.linspace(0, L, N, endpoint=False,
                                          dtype=dtype),
                 system_size, shape)
    coords = np.meshgrid(*coords, 'ij', sparse=True)
    surface = (-1 / (2 * radius)) * sum((x-L/2)**2
                                        for x, L in zip(coords, system_size))
    return surface
