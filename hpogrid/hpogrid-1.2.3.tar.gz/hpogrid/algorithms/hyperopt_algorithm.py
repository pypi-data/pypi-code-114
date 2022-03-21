from typing import Dict

from hpogrid.search_space import HyperOptSpace

class HyperOptAlgorithm():
    
    def __init__(self):
        self.algorithm = None
        
    def create(self, metric:str, mode:str, search_space:Dict, **args):
        search_space = HyperOptSpace(search_space).search_space
        from ray.tune.suggest.hyperopt import HyperOptSearch
        self.algorithm = HyperOptSearch(
            search_space,
            metric=metric,
            mode=mode, **args)
        return self.algorithm