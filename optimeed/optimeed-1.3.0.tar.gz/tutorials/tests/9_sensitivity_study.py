from optimeed.visualize import plot
from optimeed.core import Performance_ListDataStruct
from optimeed.optimize import MathsToPhysics, InterfaceCharacterization, Real_OptimizationVariable
from optimeed.consolidate import get_sensitivity_problem, evaluate_sensitivities, SensitivityParameters
from SALib.sample import saltelli
from optimeed.core import SingleObjectSaveLoad


class Foo:
    x: float
    y: float
    res: float

    def __init__(self):
        self.x = 3
        self.y = 4
        self.res = 0


class Char(InterfaceCharacterization):
    def compute(self, theDevice):
        x = theDevice.x
        y = theDevice.y
        theDevice.res = x**2 + y**2 + x*y


if __name__ == "__main__":
    analysis = 1
    if analysis == 0:

        listOfOptimizationVariables = [Real_OptimizationVariable("x", 0, 10), Real_OptimizationVariable("y", 5, 7)]
        problem = get_sensitivity_problem(listOfOptimizationVariables)
        M2P = MathsToPhysics()
        theCharacterization = Char()
        foo = Foo()

        param_values = saltelli.sample(problem, 8)

        theSensitivityParameters = SensitivityParameters(param_values, listOfOptimizationVariables, foo, M2P, theCharacterization)
        #
        # evaluate_sensitivities(theSensitivityParameters, 2, "test_sensitivity")

        SingleObjectSaveLoad.save(theSensitivityParameters, "Test")
        theSensitivityParameters = SingleObjectSaveLoad.load("Test")
        # print(theSensitivityParameters.list_of_optimization_variables)
        evaluate_sensitivities(theSensitivityParameters, 2, "test_sensitivity")

    else:
        results = Performance_ListDataStruct.load("Workspace/test_sensitivity/sensitivity.json")
        datas = results.get_list_attributes("index")
        xs = results.get_list_attributes("device.x")
        ys = results.get_list_attributes("device.y")
        res = results.get_list_attributes("device.res")
        normally_results = [ xs[index]**2 + ys[index]**2 + xs[index]*ys[index] for index in range(len(xs))]
        plot([], res, hold=False)
        plot([], normally_results, hold=True)
