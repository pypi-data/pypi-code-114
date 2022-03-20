from typing import Dict

from hpogrid.search_space import OptunaSpace

class OptunaAlgorithm():
    
    def __init__(self):
        self.algorithm = None
        
    def create(self, metric:str, mode:str, search_space:Dict, **args):
        search_space = OptunaSpace(search_space).search_space
        from ray.tune.suggest.optuna import OptunaSearch
        self.algorithm = OptunaSearch(space=search_space, mode=mode, metric=metric, **args)
        return self.algorithm