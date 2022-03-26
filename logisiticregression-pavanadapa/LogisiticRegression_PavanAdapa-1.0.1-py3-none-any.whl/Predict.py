import numpy as np
from LogisticRegression.Sigmoid import sigmoid

def predict(X, theta):
  m, n = X.shape
  X = np.hstack((X,np.ones((m, 1))))
  y_results = []
  for i in range(0, len(X)):
    if sigmoid(np.dot(X[i,:], theta)) >= 0.5:
      y_results.append(1)
    else:
      y_results.append(0)
  return y_results
