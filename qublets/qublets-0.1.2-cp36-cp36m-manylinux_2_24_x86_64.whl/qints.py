""" QUInt and QInt class definition """

from typing import Optional, Type, TypeVar

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

  @classmethod
  def zeros(cls: Type[QIntType],
            size: int,
            qpu: Optional[QPU] = None) -> QIntType:
    return cls(size, qpu)

  @classmethod
  def ones(cls: Type[QIntType],
           size: int,
           qpu: Optional[QPU] = None) -> QIntType:
    return cls.zeros(size, qpu).negate()

  @classmethod
  def pluses(cls: Type[QIntType],
             size: int,
             qpu: Optional[QPU] = None) -> QIntType:
    return cls.zeros(size, qpu).hadamard()

  @classmethod
  def minuses(cls: Type[QIntType],
              size: int,
              qpu: Optional[QPU] = None) -> QIntType:
    return cls.ones(size, qpu).hadamard()

  @classmethod
  def lefts(cls: Type[QIntType],
            size: int,
            qpu: Optional[QPU] = None) -> QIntType:
    return cls.zeros(size, qpu).sqrt_not().hadamard()

  @classmethod
  def rights(cls: Type[QIntType],
             size: int,
             qpu: Optional[QPU] = None) -> QIntType:
    return cls.ones(size, qpu).sqrt_not().hadamard()

  @classmethod
  def fully_entangled(cls: Type[QIntType],
                      size: int,
                      qpu: Optional[QPU] = None) -> QIntType:
    q = cls.zeros(size, qpu).hadamard(0)

    for i in range(q.num_qubits - 1):
      q.qpu.ApplyCPauliX(q.start_qubit + i, q.start_qubit + i + 1)

    return q

  def negate(self: QIntType, qubit: Optional[int] = None) -> QIntType:
    if qubit is not None:
      self.qpu.ApplyPauliX(self.start_qubit + qubit)
      return self

    for i in range(self.num_qubits):
      self.negate(i)

    return self

  def c_negate(self: QIntType,
               on: QIntType,
               qubit: Optional[int] = None,
               on_qubit: Optional[int] = None) -> QIntType:
    if self.qpu != on.qpu:
      raise Exception("Cannot cross-compute between QPUs!")

    if qubit is not None:
      if on_qubit is None:
        on_qubit = qubit

      self.qpu.ApplyCPauliX(on.start_qubit + on_qubit, self.start_qubit + qubit)
      return

    if self.num_qubits != on.num_qubits:
      raise Exception("Cannot entangle Q(U)Int of different sizes!")

    for i in range(self.num_qubits):
      self.c_negate(on, i)

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
      return

    if self.num_qubits != other.num_qubits:
      raise Exception("Cannot swap Q(U)Int of different sizes!")

    for i in range(self.num_qubits):
      self.swap(other, i)

  def c_swap(self: QIntType,
             other: QIntType,
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
      return

    if self.num_qubits != other.num_qubits:
      raise Exception("Cannot swap Q(U)Int of different sizes!")

    for i in range(self.num_qubits):
      self.c_swap(other, on, i)

  def swap_test(self: QIntType,
                other: QIntType,
                on: Qubit,
                qubit: Optional[int] = None,
                other_qubit: Optional[int] = None) -> QIntType:
    if self.qpu != other.qpu or self.qpu != on.quint.qpu:
      raise Exception("Cannot cross-compute between QPUs!")

    # Trample the ancilla for a swaptest
    self.qpu.CollapseQubit(on.quint.start_qubit + on.qubit, False)
    self.qpu.Normalize()
    self.c_swap(other, on.hadamard(), qubit, other_qubit)
    return on.hadamard().negate().measure()

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


class QInt(QUInt):

  def measure(self: QIntType, qubit: Optional[int] = None) -> int:
    val = super().measure(qubit)
    if qubit is not None:
      return val

    if val < (1 << self.num_qubits - 1):
      return val
    val ^= 2**(self.num_qubits) - 1
    return -(val + 1)
