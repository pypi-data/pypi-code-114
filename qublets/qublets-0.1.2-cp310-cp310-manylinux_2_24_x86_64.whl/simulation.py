""" Simulation class definition """

import time
from typing import Callable, List, Tuple


class Simulation:
  """ Utility class for running simulations in batches

  Args:
    num_shots: How many times to run a simulation for
    function: The simulation function to run

  Attributes:
    last_results: The results (distribution) for the most-recently-ran batch
    function: The elapsed time (ms) for the most-recently-ran batch

  """

  def __init__(self, num_shots: int, function: Callable[[], int]) -> None:
    self.num_shots = num_shots
    self.function = function
    self.last_results = None
    self.last_time = None

  def run(self) -> List[Tuple[int, int]]:
    """ Run the simulation, returning the distribution of results

    Returns:
      A sorted tuple reprenting a histogram of values returned by the
      simulation function

    """

    start = time.time()
    results = {}
    for _ in range(self.num_shots):
      result = self.function()
      results.setdefault(result, 0)
      results[result] += 1

    self.last_results = sorted(results.items(), key=lambda x: x[0])
    self.last_time = round((time.time() - start) * 1000, 2)

    return self.last_results
