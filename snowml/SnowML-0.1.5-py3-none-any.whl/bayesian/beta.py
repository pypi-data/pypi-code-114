import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

from .base import BasePrior

class Beta(BasePrior):
    def __init__(self, alpha=1, beta=None, n=0, **kwargs):
        """
        Args:
            alpha (int, optional): alpha of the beta distribution. Defaults to 1.
            beta ([type], optional): beta of the beta distribution. equals to n-alpha+1 when None. Defaults to None.
            n (int, optional): the number of trials. Defaults to 0.
        """ 
        if beta is None:
            if n > 0:
                beta = n - alpha + 1
            else:
                beta = 1
        
        self.alpha = alpha
        self.beta = beta
        self.n = n


    def update(self, successes: int = None, trials: int = None, data=None):  
        """
        Update the alpha (sucesses) and n (trials) for a given input.
        If data array is provided, all other given arguments are ignored.

        Args:
            successes (int, optional): number of sucesses in set of trials. Defaults to None.
            trials (int, optional): the nuber of trials. Defaults to None.
            data (iterable, optional):  array where each element is either 1 or 0 indicating sucessful or unsucessful action. Defaults to None.

        Return:
            Beta object with updated distribution.
        """

        if data is not None:
            successes = np.sum(data)
            trials = len(data)

        if successes is None or trials is None:
            raise ValueError("must provied data array or sucesses AND trails.")

        alpha = self.alpha + successes
        n = self.n + trials

        return Beta(alpha= alpha, n=n)

    def to_scipy(self):
        """
        Returns current beta distribution as scipy.stats.beta instance.
        """
        return stats.beta(a=self.alpha, b=self.beta)

    def sample(self, size=1):
        """
        Draw samples from the beta distribution.

        Args:
            size (int, defaults=1): the number of samples to draw.

        Returns:
            np.array of given size with random samples from the distribution. 
        """
        return np.random.beta(self.alpha, self.beta, size=size)

    def simulate_action(self):
        """
        Simulate real world action based on the beta distribution.
        """
        beta_sample = self.sample(size=1)[0]
        return np.random.choice([0, 1], 1, p=[1-beta_sample, beta_sample])[0]

    def pdf(self, x):
        """
        Returns PDF value at given x drawn from the beta distribution.
        """
        return self.to_scipy().pdf(x)

    def cdf(self, x):
        """
        Returns CDF value at given x drawn from the beta distribution.
        """
        return self.to_scipy().cdf(x)

    def posterior(self, l, u):
        """
        Returns posterior probability drawn from the beta distribution for values in the range of 'l' to 'u'.
        """
        if l > u:
            return 0.0
        return self.cdf(u) - self.cdf(l)

    def mean(self):
        return self.to_scipy().mean()

    def plot(self, lim: tuple = None,
             ax: plt.axes = None,
             label=None, pp=200, normalize=False):
        """
        Plot the beta distribution on an axes.

        Args:
            lim(tuple, optional): lower and upper limit to plot. Default: None (mean +- 4 std)
            ax (plt.axes, optional): Matplotlib axes to draw on. New one will be created if none is given. Defaults to None.
            label (str, optional): Unique label to be added to the plot. Defaults to None.
            pp (int, optional): Numer of points to draw probability for (similar to resolution). Defaults to 200.

        Return:
            matplotlib.pyplot.axes with the distribution ploted.
        """

        if lim is None:
            mean = self.to_scipy().mean()
            std = self.to_scipy().std()
            l = mean - 4 * std
            u = mean + 4 * std
        else:
            l, u = lim

        x = np.linspace(u, l, pp)
        y = self.pdf(x)
        if normalize:
            y = y / y.sum()

        if ax is None:
            fig, ax = plt.subplots()

        legend_label = "p={:.2f}".format(self.to_scipy().mean())
        if label is not None:
            legend_label = label + ', ' + legend_label
        ax.plot(x, y, label=legend_label)
        ax.margins(y=0)
        interval = self.to_scipy().interval(0.95)
        ax.fill_between(x, y, where=(x > interval[0]) & (
            x < interval[1]), alpha=.5)

        return ax

    @staticmethod
    def plot_multiple(ax=None, **kwargs):
        """
        Plot multiple Beta distributions on the same axes.

        Args:
            ax (matplotlib.pyplot.axes, optional): The axes to plot on. If None, new axes will be reated. Defaults to None.
            kwargs : beta distributions to plot (with label as key).

        Example:
            Beta.plot_multiple(A=Beta(10, n=100), B=Beta(20, n=100))
        """
        if ax is None:
            fig, ax = plt.subplots()

        for key, value in kwargs.items():
            value.plot(label=key, ax=ax)
        
        plt.legend()
        plt.show()

    def to_json(self):
        """Exports beta distribution parameters (alpha, beta and N) as a python dictionary.

        Returns:
            dict: beta distribution parameters.
        """
        return vars(self)

    @staticmethod
    def from_json(json):
        """
        Load a Beta instance from json (dict) object. 

        Args:
            json (dict): a dictionary with the parameters of the beta distribution.

        Returns:
            Beta: instance wtih given parameters. 
        """
        return Beta(**json)
