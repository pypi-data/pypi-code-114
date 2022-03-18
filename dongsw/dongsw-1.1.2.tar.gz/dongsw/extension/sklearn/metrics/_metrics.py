from sklearn.metrics import mean_squared_error
import numpy as np

def root_mean_squared_error_(y_true, y_pred, *args, **kwargs):

    return np.sqrt(mean_squared_error(y_true, y_pred, *args, *kwargs))