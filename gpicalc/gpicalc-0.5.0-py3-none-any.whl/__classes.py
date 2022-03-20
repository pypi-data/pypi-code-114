from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

class GPICalculator():
    def __init__(self):
        pass
    
    def score(self, data, coefficient):
        self.data = data
        self.coefficient = coefficient
        self.scaler = MinMaxScaler()
        self.norm_data = self.scaler.fit_transform(self.data)
        self.median = list()
        for i in range(np.shape(self.norm_data)[1]):
            self.median.append(np.median(self.norm_data[:,i]))
            self.norm_data[:,i] = self.coefficient[i] * (self.median[i] - self.norm_data[:,i])
        self.gpi = np.sum(self.norm_data, axis=1)
        self.gpi = pd.DataFrame(self.gpi, index=data.index, columns=['GPI Score'])
        return self.gpi
    
    
