""" Qubit class definition """

from math import pi
from typing import TypeVar

QIntType = TypeVar("QIntType", bound="QUInt")
QubitType = TypeVar("QubitType", bound="Qubit")


class Qubit:
  """ A single qubit in a Q(U)Int """

  def __init__(self, quint: QIntType, qubit: int) -> None:
    if qubit >= quint.num_qubits:
      raise Exception("Qubit index out of bounds")

    self.quint = quint
    self.qubit = qubit

  def negate(self) -> QubitType:
    """ Negates the qubit (PauliX Gate)

    Returns:
      The Qubit

    """

    self.quint.negate(self.qubit)
    return self

  def c_negate(self, on: QubitType) -> QubitType:
    """ Controlled negate on another qubit

    Returns:
      The Qubit

    """

    self.quint.c_negate(on=on, qubit=self.qubit)
    return self

  def sqrt_not(self) -> QubitType:
    """ Apply square root of `not`. Applying this twice is a `not` gate

    Returns:
      The Qubit

    """

    self.quint.sqrt_not(self.qubit)
    return self

  def hadamard(self) -> QubitType:
    """ Applies a hadamard gate. Puts the qubit in an exact superposition

    Returns:
      The Qubit

    """

    self.quint.hadamard(self.qubit)
    return self

  def phase(self, angle: float = pi / 2) -> QubitType:
    """ Applies a hadamard gate. Puts the qubit in an exact superposition

    Returns:
      The Qubit

    """

    self.quint.phase(self.qubit, angle)
    return self

  def c_phase(self, *, on: QubitType, angle: float = pi / 2) -> QubitType:
    """ Applies a hadamard gate. Puts the qubit in an exact superposition

    Returns:
      The Qubit

    """

    self.quint.c_phase(on=on, qubit=self.qubit, angle=angle)
    return self

  def swap(self, other: QubitType) -> QubitType:
    """ Swap with a give qubit

    Args:
      other: Qubit to swap with

    Returns:
      The original Qubit method was called on

    """

    self.quint.swap(other.quint, self.qubit, other.qubit)
    return self

  def c_swap(self, other: QubitType, on: QubitType) -> QubitType:
    self.quint.c_swap(other.quint, self.qubit, other.qubit, on=on)
    return self

  def measure(self) -> int:
    return self.quint.measure(self.qubit)

  # Aliases
  h = hadamard
  dburby = hadamard
  entangle = c_negate
