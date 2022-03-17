from abc import abstractmethod

from .abstract_problem import AbstractProblem


class TimeDependentProblem(AbstractProblem):

    @property
    @abstractmethod
    def temporal_variable(self):
        pass
