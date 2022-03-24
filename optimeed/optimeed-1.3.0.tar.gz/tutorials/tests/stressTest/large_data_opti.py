"""This example shows how to start a small optimization problem. Start with these imports: (note: full path is not necessary)"""

from optimeed.core import InterfaceDevice
from optimeed.optimize.optiAlgorithms import MultiObjective_GA as OptimizationAlgorithm
# from optimeed.optimize.optiAlgorithms import NLOpt_Algorithm as OptimizationAlgorithm  # Toggle this line to use NLOpt
from optimeed.optimize import Optimizer, Real_OptimizationVariable, InterfaceObjCons, InterfaceCharacterization
from optimeed.visualize.displayOptimization import OptimizationDisplayer
from optimeed.visualize import start_qt_mainloop
import time
from typing import List


"""User-defined structures"""


class Device(InterfaceDevice):
    """Define the Device to optimize."""
    x: float  # Type hinted -> will be automatically saved
    large_data: List[float]

    def __init__(self):
        self.x = 1
        self.large_data = [1.321309]*1000


class Characterization(InterfaceCharacterization):
    """Define the Characterization scheme. In this case nothing is performed,
     but this is typically where model code will be executed and results saved."""
    def compute(self, thedevice):
        time.sleep(0.005)


class MyObjective1(InterfaceObjCons):
    """First objective function (to be minimized)"""
    def compute(self, theDevice):
        return (1 + theDevice.x**2)**0.5


class MyConstraint(InterfaceObjCons):
    """Constraints, that needs to be <= 0"""
    def compute(self, theDevice):
        return theDevice.x - 0.55


def run():
    """Start the main code. Instantiate previously defined classes."""
    theDevice = Device()
    theCharacterization = Characterization()

    """Variable to be optimized"""
    optimizationVariables = list()
    optimizationVariables.append(Real_OptimizationVariable('x', 0, 2))  #

    """Objective and constraints"""
    listOfObjectives = [MyObjective1()]
    listOfConstraints = [MyConstraint()]

    """Set the optimizer"""
    theOptimizer = Optimizer()
    theAlgo = OptimizationAlgorithm()
    theAlgo.set_optionValue(theAlgo.NUMBER_OF_CORES, 2)
    theAlgo.set_optionValue(theAlgo.OPTI_ALGORITHM, "NSGAII")
    theOptimizer.set_optionValue(theOptimizer.KWARGS_OPTIHISTO, {"optiname": "stressTest", "timer_autosave": 5, "compress_save": True, "memory_efficient": True})
    PipeOptimization = theOptimizer.set_optimizer(theDevice, listOfObjectives, listOfConstraints, optimizationVariables,
                                                  theOptimizationAlgorithm=theAlgo, theCharacterization=theCharacterization)
    theOptimizer.set_max_opti_time(500)

    optiDisplayer = OptimizationDisplayer(PipeOptimization, listOfObjectives, theOptimizer)
    _, _theDatalink, _ = optiDisplayer.generate_optimizationGraphs()
    optiDisplayer.launch_optimization(refresh_time=10)
    optiDisplayer.close_windows()
