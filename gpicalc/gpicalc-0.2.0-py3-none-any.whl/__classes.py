from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

class GPICalculator():
    def __init__(self):
        pass
    
    def score(self, data, coefficient):
        self.data = data
        self.coefficient = coefficient
        scaler = MinMaxScaler()
        norm_data = scaler.fit_transform(data)
        median = list()
        for i in range(np.shape(norm_data)[1]):
            median.append(np.median(norm_data[:,i]))
            norm_data[:,i] = coefficient[i] * (median[i] - norm_data[:,i])
        gpi = np.sum(norm_data, axis=1)
        gpi = pd.DataFrame(gpi, index=data.index, columns=['GPI Score'])
        return gpi
    
    
