import numpy as np

class multi():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def run(self):
        return np.dot(self.num1,self.num2)
