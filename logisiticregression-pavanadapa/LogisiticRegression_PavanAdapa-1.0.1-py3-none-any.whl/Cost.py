import numpy as np
from LogisticRegression.Sigmoid import sigmoid
def cost(X, y, theta, lambdad):
    # function takes the training data, the parameters 𝜃, 
    # and the regularization parameter λ, then computes and 
    # returns the regularized cost function
    neg_Loglik = 0 # negative loglikelihood function
    m = len(y)
    for i in range(m):
        h_x = sigmoid(np.dot(X[i,:], theta))
        neg_Loglik = neg_Loglik + ((-y[i]*np.log(h_x)) - (1-y[i])*np.log(1-h_x))
    return (neg_Loglik + (lambdad/2)*np.dot(theta, theta))/m