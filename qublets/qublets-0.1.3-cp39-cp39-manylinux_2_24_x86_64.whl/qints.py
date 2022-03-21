""" QUInt and QInt class definition """

from math import pi
from typing import Literal, Optional, Type, TypeVar

from .qpu import QPU
from .qubit import Qubit
from .rng import _rng

QIntType = TypeVar("QIntType", bound="QUInt")


class QUInt:

  def __init__(self: QIntType,
               num_qubits: int,
               qpu: Optional[QPU] = None) -> None:
    self.num_qubits = num_qubits

    if qpu is None:
      qpu = QPU(num_qubits)
    self.qpu = qpu
    self.start_qubit = qpu._next_qubit
    self.qpu._reserve(num_qubits)

  def __getitem__(self, qubit: int) -> Qubit:
    return Qubit(self, qubit)

  def __setitem__(self, qubit: int, value: Literal[1, 0]) -> None:
    # TODO(dyordan1): Is this really the most reliable way to "force" a qubit?
    if value != 1 and value != 0:
      raise Exception("Can only set qubits to 0 or 1")

    # sanity check if we can set this bit
    probability = self.qpu.GetProbability(self.start_qubit + qubit)
    if (probability == 0 and value == 1) or (probability == 1 and value == 0):
      if not self.qpu.IsClassicalBit(self.start_qubit + qubit, 1.e-13):
        raise Exception("Cannot set entangled qubit")

      # Invert gate if incompatible *and* classical
      self.qpu.ApplyPauliX(self.start_qubit + qubit)

    self.qpu.CollapseQubit(self.start_qubit + qubit, bool(value))
    self.qpu.Normalize()

  @classmethod
  def zeros(cls: Type[QIntType],
            size: int,
            *,
            qpu: Optional[QPU] = None) -> QIntType:
    return cls(size, qpu=qpu)

  @classmethod
  def ones(cls: Type[QIntType],
           size: int,
           *,
           qpu: Optional[QPU] = None) -> QIntType:
    return cls.zeros(size, qpu=qpu).negate()

  @classmethod
  def pluses(cls: Type[QIntType],
             size: int,
             *,
             qpu: Optional[QPU] = None) -> QIntType:
    return cls.zeros(size, qpu=qpu).hadamard()

  @classmethod
  def minuses(cls: Type[QIntType],
              size: int,
              *,
              qpu: Optional[QPU] = None) -> QIntType:
    return cls.ones(size, qpu=qpu).hadamard()

  @classmethod
  def lefts(cls: Type[QIntType],
            size: int,
            *,
            qpu: Optional[QPU] = None) -> QIntType:
    return cls.zeros(size, qpu=qpu).sqrt_not().hadamard()

  @classmethod
  def rights(cls: Type[QIntType],
             size: int,
             *,
             qpu: Optional[QPU] = None) -> QIntType:
    return cls.ones(size, qpu=qpu).sqrt_not().hadamard()

  @classmethod
  def fully_entangled(cls: Type[QIntType],
                      size: int,
                      *,
                      qpu: Optional[QPU] = None) -> QIntType:
    q = cls.zeros(size, qpu=qpu).hadamard(0)

    for i in range(q.num_qubits - 1):
      q.qpu.ApplyCPauliX(q.start_qubit + i, q.start_qubit + i + 1)

    return q

  @classmethod
  def value(cls: Type[QIntType],
            size: int,
            value: int,
            *,
            qpu: Optional[QPU] = None) -> QIntType:
    return cls.zeros(size, qpu=qpu).set(value)

  def negate(self: QIntType, qubit: Optional[int] = None) -> QIntType:
    if qubit is not None:
      self.qpu.ApplyPauliX(self.start_qubit + qubit)
      return self

    for i in range(self.num_qubits):
      self.negate(i)

    return self

  def c_negate(self: QIntType,
               *,
               on: Qubit,
               qubit: Optional[int] = None) -> QIntType:
    if self.qpu != on.quint.qpu:
      raise Exception("Cannot cross-compute between QPUs!")

    if qubit is not None:
      self.qpu.ApplyCPauliX(on.quint.start_qubit + on.qubit,
                            self.start_qubit + qubit)
      return self

    for i in range(self.num_qubits):
      self.c_negate(on=on, qubit=i)

    return self

  def sqrt_not(self: QIntType, qubit: Optional[int] = None) -> QIntType:
    if qubit is not None:
      self.qpu.ApplyPauliSqrtX(self.start_qubit + qubit)
      return self

    for i in range(self.num_qubits):
      self.sqrt_not(i)

    return self

  def hadamard(self: QIntType, qubit: Optional[int] = None) -> QIntType:
    if qubit is not None:
      self.qpu.ApplyHadamard(self.start_qubit + qubit)
      return self

    for i in range(self.num_qubits):
      self.hadamard(i)

    return self

  def phase(self: QIntType,
            *,
            qubit: Optional[int] = None,
            angle: float = -pi / 2) -> QIntType:
    if qubit is not None:
      self.qpu.ApplyRotationZ(self.start_qubit + qubit, angle)
      return self

    for i in range(self.num_qubits):
      self.phase(qubit=i, angle=angle)

    return self

  def c_phase(self: QIntType,
              *,
              on: Qubit,
              qubit: Optional[int] = None,
              angle: float = -pi / 2) -> QIntType:
    if self.qpu != on.quint.qpu:
      raise Exception("Cannot cross-compute between QPUs!")

    if qubit is not None:
      self.qpu.ApplyCRotationZ(on.quint.start_qubit + on.qubit,
                               self.start_qubit + qubit, angle)
      return self

    for i in range(self.num_qubits):
      self.c_phase(on=on, qubit=i, angle=angle)

    return self

  def swap(self: QIntType,
           other: QIntType,
           qubit: Optional[int] = None,
           other_qubit: Optional[int] = None) -> QIntType:
    if self.qpu != other.qpu:
      raise Exception("Cannot cross-compute between QPUs!")

    if qubit is not None:
      if other_qubit is None:
        other_qubit = qubit

      self.qpu.ApplySwap(self.start_qubit + qubit,
                         other.start_qubit + other_qubit)
      return self

    if self.num_qubits != other.num_qubits:
      raise Exception("Cannot swap Q(U)Int of different sizes!")

    for i in range(self.num_qubits):
      self.swap(other, i)

    return self

  def c_swap(self: QIntType,
             other: QIntType,
             *,
             on: Qubit,
             qubit: Optional[int] = None,
             other_qubit: Optional[int] = None) -> QIntType:
    if self.qpu != other.qpu or self.qpu != on.quint.qpu:
      raise Exception("Cannot cross-compute between QPUs!")

    if qubit is not None:
      if other_qubit is None:
        other_qubit = qubit

      self.qpu.ApplyToffoli(on.quint.start_qubit + on.qubit,
                            self.start_qubit + qubit,
                            other.start_qubit + other_qubit)
      self.qpu.ApplyToffoli(on.quint.start_qubit + on.qubit,
                            other.start_qubit + other_qubit,
                            self.start_qubit + qubit)
      self.qpu.ApplyToffoli(on.quint.start_qubit + on.qubit,
                            self.start_qubit + qubit,
                            other.start_qubit + other_qubit)
      return self

    if self.num_qubits != other.num_qubits:
      raise Exception("Cannot swap Q(U)Int of different sizes!")

    for i in range(self.num_qubits):
      self.c_swap(other, on=on, qubit=i)

    return self

  def swap_test(self: QIntType,
                other: QIntType,
                *,
                on: Qubit,
                qubit: Optional[int] = None,
                other_qubit: Optional[int] = None) -> QIntType:
    if self.qpu != other.qpu or self.qpu != on.quint.qpu:
      raise Exception("Cannot cross-compute between QPUs!")

    # Trample the ancilla for a swaptest
    on.quint[on.qubit] = 0
    self.c_swap(other, on=on.hadamard(), qubit=qubit, other_qubit=other_qubit)
    return on.hadamard().negate().measure()

  def set(self, value: int) -> QIntType:
    if value < 0 or value > 2**self.num_qubits:
      raise Exception(f"Value to set for QUInt out of bounds: {value}")
    mask = 1
    for i in range(self.num_qubits):
      self[i] = 1 if value & mask else 0
      mask <<= 1

    return self

  def measure(self: QIntType, qubit: Optional[int] = None) -> int:
    if qubit is not None:
      probability = self.qpu.GetProbability(self.start_qubit + qubit)
      r = _rng.GetUniformRandomNumbers(1, 0., 1., "pool")[0]
      if r < probability:
        self.qpu.CollapseQubit(self.start_qubit + qubit, True)
        self.qpu.Normalize()
        return 1

      self.qpu.CollapseQubit(self.start_qubit + qubit, False)
      self.qpu.Normalize()
      return 0

    val = 0
    for i in range(self.num_qubits - 1, -1, -1):
      val <<= 1
      val |= self.measure(i)

    return val

  # Aliases
  h = hadamard
  dburby = hadamard
  entangle = c_negate


class QInt(QUInt):

  def measure(self: QIntType, qubit: Optional[int] = None) -> int:
    val = super().measure(qubit)
    if qubit is not None:
      return val

    if val < (1 << self.num_qubits - 1):
      return val
    val ^= 2**(self.num_qubits) - 1
    return -(val + 1)

  def set(self, value: int) -> QIntType:
    if value < -(1 << self.num_qubits - 1) or value >= (
        1 << self.num_qubits - 1):
      raise Exception(f"Value to set for QInt out of bounds: {value}")

    if value < 0:
      value ^= 2**(self.num_qubits) - 1
      value = -(value + 1)

    return super().set(value)
