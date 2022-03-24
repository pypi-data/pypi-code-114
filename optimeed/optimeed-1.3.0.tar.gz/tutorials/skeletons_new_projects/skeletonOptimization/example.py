"""This example provides a skeleton structure of a more complex optimization project. Refer to first optimization tutorial for more understanding"""
from .myDevice import MyDevice
from .myObjectives import MyObjective
from .myCharacterization import MyCharacterization

from optimeed.optimize import Optimizer, Real_OptimizationVariable
from optimeed.visualize.displayOptimization import OptimizationDisplayer
from optimeed.visualize import start_qt_mainloop


def run():
    theDevice = MyDevice()

    theCharacterization = MyCharacterization()

    optimizationVariables = list()
    optimizationVariables.append(Real_OptimizationVariable('x', 0, 2))
    optimizationVariables.append(Real_OptimizationVariable('y', 0, 2))

    listOfObjectives = [MyObjective()]
    listOfConstraints = []

    theOptimizer = Optimizer()
    PipeOptimization = theOptimizer.set_optimizer(theDevice, listOfObjectives, listOfConstraints, optimizationVariables,
                                                  theCharacterization=theCharacterization)
    theOptimizer.set_max_opti_time(5)
    optiDisplayer = OptimizationDisplayer(PipeOptimization, listOfObjectives, theOptimizer)
    _, _, _ = optiDisplayer.generate_optimizationGraphs()
    resultsOpti, convergence = optiDisplayer.launch_optimization()

    print("Best individuals :")
    for device in resultsOpti:
        print("x : {} \t y : {}". format(device.x, device.y))

    start_qt_mainloop()
