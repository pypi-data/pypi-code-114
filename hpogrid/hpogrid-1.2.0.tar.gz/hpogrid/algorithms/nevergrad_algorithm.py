from typing import Dict

from hpogrid.search_space import NeverGradSpace

class NeverGradAlgorithm():
    
    kDefaultBudget = 100
    kDefaultMethod = "RandomSearch"
    
    def __init__(self):
        self.algorithm = None

    def create(self, metric:str, mode:str, search_space:Dict, **args):
        search_space = NeverGradSpace(search_space).get_search_space()
        method = args.pop('method', self.kDefaultMethod)
        import nevergrad as ng
        optimizer = ng.optimizers.registry[method](
                parametrization=search_space, budget=self.kDefaultBudget)
        from ray.tune.suggest.nevergrad import NevergradSearch
        self.algorithm = NevergradSearch(optimizer, None, metric=metric, mode=mode, **args)
        return self.algorithm