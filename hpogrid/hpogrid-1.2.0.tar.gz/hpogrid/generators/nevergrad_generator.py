import copy
from typing import List, Dict

from .base_generator import Generator
from hpogrid.search_space.nevergrad_space import NeverGradSpace

class NeverGradGenerator(Generator):
    
    kDefaultBudget = 100
    kDefaultMethod = "RandomSearch"
    
    def get_searcher(self, search_space:Dict, metric:str, mode:str, **args):
        search_space = NeverGradSpace(search_space).get_search_space()
        if ('method' in args) and (args['method']):
            method = args['method']
        else:
            method = self.kDefaultMethod
        import nevergrad as ng
        searcher = ng.optimizers.registry[method](
                parametrization=search_space, budget=self.kDefaultBudget)
        return searcher

    def ask(self, n_points:int = None):
        points = []
        for _ in range(n_points):
            point = self.searcher.ask().kwargs
            points.append(copy.deepcopy(point))
        return points

    def tell(self, point:Dict, value):
        value = self._to_metric_values(value)
        self.searcher.suggest(**point)
        candidate = self.searcher.ask()
        self.searcher.tell(candidate, self.signature * value)
