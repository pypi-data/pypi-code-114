from typing import Dict

from hpogrid.search_space import BOHBSpace

class BOHBAlgorithm():
    
    def __init__(self):
        self.algorithm = None
        
    def create(self, metric:str, mode:str, search_space:Dict, **args):
        search_space = BOHBSpace(search_space).search_space
        from ray.tune.suggest.bohb import TuneBOHB
        self.algorithm = TuneBOHB(search_space, metric=metric, mode=mode, **args)
        return self.algorithm
