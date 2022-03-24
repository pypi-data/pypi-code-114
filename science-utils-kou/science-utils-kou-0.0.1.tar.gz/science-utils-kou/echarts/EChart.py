
from abc import abstractclassmethod, abstractmethod


class EChart(object):
    def __init__(self, global_args, options=None):
        self.global_args = global_args
    
    def get_global_args(self):
        return self.global_args
    
    def set_global_args(self):
        pass
    def output(type):
        pass
