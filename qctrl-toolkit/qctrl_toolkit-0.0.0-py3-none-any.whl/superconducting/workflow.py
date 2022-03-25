# Copyright 2022 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""
Convenience functions for superconducting systems.
"""

from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Optional,
    Union,
)

import numpy as np
from qctrlcommons.exceptions import QctrlArgumentsValueError
from qctrlcommons.graph import Graph
from qctrlcommons.preconditions import (
    check_argument,
    check_argument_positive_integer,
)

from qctrltoolkit.namespace import Namespace
from qctrltoolkit.utils import expose


class OptimizableCoefficient(ABC):
    """
    Abstract class for optimizable Hamiltonian coefficients.
    """

    @abstractmethod
    def get_pwc(self, graph, gate_duration, name):
        """
        Return a Pwc representation of the optimizable coefficient.
        """
        raise NotImplementedError


@expose(Namespace.SUPERCONDUCTING)
@dataclass
class RealOptimizableConstant(OptimizableCoefficient):
    """
    A real-valued optimizable constant coefficient for a Hamiltonian term.
    The main function will try to find the optimal value for this constant.

    Attributes
    ----------
    min : float
        The minimum value that the coefficient can take.
    max : float
        The maximum value that the coefficient can take.
    """

    min: float
    max: float

    def __post_init__(self):
        check_argument(
            self.min < self.max,
            "The maximum must be larger than the minimum.",
            {"min": self.min, "max": self.max},
        )

    def get_pwc(self, graph, gate_duration, name):
        value = graph.optimization_variable(1, self.min, self.max)[0]
        value.name = name
        return graph.constant_pwc(constant=value, duration=gate_duration)


@expose(Namespace.SUPERCONDUCTING)
@dataclass
class ComplexOptimizableConstant(OptimizableCoefficient):
    """
    A complex-valued optimizable constant coefficient for a Hamiltonian term.
    The main function will try to find the optimal value for this constant.

    Attributes
    ----------
    min : float
        The minimum value that the modulus of the coefficient can take.
    max : float
        The maximum value that the modulus of the coefficient can take.
    """

    min: float
    max: float

    def __post_init__(self):
        check_argument(
            self.min < self.max,
            "The maximum must be larger than the minimum.",
            {"min": self.min, "max": self.max},
        )

    def get_pwc(self, graph, gate_duration, name):
        mod = graph.optimization_variable(1, self.min, self.max)[0]
        phase = graph.optimization_variable(1, 0, 2 * np.pi, True, True)[0]
        value = graph.multiply(mod, graph.exp(1j * phase), name=name)
        return graph.constant_pwc(constant=value, duration=gate_duration)


@expose(Namespace.SUPERCONDUCTING)
@dataclass
class RealOptimizableSignal(OptimizableCoefficient):
    """
    A real-valued optimizable time-dependent piecewise-constant coefficient for
    a Hamiltonian term. The main function will try to find the optimal value for
    this signal at each segment.

    Attributes
    ----------
    count : int
        The number of segments in the piecewise-constant signal.
    min : float
        The minimum value that the signal can take at each segment.
    max : float
        The maximum value that the signal can take at each segment.
    """

    count: int
    min: float
    max: float

    def __post_init__(self):
        check_argument(
            self.count > 0, "There must be at least one segment.", {"count": self.count}
        )
        check_argument(
            self.min < self.max,
            "The maximum must be larger than the minimum.",
            {"min": self.min, "max": self.max},
        )

    def get_pwc(self, graph, gate_duration, name):
        values = graph.optimization_variable(self.count, self.min, self.max)
        return graph.pwc_signal(values=values, duration=gate_duration, name=name)


@expose(Namespace.SUPERCONDUCTING)
@dataclass
class ComplexOptimizableSignal(OptimizableCoefficient):
    """
    A complex-valued optimizable time-dependent piecewise-constant coefficient
    for a Hamiltonian term. The main function will try to find the optimal value
    for this signal at each segment.

    Attributes
    ----------
    count : int
        The number of segments in the piecewise-constant signal.
    min : float
        The minimum value that the modulus of the signal can take at each segment.
    max : float
        The maximum value that the modulus of the signal can take at each segment.
    """

    count: int
    min: float
    max: float

    def __post_init__(self):
        check_argument(
            self.count > 0, "There must be at least one segment.", {"count": self.count}
        )
        check_argument(
            self.min < self.max,
            "The maximum must be larger than the minimum.",
            {"min": self.min, "max": self.max},
        )

    def get_pwc(self, graph, gate_duration, name):
        mods = graph.optimization_variable(self.count, self.min, self.max)
        phases = graph.optimization_variable(self.count, 0, 2 * np.pi, True, True)
        return graph.pwc_signal(
            values=mods * graph.exp(1j * phases), duration=gate_duration, name=name
        )


RealCoefficient = Union[
    int, float, np.ndarray, RealOptimizableSignal, RealOptimizableConstant
]
Coefficient = Union[
    RealCoefficient, complex, ComplexOptimizableSignal, ComplexOptimizableConstant
]


def _check_argument_real_coefficient(argument, name):

    if isinstance(argument, (ComplexOptimizableSignal, ComplexOptimizableConstant)):
        check = False
    else:
        check = np.isrealobj(argument)

    check_argument(check, f"The {name} must be a real coefficient.", {name: argument})


@expose(Namespace.SUPERCONDUCTING)
@dataclass
class Transmon:
    r"""
    Class that stores all the physical system data for a transmon.

    Arguments
    ---------
    dimension : int
        Number of dimensions of the Hilbert space of the transmon.
        Must be at least 2.
    anharmonicity : RealCoefficient, optional
        The nonlinearity of the transmon,
        multiplying the term :math:`(b^\dagger)^2 b^2/2` in the Hamiltonian.
        If not provided, it defaults to no anharmonicity term.
    frequency : RealCoefficient, optional
        The frequency of the transmon,
        multiplying the term :math:`b^\dagger b` in the Hamiltonian.
        If not provided, it defaults to no frequency term.
    drive : Coefficient, optional
        The complex drive of the transmon,
        multiplying the term :math:`b^\dagger` in the Hamiltonian.
        If not provided, it defaults to no drive term.

    Notes
    -----
    The Hamiltonian for the transmon is defined as

    .. math::
        H_\mathrm{transmon} =
            \frac{\alpha}{2} (b^\dagger)^2 b^2
            + \omega_T b^\dagger b
            + \frac{1}{2} \left(\gamma_T b^\dagger + H.c. \right)

    where :math:`\alpha` is the transmon nonlinearity,
    :math:`\omega_T` is the transmon frequency,
    :math:`\gamma_T` is the transmon drive,
    and :math:`H.c.` indicates the Hermitian conjugate.
    All coefficients in the Hamiltonian are optional,
    and you should only pass those relevant to your system.
    """

    dimension: int
    anharmonicity: Optional[RealCoefficient] = None
    frequency: Optional[RealCoefficient] = None
    drive: Optional[Coefficient] = None

    def __post_init__(self):
        check_argument_positive_integer(self.dimension, "dimension")
        check_argument(
            self.dimension >= 2,
            "The dimension must be at least 2.",
            {"dimension": self.dimension},
        )
        _check_argument_real_coefficient(self.anharmonicity, "anharmonicity")
        _check_argument_real_coefficient(self.frequency, "frequency")


@expose(Namespace.SUPERCONDUCTING)
@dataclass
class Cavity:
    r"""
    Class that stores all the physical system data for a cavity.

    Arguments
    ---------
    dimension : int
        Number of dimensions of the Hilbert space of the cavity.
        Must be at least 2.
    kerr_coefficient: RealCoefficient, optional
        The nonlinearity of the cavity,
        multiplying the term :math:`(a^\dagger)^2 a^2/2` in the Hamiltonian.
        If not provided, it defaults to no nonlinear term.
    frequency : RealCoefficient, optional
        The frequency of the cavity,
        multiplying the term :math:`a^\dagger a` in the Hamiltonian.
        If not provided, it defaults to no frequency term.
    drive : Coefficient, optional
        The complex drive of the cavity,
        multiplying the term :math:`a^\dagger` in the Hamiltonian.
        If not provided, it defaults to no drive term.

    Notes
    -----
    The Hamiltonian for the cavity is defined as

    .. math::
        H_\mathrm{cavity} =
            \frac{K}{2} (a^\dagger)^2 a^2
            + \omega_C a^\dagger a
            + \frac{1}{2} \left(\gamma_C a^\dagger + H.c. \right)

    where :math:`K` is the Kerr coefficient,
    :math:`\omega_C` is the cavity frequency,
    :math:`\gamma_C` is the cavity drive,
    and :math:`H.c.` indicates the Hermitian conjugate.
    All coefficients in the Hamiltonian are optional,
    and you should only pass those relevant to your system.
    """

    dimension: int
    kerr_coefficient: Optional[RealCoefficient] = None
    frequency: Optional[RealCoefficient] = None
    drive: Optional[Coefficient] = None

    def __post_init__(self):
        check_argument_positive_integer(self.dimension, "dimension")
        check_argument(
            self.dimension >= 2,
            "The dimension must be at least 2.",
            {"dimension": self.dimension},
        )
        _check_argument_real_coefficient(self.kerr_coefficient, "Kerr coefficient")
        _check_argument_real_coefficient(self.frequency, "frequency")


@expose(Namespace.SUPERCONDUCTING)
@dataclass
class TransmonCavityInteraction:
    r"""
    Class that stores all the physical system data for the interaction
    between a transmon and a cavity.

    Arguments
    ---------
    dispersive_shift : RealCoefficient, optional
        The dispersive shift in the system,
        multiplying the term :math:`a^\dagger a b^\dagger b` in the Hamiltonian.
        If not provided, it defaults to no dispersive shift term.
    rabi_coupling : Coefficient, optional
        The strength of the Rabi coupling between the transmon and the cavity,
        multiplying the term :math:`a b^\dagger` in the Hamiltonian.
        If not provided, it defaults to no Rabi coupling term.

    Notes
    -----
    The Hamiltonian for the interaction is defined as

    .. math::
        H_\mathrm{interaction} =
            \chi a^\dagger a b^\dagger b
            + \frac{1}{2} \left(\Omega a b^\dagger + H.c.\right)

    where :math:`\chi` is the dispersive shift,
    :math:`\Omega` is the Rabi coupling between the transmon and the cavity,
    and :math:`H.c.` indicates the Hermitian conjugate.
    All coefficients in the Hamiltonian are optional,
    and you should only pass those relevant to your system.
    """

    dispersive_shift: Optional[RealCoefficient] = None
    rabi_coupling: Optional[Coefficient] = None

    def __post_init__(self):
        _check_argument_real_coefficient(self.dispersive_shift, "dispersive shift")


def _check_real_coefficient(obj):
    if isinstance(obj, (RealOptimizableSignal, RealOptimizableConstant)):
        return True

    if np.isscalar(obj) or isinstance(obj, np.ndarray):
        return np.isrealobj(obj)

    return False


def _create_transmon_and_cavity_hamiltonian(
    graph: Graph,
    transmon: Transmon,
    cavity: Cavity,
    interaction: TransmonCavityInteraction,
    gate_duration: float,
    cutoff_frequency: float,
    sample_count: int,
):
    r"""
    Returns a Pwc node representing a transmon/cavity Hamiltonian
    and a list with the names of the optimizable nodes it contains.

    Parameters
    ----------
    graph : Graph
        The graph where the Hamiltonian will be added.
    transmon : Transmon
        Object containing the physical information about the transmon.
    cavity : Cavity
        Object containing the physical information about the cavity.
    interaction : TransmonCavityInteraction
        Object containing the physical information about the transmon/cavity interaction.
    gate_duration : float
        The duration of the gate.
    cutoff_frequency : float
        The cut-off frequency of a linear sinc filter to be applied to the piecewise-constant
        signals you provide for the coefficients. If None, the signals are not filtered.
    sample_count : int
        The number of segments into which the PWC terms are discretized.

    Returns
    -------
    Pwc
        A node representing the system's Hamiltonian.
    list
        The names of the graph nodes representing optimizable coefficients.
        If some of these are PWC functions and cutoff_frequency is not None,
        then the names of the filtered PWC nodes are also included.
    """

    def convert_to_pwc(coefficient: Coefficient, real_valued: bool, name: str):
        """
        Returns the Pwc representation of a coefficient.
        """

        def filter_signal(signal):
            return graph.discretize_stf(
                stf=graph.convolve_pwc(pwc=signal, kernel=kernel),
                duration=gate_duration,
                segment_count=sample_count,
                name=f"{name}_filtered",
            )

        if real_valued:
            check_argument(
                _check_real_coefficient(coefficient),
                f"{name} can't be complex.",
                {name: coefficient},
            )

        # Convert scalar value into constant Pwc.
        if np.isscalar(coefficient):
            return graph.constant_pwc(
                constant=graph.tensor(coefficient, name=name), duration=gate_duration
            )

        # Convert array into Pwc.
        if isinstance(coefficient, np.ndarray):
            signal = graph.pwc_signal(coefficient, gate_duration, name=name)

            if kernel is None:
                return signal

            return filter_signal(signal)

        # Convert Real/ComplexOptimizableConstant into optimizable constant Pwc.
        if isinstance(
            coefficient, (RealOptimizableConstant, ComplexOptimizableConstant)
        ):
            optimizable_node_names.append(name)
            return coefficient.get_pwc(graph, gate_duration, name)

        # Convert Real/ComplexOptimizableSignal into optimizable Pwc.
        if isinstance(coefficient, (RealOptimizableSignal, ComplexOptimizableSignal)):
            optimizable_node_names.append(name)
            signal = coefficient.get_pwc(graph, gate_duration, name)
            if kernel is None:
                return signal

            optimizable_node_names.append(f"{name}_filtered")
            return filter_signal(signal)

        raise QctrlArgumentsValueError(
            f"{name} has an invalid type.", {name: coefficient}
        )

    check_argument_positive_integer(transmon.dimension, "transmon.dimension")
    check_argument(
        transmon.dimension >= 2,
        "transmon.dimension must be at least 2.",
        {"transmon.dimension": transmon.dimension},
    )
    check_argument_positive_integer(cavity.dimension, "cavity.dimension")
    check_argument(
        cavity.dimension >= 2,
        "cavity.dimension must be at least 2.",
        {"cavity.dimension": transmon.dimension},
    )

    # Define annihilation and creation operators for the transmon and the cavity.
    b = graph.kron(  # pylint: disable=invalid-name
        np.diag(np.sqrt(np.arange(1, transmon.dimension)), k=1),
        np.eye(cavity.dimension),
    )
    a = graph.kron(  # pylint: disable=invalid-name
        np.eye(transmon.dimension),
        np.diag(np.sqrt(np.arange(1, cavity.dimension)), k=1),
    )
    b_T = graph.transpose(b)  # pylint: disable=invalid-name
    a_T = graph.transpose(a)  # pylint: disable=invalid-name

    # Create nested dictionary structure containing information for the different Hamiltonian terms.
    hamiltonian_info = {
        "transmon.anharmonicity": {
            "coefficient": transmon.anharmonicity,
            "operator": 0.5 * b_T @ b_T @ b @ b,
            "is_hermitian": True,
        },
        "transmon.frequency": {
            "coefficient": transmon.frequency,
            "operator": b_T @ b,
            "is_hermitian": True,
        },
        "transmon.drive": {
            "coefficient": transmon.drive,
            "operator": b_T,
            "is_hermitian": False,
        },
        "cavity.frequency": {
            "coefficient": cavity.frequency,
            "operator": a_T @ a,
            "is_hermitian": True,
        },
        "cavity.kerr_coefficient": {
            "coefficient": cavity.kerr_coefficient,
            "operator": 0.5 * a_T @ a_T @ a @ a,
            "is_hermitian": True,
        },
        "cavity.drive": {
            "coefficient": cavity.drive,
            "operator": a_T,
            "is_hermitian": False,
        },
        "interaction.dispersive_shift": {
            "coefficient": interaction.dispersive_shift,
            "operator": b_T @ b @ a_T @ a,
            "is_hermitian": True,
        },
        "interaction.rabi_coupling": {
            "coefficient": interaction.rabi_coupling,
            "operator": b_T @ a,
            "is_hermitian": False,
        },
    }

    check_argument(
        any(info["coefficient"] for info in hamiltonian_info.values()),
        "The system must contain at least one Hamiltonian coefficient.",
        {"transmon": transmon, "cavity": cavity, "interaction": interaction},
    )

    # Create kernel to filter signals.
    if cutoff_frequency is not None:
        kernel = graph.sinc_convolution_kernel(cutoff_frequency)
    else:
        kernel = None

    # Build the Hamiltonian from the different terms.
    hamiltonian_terms = []
    optimizable_node_names = []

    for name, info in hamiltonian_info.items():
        if info["coefficient"] is not None:
            coefficient = convert_to_pwc(
                coefficient=info["coefficient"],
                real_valued=info["is_hermitian"],
                name=name,
            )
            if info["is_hermitian"]:
                hamiltonian_terms.append(coefficient * info["operator"])
            else:
                hamiltonian_terms.append(0.5 * coefficient * info["operator"])
                hamiltonian_terms.append(
                    0.5 * graph.conjugate(coefficient) * graph.adjoint(info["operator"])
                )

    return graph.pwc_sum(hamiltonian_terms), optimizable_node_names


def _sanitize_output(item):
    """
    Converts a non-batched item from a qctrl.types.graph/optimization.Result.output
    dictionary into a NumPy array.

    If the item is a dictionary (corresponds to a tensor), then its "value" is returned.

    If the item is a list of dictionaries (corresponds to a Pwc), then the "value"
    elements of its inner dictionaries are returned in a NumPy array.
    """
    if isinstance(item, dict):
        return item["value"]
    if isinstance(item, list):
        assert all(
            isinstance(elem, dict) for elem in item
        ), "Batches are not supported."
        return np.array([seg["value"] for seg in item])
    assert False, "Unknown output format."


@expose(Namespace.SUPERCONDUCTING)
def simulate_transmon_and_cavity(  # pylint: disable=missing-param-doc
    qctrl: Any,
    transmon: Transmon,
    cavity: Cavity,
    interaction: TransmonCavityInteraction,
    gate_duration: float,
    sample_count: int = 128,
    cutoff_frequency: Optional[float] = None,
    initial_state: Optional[np.ndarray] = None,
):
    r"""
    Simulates a system consisting of a transmon coupled to a cavity.

    Parameters
    ----------
    transmon : Transmon
        Object containing the physical information about the transmon.
        It must not contain any optimizable coefficients.
    cavity : Cavity
        Object containing the physical information about the cavity.
        It must not contain any optimizable coefficients.
    interaction : TransmonCavityInteraction
        Object containing the physical information about the transmon-cavity interaction.
        It must not contain any optimizable coefficients.
    gate_duration : float
        The duration of the gate to be simulated, :math:`t_\mathrm{gate}`.
    sample_count : int, optional
        The number of times between 0 and `gate_duration` (included)
        at which the evolution is sampled.
        Defaults to 128.
    cutoff_frequency : float, optional
        The cut-off frequency of a linear sinc filter to be applied to the piecewise-constant
        signals you provide for the coefficients. If not provided, the signals are not filtered.
        If the signals are filtered, a larger sample count leads to a more accurate numerical
        integration. (If the signals are not filtered, the sample count has no effect on the
        numerical precision of the integration.)
    initial_state : np.ndarray, optional
        The initial state of the system, :math:`|\Psi_\mathrm{initial}\rangle`, as a 1D array of
        length ``D = transmon.dimension * cavity.dimension``.
        If not provided, the function only returns the system's unitary time-evolution operators.

    Returns
    -------
    dict
        A dictionary containing information about the time evolution of the system, with keys

            ``sample_times``
                The times at which the system's evolution is sampled,
                as an array of shape ``(T,)``.
            ``unitaries``
                The system's unitary time-evolution operators at each sample time,
                as an array of shape ``(T, D, D)``.
            ``state_evolution``
                The time evolution of the initial state at each sample time,
                as an array of shape ``(T, D)``.
                This is only returned if you provide an initial state.

    Notes
    -----
    The Hamiltonian of the system is of the form

    .. math::
        H = H_\mathrm{transmon} + H_\mathrm{cavity} + H_\mathrm{interaction}

    where :math:`H_\mathrm{transmon}` and :math:`H_\mathrm{cavity}` are the
    transmon/cavity Hamiltonians and :math:`H_\mathrm{interaction}` their
    interaction. See their respective classes for their definition.
    """

    system_dimension = transmon.dimension * cavity.dimension
    if initial_state is not None:
        check_argument(
            initial_state.shape == (system_dimension,),
            "Initial state must be a 1D array of length transmon.dimension * cavity.dimension",
            {"initial_state": initial_state, "transmon": transmon, "cavity": cavity},
            extras={"transmon.dimension * cavity.dimension": system_dimension},
        )

    # Create graph object.
    graph = qctrl.create_graph()

    # Create PWC Hamiltonian.
    hamiltonian, optimizable_node_names = _create_transmon_and_cavity_hamiltonian(
        graph=graph,
        transmon=transmon,
        cavity=cavity,
        interaction=interaction,
        gate_duration=gate_duration,
        cutoff_frequency=cutoff_frequency,
        sample_count=sample_count,
    )

    # Check whether there are any optimizable coefficients.
    check_argument(
        len(optimizable_node_names) == 0,
        "None of the the Hamiltonian terms can be optimizable.",
        {"transmon": transmon, "cavity": cavity, "interaction": interaction},
    )

    # Calculate the evolution.
    sample_times = np.linspace(
        gate_duration / sample_count, gate_duration, sample_count
    )
    unitaries = graph.time_evolution_operators_pwc(
        hamiltonian=hamiltonian, sample_times=sample_times, name="unitaries"
    )
    output_node_names = ["unitaries"]

    if initial_state is not None:
        states = unitaries @ initial_state[:, None]
        states = states[..., 0]
        states.name = "state_evolution"
        output_node_names.append("state_evolution")

    simulation_result = qctrl.functions.calculate_graph(
        graph=graph, output_node_names=output_node_names
    )

    # Retrieve results and build output dictionary.
    result_dict = {"sample_times": sample_times}

    for key in output_node_names:
        result_dict[key] = _sanitize_output(simulation_result.output[key])

    return result_dict


@expose(Namespace.SUPERCONDUCTING)
def optimize_transmon_and_cavity(  # pylint: disable=missing-param-doc
    qctrl: Any,
    transmon: Transmon,
    cavity: Cavity,
    interaction: TransmonCavityInteraction,
    gate_duration: float,
    initial_state: Optional[np.ndarray] = None,
    target_state: Optional[np.ndarray] = None,
    target_operation: Optional[np.ndarray] = None,
    sample_count: int = 128,
    cutoff_frequency: Optional[float] = None,
    avoid_cavity_top_population: bool = False,
    target_cost: Optional[float] = None,
    optimization_count: int = 5,
):
    r"""
    Finds optimal pulses or parameters for a system consisting of a transmon coupled to a cavity
    to achieve a target state or implement a target operation.

    At least one of the terms in the transmon, cavity, or interaction Hamiltonians
    must be optimizable.

    To optimize a state transfer, you need to provide an initial and a target state.
    To optimize a target gate/unitary, you need to provide a target operation.

    Parameters
    ----------
    transmon : Transmon
        Object containing the physical information about the transmon.
    cavity : Cavity
        Object containing the physical information about the cavity.
    interaction : TransmonCavityInteraction
        Object containing the physical information about the transmon-cavity interaction.
    gate_duration : float
        The duration of the gate to be optimized, :math:`t_\mathrm{gate}`.
    initial_state : np.ndarray, optional
        The initial state of the system, :math:`|\Psi_\mathrm{initial}\rangle`, as a 1D array of
        length ``transmon.dimension * cavity.dimension``.
        If provided, the function also returns its time evolution.  This is a required parameter if
        you pass a `target_state` or set `avoid_cavity_top_population` to True.
    target_state : np.ndarray, optional
        The target state of the optimization, :math:`|\Psi_\mathrm{target}\rangle`,
        as a 1D array of length `D`.
        You must provide exactly one of `target_state` or `target_operation`.
    target_operation : np.ndarray, optional
        The target operation of the optimization, :math:`U_\mathrm{target}`,
        as a 2D array of shape ``(D, D)``.
        You must provide exactly one of `target_state` or `target_operation`.
    sample_count : int, optional
        The number of times between 0 and `gate_duration` (included)
        at which the evolution is sampled.
        Defaults to 128.
    cutoff_frequency: float, optional
        The cut-off frequency of a linear sinc filter to be applied to the piecewise-constant
        signals you provide for the coefficients. If not provided, the signals are not filtered.
        If the signals are filtered, a larger sample count leads to a more accurate numerical
        integration. (If the signals are not filtered, the sample count has no effect on the
        numerical precision of the integration.)
    avoid_cavity_top_population : bool, optional
        Whether to add a term in the cost function to avoid population in the highest simulated
        cavity level during the evolution of the initial state. Note that `sample_count` affects the
        sampling and thus the relative weight of this term (larger sample counts make it more
        relevant, see Notes). If you set this flag to True, you must provide an initial state.
        Defaults to False.
    target_cost : float, optional
        A target value of the cost that you can set as an early stop condition for the optimizer.
        If not provided, the optimizer runs until it converges.
    optimization_count : int, optional
        The number of independent randomly seeded optimizations to perform. The result
        from the best optimization (the one with the lowest cost) is returned.
        Defaults to 5.

    Returns
    -------
    dict
        A dictionary containing the optimized coefficients and information about the time evolution
        of the system, with keys

            ``optimized_values``
                Dictionary with keys such as ``transmon.drive``, ``cavity.frequency``, and
                ``interaction.dispersive_shift`` whose values are the requested optimized
                Hamiltonian coefficients. The values are float/complex for constant coefficients and
                np.ndarray for piecewise-constant signals. If you pass a `cutoff_frequency`, the
                filtered versions of the piecewise-constant coefficients are also included with keys
                such as ``transmon.drive_filtered``.
            ``infidelity``
                The state/operational infidelity of the optimized evolution.
            ``cavity_top_population``
                The value of the cost term with the populations of the highest cavity state.
                (If `avoid_cavity_top_population` is set to True.)
            ``cost``
                The total final optimized cost.
                (This is the same as the infidelity if `avoid_cavity_top_population`
                is not provided.)
            ``sample_times``
                The times at which the system's evolution is sampled,
                as an array of shape ``(T,)``.
            ``unitaries``
                The system's unitary time-evolution operators at each sample time,
                as an array of shape ``(T, D, D)``.
            ``state_evolution``
                The time evolution of the initial state at each sample time,
                as an array of shape ``(T, D)``.
                This is only returned if you provide an initial state.

    Notes
    -----
    The Hamiltonian of the system is of the form

    .. math::
        H = H_\mathrm{transmon} + H_\mathrm{cavity} + H_\mathrm{interaction}

    where :math:`H_\mathrm{transmon}` and :math:`H_\mathrm{cavity}` are the
    transmon/cavity Hamiltonians and :math:`H_\mathrm{interaction}` their
    interaction. See their respective classes for their definition.

    If you provide an `initial_state` and a `target_state`, the optimization cost is defined as the
    infidelity of the state transfer process,

    .. math::
        \mathcal{I}
            = 1 - \left|
                \langle \Psi_\mathrm{target} | U(t_\mathrm{gate}) | \Psi_\mathrm{initial} \rangle
            \right|^2 ,

    where :math:`U(t)` is the unitary time-evolution operator generated by the Hamiltonian.

    If you provide a `target_operation`, the optimization cost is defined as the operational
    infidelity,

    .. math::
        \mathcal{I}
            = 1 - \left| \frac
                {\mathrm{Tr} (U_\mathrm{target}^\dagger U(t_\mathrm{gate}))}
                {\mathrm{Tr} (U_\mathrm{target}^\dagger U_\mathrm{target})}
            \right|^2 .

    If the `avoid_cavity_top_population` flag is set to True, then an additional term is added
    to the cost, penalizing the population of the highest state in the cavity
    (:math:`|N_\mathrm{cavity}\rangle`)

    .. math::
        \mathcal{C} = \mathcal{I}
            + \sum_{n_\mathrm{transmon}} \sum_{i=1}^{N_t}
                |\langle n_\mathrm{transmon}| \langle N_\mathrm{cavity} | U(t_i)
                    | \Psi_\mathrm{initial} \rangle|^2

    where the second sum adds over `sample_count` equally spaced times during the evolution.
    """

    check_argument(
        (target_state is None) ^ (target_operation is None),
        "You have to provide exactly one of `target_state` or `target_operation`.",
        {"target_state": target_state, "target_operation": target_operation},
    )

    system_dimension = transmon.dimension * cavity.dimension

    if initial_state is not None:
        check_argument(
            initial_state.shape == (system_dimension,),
            "Initial state must be a 1D array of length transmon.dimension * cavity.dimension",
            {"initial_state": initial_state, "transmon": transmon, "cavity": cavity},
            extras={"transmon.dimension * cavity.dimension": system_dimension},
        )

    if target_state is not None:
        check_argument(
            initial_state is not None,
            "If you provide a `target_state`, you must provide an `initial_state`.",
            {"target_state": target_state, "initial_state": initial_state},
        )
        check_argument(
            target_state.shape == (system_dimension,),
            "Target state must be a 1D array of length transmon.dimension * cavity.dimension",
            {"target_state": target_state, "transmon": transmon, "cavity": cavity},
            extras={"transmon.dimension * cavity.dimension": system_dimension},
        )

    if target_operation is not None:
        check_argument(
            target_operation.shape == (system_dimension, system_dimension),
            "Target operation must be a square operator of shape "
            "(transmon.dimension * cavity.dimension, transmon.dimension * cavity.dimension).",
            {
                "target_operation": target_operation,
                "transmon": transmon,
                "cavity": cavity,
            },
            extras={"transmon.dimension * cavity.dimension": system_dimension},
        )

    # Create graph object.
    graph = qctrl.create_graph()

    # Create PWC Hamiltonian.
    hamiltonian, optimizable_node_names = _create_transmon_and_cavity_hamiltonian(
        graph=graph,
        transmon=transmon,
        cavity=cavity,
        interaction=interaction,
        gate_duration=gate_duration,
        cutoff_frequency=cutoff_frequency,
        sample_count=sample_count,
    )

    # Check whether there are any optimizable coefficients.
    check_argument(
        len(optimizable_node_names) > 0,
        "At least one of the Hamiltonian terms must be optimizable.",
        {"transmon": transmon, "cavity": cavity, "interaction": interaction},
    )

    other_output_node_names = ["unitaries", "infidelity", "cost"]

    # Calculate the evolution.
    sample_times = np.linspace(
        gate_duration / sample_count, gate_duration, sample_count
    )
    unitaries = graph.time_evolution_operators_pwc(
        hamiltonian=hamiltonian, sample_times=sample_times, name="unitaries"
    )

    if initial_state is not None:
        states = unitaries @ initial_state[:, None]
        states = states[..., 0]
        states.name = "state_evolution"
        other_output_node_names.append("state_evolution")

    # Calculate the infidelity.
    if target_state is not None:
        infidelity = graph.state_infidelity(target_state, states[-1], name="infidelity")
    else:
        infidelity = graph.unitary_infidelity(
            unitaries[-1], target_operation, name="infidelity"
        )

    # Add optional top population term to the cost.
    if not avoid_cavity_top_population:
        graph.add(infidelity, 0.0, name="cost")

    else:
        cavity_top_states = graph.reshape(
            states, [states.shape[0], transmon.dimension, cavity.dimension]
        )[:, :, -1]
        cavity_top_pops = graph.sum(
            graph.abs(cavity_top_states) ** 2, name="cavity_top_population"
        )
        other_output_node_names.append("cavity_top_population")

        graph.add(infidelity, cavity_top_pops, name="cost")

    optimization_result = qctrl.functions.calculate_optimization(
        graph=graph,
        cost_node_name="cost",
        output_node_names=optimizable_node_names + other_output_node_names,
        target_cost=target_cost,
        optimization_count=optimization_count,
    )

    # Retrieve results and build output dictionary.
    result_dict = {
        "optimized_values": {},
        "sample_times": sample_times,
    }

    for key in optimizable_node_names:
        result_dict["optimized_values"][key] = _sanitize_output(
            optimization_result.output[key]
        )

    for key in other_output_node_names:
        result_dict[key] = _sanitize_output(optimization_result.output[key])

    return result_dict
