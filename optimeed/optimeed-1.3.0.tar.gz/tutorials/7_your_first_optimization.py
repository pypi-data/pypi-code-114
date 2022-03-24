"""Now that you know everything about data and visualization, let's get started with optimization!
Optimeed provides high-level interface to perform optimization with visualization and data storage.
The Wiki gives more details about the optimization. To get started, you need the following key ingredients:

    - A device that contains the variables to be optimized ("Device") and other parameters you would like to save
    - A list of optimization variables ("OptimizationVariable")
    - An evaluation function ("Characterization")
    - One or more objective functions ("Objectives")
    - (optional) Eventual constraints ("Constraints")
    - An optimization algorithm ("Optimization Algorithm")
    - Something that will fill the "Device" object with the optimization variables coming from the optimization algorithm. ("MathsToPhysics")
        Don't get scared with this one, if you do not know how it can be useful, the proposition by default works perfectly fine.
    - Something that will link all the blocks together ("Optimizer")
"""

# These are what we need for the optimization
from optimeed.core import InterfaceDevice
from optimeed.optimize.optiAlgorithms import MultiObjective_GA as OptimizationAlgorithm
from optimeed.optimize import Optimizer, Real_OptimizationVariable, InterfaceObjCons, InterfaceCharacterization

# These are the high-level visualization tools optimeed provides ;)
from optimeed.visualize.displayOptimization import OptimizationDisplayer
from optimeed.visualize import on_graph_click_showInfo
from optimeed.visualize import start_qt_mainloop
import time


class Device(InterfaceDevice):
    """Define the Device to optimize."""
    x: float  # Type hinted -> will be automatically saved
    y: float  # Type hinted -> will be automatically saved

    def __init__(self):
        self.x = 1
        self.y = 1


class Characterization(InterfaceCharacterization):
    """Define the Characterization scheme. In this case nothing is performed,
     but this is typically where model code will be executed and results saved inside 'theDevice'."""
    def compute(self, thedevice):
        time.sleep(0.0001)


class MyObjective1(InterfaceObjCons):
    """First objective function (to be minimized)"""
    def compute(self, thedevice):
        return (1 + (thedevice.y+3)*thedevice.x**2)**0.5


class MyObjective2(InterfaceObjCons):
    """Second objective function (to be minimized)"""
    def compute(self, thedevice):
        return 4 + 2*(thedevice.y+3)**0.5*(1+(thedevice.x-1)**2)**0.5


class MyConstraint(InterfaceObjCons):
    """Constraints, that needs to be <= 0"""
    def compute(self, thedevice):
        return thedevice.x - 0.55


if __name__ == "__main__":  # What ??? what is this new line ?? It is actually necessary if you use windows, so that the optimizer can properly spawn the threads.
    """Start the main code. Instantiate previously defined classes."""
    theDevice = Device()
    theAlgo = OptimizationAlgorithm()
    theAlgo.set_optionValue(theAlgo.OPTI_ALGORITHM, "NSGAII")  # You can change the algorithm if you need ;)
    # theAlgo.set_optionValue(theAlgo.NUMBER_OF_CORES, 2)  # Toggle this line to use more cores. Default is 1 (single core).
    # Careful that it generates overhead -> only helpful when the characterization is computationnally expensive.

    theCharacterization = Characterization()

    """Variable to be optimized"""
    optimizationVariables = list()
    optimizationVariables.append(Real_OptimizationVariable('x', 0, 2))  #
    optimizationVariables.append(Real_OptimizationVariable('y', 0, 2))

    """Objective and constraints"""
    listOfObjectives = [MyObjective1(), MyObjective2()]
    listOfConstraints = [MyConstraint()]

    """Set the optimizer"""
    theOptimizer = Optimizer()
    theOptimizer.set_optionValue(theOptimizer.KWARGS_OPTIHISTO, {"autosave": True, 'timer_autosave': 2})  # This line indicates the results will be automatically saved, each 5 minutes
    PipeOptimization = theOptimizer.set_optimizer(theDevice, listOfObjectives, listOfConstraints, optimizationVariables, theOptimizationAlgorithm=theAlgo, theCharacterization=theCharacterization)
    theOptimizer.set_max_opti_time(10)  # That's the stopping criterion ...
    # It is always tricky to find a good one, so that time-based is not bad.
    # In practice, for very long optimizations, I check them regularly and I stop them manually when they seem to have converged (=stagnating objectives 'for a while').
    # Because the results are periodically saved, I am not stressed about brutally stopping the optimization ;)

    """Start the optimization"""
    display_opti = True
    if display_opti:  # Display real-time graphs
        optiDisplayer = OptimizationDisplayer(PipeOptimization, listOfObjectives, theOptimizer, light_background=False)
        _, theDataLink, _ = optiDisplayer.generate_optimizationGraphs()

        # Here we set the actions on click.
        # Yup, on top of generating live graphs, you can also interact with them!! :D
        theActionsOnClick = list()
        theActionsOnClick.append(on_graph_click_showInfo(theDataLink))
        optiDisplayer.set_actionsOnClick(theActionsOnClick)

        resultsOpti, convergence = optiDisplayer.launch_optimization(refresh_time=0.1, max_nb_points_convergence=None)  # Refresh the graphs each 0.1s
    else:  # Otherwise just focus on results ... That can be helpful if you are confident the optimizations will converge and you need to launch several optimizations.
        resultsOpti, convergence = theOptimizer.run_optimization()

    """Gather results"""
    # Pro hint: you would probably never work with these next few lines of code, instead you would move to the next tutorial
    # to retrieve the results from the automatically saved files.
    print("Best individuals :")
    for device in resultsOpti:
        print("x : {} \t y : {}". format(device.x, device.y))

    if display_opti:
        start_qt_mainloop()  # To keep windows alive

    """Note that the results are automatically saved if KWARGS_OPTIHISTO autosaved=True.
    In this case, optimization folder is automatically generated in Workspace/optiX. It contains five files:
    -> autosaved: contains all the devices evaluated during the optimization
    -> logopti: contains all the information relating to the optimization itself: objectives, constraints, evaluation time.
    -> opticonvergence: contains all the information relative to the convergence of the optimization (saved only at the end)
    -> results: all the best devices as decided by the optimization algorithm
    -> summary.html: a summary of the optimization problem
    See other tutorials on how to save/load these information.
    """
