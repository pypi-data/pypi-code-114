import numpy as np
from metricspaces import MetricSpace
from metricspaces import NumpyPoint


class MDS:
    """
    A class for structuring data associated with Multi-Dimensional Scaling.
    """

    def __init__(self, M, target_dimension = None):
        """
        Initialize an empty MDS object for a given metric space M.
        """
        self.M = M
        n = len(M)
        if target_dimension is None:
            target_dimension = n-1
        self.target_dimension = target_dimension

        # The matrix of squared distances
        D = np.array([[self.M.distsq(a,b) for a in self.M] for b in self.M])

        # B is the approximate covariance matrix.
        J = np.ones((n,n))
        I = np.identity(n)
        L = (I - J/n)
        B = (-0.5) * L @ D @ L

        # Compute the SVD
        U, Sigma, VT = np.linalg.svd(B)
        # Take the most significant directions (rescaled).
        self.Q = (U @ np.diag(Sigma ** (1/2)))[:,:target_dimension]
        # The Pseudoinverse of Q.
        self.Q_dagger = (U @ np.diag((1/Sigma) ** (1/2)))
        # Squared norms.
        self.squared_norms = np.array([np.dot(self.Q[i], self.Q[i])
                                                for i in range(n)])

    def inverseSigma(self):
        return np.diag([(0 if s < 1e-8 else 1/s) for s in self.Sigma])

    def coordinates(self, target_dimension = False):
        if target_dimension is False:
            target_dimension = self.target_dimension
        return self.Q[:target_dimension]

    def metricspace(self, target_dimension = False):
        n = len(self.M)
        return MetricSpace([NumpyPoint(self.Q[i]) for i in range(n)])

    def project(self, point):
        s = self.squared_norms
        d = self.target_dimension
        delta = [self.M.distsq(point, q) for q in self.M]
        return (-1/2 * Q_dagger @ (delta - s).T)[:d]
