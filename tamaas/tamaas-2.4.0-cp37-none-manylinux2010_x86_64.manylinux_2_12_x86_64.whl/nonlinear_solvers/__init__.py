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

"""Nonlinear solvers for plasticity problems.

Solvers in this module use :py:mod:`scipy.optimize` to solve the implicit
non-linear equation for plastic deformations with fixed contact pressures.
"""
from functools import wraps

from scipy.optimize import newton_krylov, root
from scipy.optimize.nonlin import NoConvergence

from .. import EPSolver, Logger, LogLevel, mpi
from .._tamaas import _tolerance_manager
from .._tamaas import _DFSANESolver as DFSANECXXSolver


__all__ = ['NLNoConvergence',
           'DFSANESolver',
           'DFSANECXXSolver',
           'NewtonKrylovSolver',
           'ToleranceManager']


class NLNoConvergence(Exception):
    """Convergence not reached exception."""


class ScipySolver(EPSolver):
    """Base class for solvers wrapping SciPy routines."""

    def __init__(self, residual, model=None, callback=None):
        """Construct nonlinear solver with residual.

        :param residual: plasticity residual object
        :param model: Deprecated
        :param callback: passed on to the Scipy solver
        """
        super(ScipySolver, self).__init__(residual)

        if mpi.size() > 1:
            raise RuntimeError("Scipy solvers cannot be used with MPI; "
                               "DFSANECXXSolver can be used instead")

        self.callback = callback
        self._x = self.getStrainIncrement()
        self._residual = self.getResidual()
        self.options = {'ftol': 0, 'fatol': 1e-9}

    def solve(self):
        """Solve R(δε) = 0 using a Scipy function."""
        # For initial guess, compute the strain due to boundary tractions
        # self._residual.computeResidual(self._x)
        # self._x[...] = self._residual.getVector()
        EPSolver.beforeSolve(self)

        # Scipy root callback
        def compute_residual(vec):
            self._residual.computeResidual(vec)
            return self._residual.getVector().copy()

        # Solve
        self._x[...] = self._scipy_solve(compute_residual)

        # Computing displacements
        self._residual.computeResidualDisplacement(self._x)

    def reset(self):
        """Set solution vector to zero."""
        self._x[...] = 0

    def _scipy_solve(self, compute_residual):
        """Actually call the scipy solver.

        :param compute_residual: function returning residual for given variable
        """
        raise NotImplementedError()


class NewtonKrylovSolver(ScipySolver):
    """Solve using a finite-difference Newton-Krylov method."""

    def _scipy_solve(self, compute_residual):
        try:
            return newton_krylov(compute_residual, self._x,
                                 f_tol=self.tolerance,
                                 verbose=True, callback=self.callback)
        except NoConvergence:
            raise NLNoConvergence("Newton-Krylov did not converge")


class DFSANESolver(ScipySolver):
    """Solve using a spectral residual jacobianless method.

    See :doi:`10.1090/S0025-5718-06-01840-0` for details on method and
    the relevant Scipy `documentation
    <https://scipy.github.io/devdocs/reference/optimize.root-dfsane.html>`_ for
    details on parameters.

    """

    def _scipy_solve(self, compute_residual):
        solution = root(compute_residual,
                        self._x,
                        method='df-sane',
                        options={'ftol': 0, 'fatol': self.tolerance},
                        callback=self.callback)
        Logger().get(LogLevel.info) << \
            "DF-SANE/Scipy: {} ({} iterations, {})".format(
                solution.message,
                solution.nit,
                self.tolerance)

        if not solution.success:
            raise NLNoConvergence("DF-SANE/Scipy did not converge")
        return solution.x.copy()


def ToleranceManager(start, end, rate):
    """Decorate solver to manage tolerance of non-linear solve step."""

    def actual_decorator(cls):
        orig_init = cls.__init__
        orig_solve = cls.solve
        orig_update_state = cls.updateState

        @wraps(cls.__init__)
        def __init__(obj, *args, **kwargs):
            orig_init(obj, *args, **kwargs)
            obj.setToleranceManager(_tolerance_manager(start, end, rate))

        @wraps(cls.solve)
        def new_solve(obj, *args, **kwargs):
            ftol = obj.tolerance
            ftol *= rate

            obj.tolerance = max(ftol, end)
            return orig_solve(obj, *args, **kwargs)

        @wraps(cls.updateState)
        def updateState(obj, *args, **kwargs):
            obj.tolerance = start
            return orig_update_state(obj, *args, **kwargs)

        cls.__init__ = __init__
        # cls.solve = new_solve
        # cls.updateState = updateState
        return cls

    return actual_decorator
