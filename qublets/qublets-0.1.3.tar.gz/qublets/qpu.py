""" QPU class definition """

import cmath
from dataclasses import dataclass
import math
from typing import List

from .iqs import _iqs


@dataclass
class QPUState:
  value: int
  probability: float
  phase: float


@dataclass
class QPUStateCollection:
  states: List[QPUState]

  def __getitem__(self, i):
    return self.states[i]

  def __len__(self):
    return len(self.states)

  def debug_string(self):
    debug_vals = []
    known_phases = {
        5.759586: "11π/6",
        5.497787: "7π/4",
        5.235987: "5π/3",
        4.712388: "3π/2",
        4.188790: "4π/3",
        3.926990: "5π/4",
        3.665191: "7π/6",
        3.141592: "π",
        2.617993: "5π/6",
        2.356194: "3π/4",
        2.094395: "2π/3",
        1.570796: "π/2",
        1.047197: "π/3",
        0.785398: "π/4",
        0.523598: "π/6"
    }
    for state in self.states:
      debug = f"{state.value}: {round(state.probability, 4)*100}%"
      if abs(state.phase) > 0.000001:
        phase = state.phase
        for known_val, known_label in known_phases.items():
          if abs(abs(state.phase) - known_val) < 0.000001:
            phase = known_label
            # TODO(dyordan1): Do we need phase < 0? Some sources use [-pi; pi]
            # instead of [0; 2pi]
            if state.phase * known_val < 0:
              phase = "-" + phase
            break
        debug += f" ({phase})"
      debug_vals.append(debug)
    return "QPU states:\n" + "\n".join(debug_vals) + "\n"


class QPU(_iqs.QubitRegister):
  """ Utility class to represent a QPU that can be split up into Q(U)Ints

  Args:
    num_qubits: How many qubits to allocated to the QPU

  """

  def __init__(self, num_qubits: int) -> None:
    self.num_qubits = num_qubits
    self._next_qubit = 0
    super().__init__(num_qubits, "base", 0, 0)

  def _reserve(self, num_qubits: int):
    if self._next_qubit + num_qubits > self.num_qubits:
      raise Exception(
          "Overcommitted QPU! You tried to reserve more qubits than available!")

    self._next_qubit += num_qubits

  def states(self) -> List[QPUState]:
    self.Normalize()
    states = []
    for i in range(self.GlobalSize()):
      amplitude = self.GetGlobalAmplitude(i)
      magnitude = abs(amplitude)
      states.append(
          QPUState(value=i,
                   probability=magnitude * magnitude,
                   phase=cmath.phase(amplitude)))
    state_collection = QPUStateCollection(
        states=list(filter(lambda s: s.probability != 0, states)))
    return state_collection
