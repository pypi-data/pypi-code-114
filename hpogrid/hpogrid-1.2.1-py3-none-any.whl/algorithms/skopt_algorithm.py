from typing import Dict

from hpogrid.search_space import SkOptSpace

class SkOptAlgorithm():
    
    def __init__(self):
        self.algorithm = None
        
    def create(self, metric:str, mode:str, search_space:Dict, **args):
        search_space = SkOptSpace(search_space).search_space
        from skopt import Optimizer
        optimizer = Optimizer(search_space)
        labels = [hp.name for hp in search_space]
        from ray.tune.suggest.skopt import SkOptSearch
        self.algorithm = SkOptSearch(optimizer, labels, metric=metric, mode=mode, **args)
        return self.algorithm