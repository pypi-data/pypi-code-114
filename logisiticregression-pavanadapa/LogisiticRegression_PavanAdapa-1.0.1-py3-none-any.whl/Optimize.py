import numpy as np
from LogisticRegression.Sigmoid import sigmoid
from LogisticRegression.Cost import cost

def optimize(X, y, lambdad, maxrun, alpha):
  m, n = X.shape
  X = np.hstack((X,np.ones((m, 1))))
  theta = np.random.rand(n+1, 1)
  theta = np.concatenate((np.random.rand(n + 1, 1)))
  costs = []
  for iter in range(0,maxrun):
        first_dev = np.zeros(n+1)
        for i in range(m):
            h_x = sigmoid(np.dot(X[i,:], theta))
            first_dev = first_dev + (h_x - y[i])*X[i,:]
        first_dev[1:] = first_dev[1:] + lambdad * theta[1:]
        first_dev = (alpha/m) * first_dev
        theta_new = theta - first_dev
        diff = theta_new - theta              
        theta = theta_new
        costs.append(cost(X, y, theta, lambdad))
        if np.dot(diff, diff) < 10**(-6):
            break
        if iter == maxrun - 1:
            print("Failed to converge!")
  return theta, costs