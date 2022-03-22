from matplotlib import pyplot as plt

err = NotImplementedError("not implemented yet")

class BasePrior(object):
    def __init__(self):
        raise err

    def update(self):
        raise err

    def to_scipy(self):
        raise err

    def sample(self, size=1):
        raise err

    def pdf(self, x):
        raise err

    def cdf(self, x):
        raise err

    def posterior(self, l, u):
        raise err

    def plot(self,lim:tuple = None,
                  ax:plt.axes=None, label="", pp=200, normalize=False):
        raise err

    @staticmethod
    def plot_multiple(**kwargs):
        raise err

    def to_json(self):
        raise err

    @staticmethod
    def from_json(self):
        return err