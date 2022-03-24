from optimeed.core import InterfaceDevice
from optimeed.optimize.optiAlgorithms import MultiObjective_GA as OptimizationAlgorithm
# from optimeed.optimize.optiAlgorithms import NLOpt_Algorithm as OptimizationAlgorithm  # Toggle this line to use NLOpt
from optimeed.optimize import Optimizer, Real_OptimizationVariable, InterfaceObjCons, InterfaceCharacterization
from optimeed.visualize.displayOptimization import OptimizationDisplayer
from optimeed.visualize import start_qt_mainloop, stop_qt_mainloop
import threading
import time
import gc
from typing import List


class Device(InterfaceDevice):
    x: float
    y: float
    large_data: List[float]

    def __init__(self):
        self.x = 1
        self.y = 1
        self.large_data = [1.321309]*10000


class Characterization(InterfaceCharacterization):
    def compute(self, thedevice):
        pass


class MyObjective1(InterfaceObjCons):
    def compute(self, theDevice):
        return (1 + (theDevice.y+3)*theDevice.x**2)**0.5


class MyObjective2(InterfaceObjCons):
    def compute(self, theDevice):
        return 4 + 2*(theDevice.y+3)**0.5*(1+(theDevice.x-1)**2)**0.5


class MyConstraint(InterfaceObjCons):
    def compute(self, theDevice):
        return theDevice.x - 0.55


def myOpti():
    theDevice = Device()
    theAlgo = OptimizationAlgorithm()
    theAlgo.set_optionValue(theAlgo.NUMBER_OF_CORES, 4)  # Toggle this line to use more cores. Default is 1 (single core)

    theCharacterization = Characterization()

    optimizationVariables = list()
    optimizationVariables.append(Real_OptimizationVariable('x', 0, 2))  #
    optimizationVariables.append(Real_OptimizationVariable('y', 0, 2))

    listOfObjectives = [MyObjective1(), MyObjective2()]
    listOfConstraints = [MyConstraint()]

    theOptimizer = Optimizer()
    theOptimizer.set_optionValue(theOptimizer.KWARGS_OPTIHISTO, {"autosave": True})
    PipeOptimization = theOptimizer.set_optimizer(theDevice, listOfObjectives, listOfConstraints, optimizationVariables, theOptimizationAlgorithm=theAlgo, theCharacterization=theCharacterization)
    theOptimizer.set_max_opti_time(0.5)

    """Start the optimization"""
    display_opti = True
    if display_opti:  # Display real-time graphs
        optiDisplayer = OptimizationDisplayer(PipeOptimization, listOfObjectives, theOptimizer)
        _, _, _ = optiDisplayer.generate_optimizationGraphs()
        _, _ = optiDisplayer.launch_optimization()
    else:  # Just focus on results
        _, _ = theOptimizer.run_optimization()

    if display_opti:
        timer_autorefresh = threading.Timer(0.5, lambda: stop_qt_mainloop())
        timer_autorefresh.start()
        start_qt_mainloop()  # To keep windows alive
        optiDisplayer.close_windows()


def run():
    for i in range(1000):
        myOpti()
        gc.collect()  # Fix stability upon display ...
        print("Number of threads actives: ", threading.active_count())


if __name__ == "__main__":
    run()
