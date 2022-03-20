from typing import Dict

from hpogrid.search_space import AxSpace

class AxAlgorithm():
    
    def __init__(self):
        self.algorithm = None
        
    def create(self, metric:str, mode:str, search_space:Dict, **args):
        search_space = AxSpace(search_space).get_search_space()
        
        kwargs = {**args}
        if 'enforce_sequential_optimization' not in kwargs:
            kwargs['enforce_sequential_optimization'] = False
        if 'verbose_logging' not in kwargs:
            kwargs['verbose_logging'] = False

        from ray.tune.suggest.ax import AxSearch
        self.algorithm = AxSearch(search_space, metric=metric, mode=mode, **kwargs)
        return self.algorithm