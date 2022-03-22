import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

from .base import BasePrior


class Gamma(BasePrior):
    def __init__(self, shape=0, scale=None, rate=None, **kwargs):
        """
        Define a new Gamma distribution of given shape and either scale or rate. 
        If scale is given the rate will equal to 1/scale. Likewise, if rate is given then scale will equal to 1 / rate.

        Args:
            shape (int/float, optional): the shape parameter of the gamma distribution. Defaults to 0.
            scale (int/float, partially optional): the scale parameter of the gamma distribution. Must be provided if rate is not provided. Defaults to None.
            rate (int/float, partially optional): the rate parameter of the gamma distribution. Must be provided if scale is not provided. Defaults to None.

        Raises:
            ValueError: if neither scale or rate are given, an error will be risen. Must provide either one.
        """
        self.shape = shape

        if (scale is not None) and (rate is None):
            self.scale = scale
        elif (rate is not None) and (scale is None):
            self.scale = 1/rate
        else:
            raise ValueError("either 'scale' OR 'rate' should be provided.")

        self._update_rate()

    def _update_rate(self):
        # private function to update the rate atribute. potentially to be used by other methdos if needed.
        self.rate = 1/self.scale

    @staticmethod
    def from_normal(mean, var=None, std=None):
        """
        Generate a Gamma distribution instance from normal distribution parameters (mean and either var OR std).

        Args:
            mean (int/float): the mean value of the normal distribution.
            var (int/float, partially optional): the variance of the normal distribution. Must be provided if std is not provided. Defaults to None.
            std (int/float, partially optional): the standard deviation of the normal distribution. Must be provided if var is not provided. Defaults to None.

        Raises:
            ValueError: if neither var or std are given, an error will be risen. Must provide either one.

        Returns:
            a Gamma instance of the gamma distribution created from the normal parameters.
        """
        shape = np.power(mean, 2) / var

        if var is not None and std is None:
            scale = var / mean

        elif var is None and std is not None:
            scale = np.power(std, 2) / mean

        else:
            raise ValueError("Must provide either var or std.")

        return Gamma(shape=shape, scale=scale)

    def to_scipy(self):
        """
        Returns current gamma distribution as scipy.stats.gamma instance.
        """
        return stats.gamma(a=self.shape, scale=self.scale)

    def update(self, count: int = None, 
                     observations: int= None, 
                     data:np.array = None):
        """
        Update the Gamma distribution given a set of new observations (data) or a summary of counts and observations.

        Args:
            count (int, optional): positive counts observed. Defaults to None.
            observations (int, optional): number of observations obtained. Defaults to None.
            data (np.array, optional): array of data containing counts. Defaults to None.

        Returns:
            an updated Gamma instance.
        """
        summary_given = (count is not None) and (observations is not None)
        either_summary_given = (count is not None) or (observations is not None)
        data_given =  data is not None

        if data_given and not either_summary_given:
            post_shape = self.shape + sum(data)
            post_scale = self.scale / (len(data) * self.scale + 1)

        elif summary_given and not data_given:
            post_shape = self.shape + count
            post_scale = self.scale / (observations * self.scale + 1)

        else:
            ValueError("Must provide either summary information or data array.")
            
        return Gamma(shape=post_shape, scale=post_scale)

    def sample(self, size=1):
        """
        Draw samples from the gamma distribution.

        Args:
            size (int, defaults=1): the number of samples to draw.

        Returns:
            np.array of given size with random samples from the distribution. 
        """
        return np.random.gamma(shape=self.shape, scale=self.scale, size=size)

    def pdf(self, x):
        """
        Returns probability density function (PDF) value at given x drawn from the gamma distribution.
        """
        return self.to_scipy().pdf(x)

    def cdf(self, x):
        """
        Returns commutative distribution function (CDF) value at given x drawn from the gamma distribution.
        """
        return self.to_scipy().cdf(x)

    def posterior(self, l, u):
        """
        Returns posterior probability drawn from the gamma distribution for values in the range of 'l' to 'u'. 
        Equivalent to cdf(u) - cdf(l).
        """
        if l > u:
            return 0.0

        return self.cdf(u) - self.cdf(l)

    def plot(self, lim: tuple = None,
             ax: plt.axes = None, label="", pp=200, normalize=False):
        """
        Plot the gamma distribution on an axes.

        Args:
            lim(tuple, optional): lower and upper limit to plot. Default: None (mean +- 4 std)
            ax (plt.axes, optional): Matplotlib axes to draw on. New one will be created if none is given. Defaults to None.
            label (str, optional): Unique label to be added to the plot. Defaults to None.
            pp (int, optional): Numer of points to draw probability for (similar to resolution). Defaults to 200.

        Return:
            matplotlib.pyplot.axes with the distribution ploted.
        """

        if lim is None:
            mu, std = self.to_scipy().mean(), self.to_scipy().std()
            l = mu - 4 * std
            u = mu + 4 * std
        else:
            l, u = lim

        x = np.linspace(u, l, pp)
        y = self.pdf(x)
        if normalize:
            y = y / y.sum()

        if ax is None:
            fig, ax = plt.subplots()

        ax.plot(x, y, label="{} shape={}, scale={}".format(label,
                                                           round(
                                                               self.shape, 2),
                                                           round(self.scale, 2)))
        ax.margins(y=0)
        interval = self.to_scipy().interval(0.95)
        ax.fill_between(x, y, where=(x > interval[0]) & (
            x < interval[1]), alpha=.5)

        return ax

    @staticmethod
    def plot_multiple(ax=None, **kwargs):
        """
        Plot multiple Gamma distributions on the same axes.

        Args:
            ax (matplotlib.pyplot.axes, optional): The axes to plot on. If None, new axes will be reated. Defaults to None.
            kwargs : gamma distributions to plot (with label as key).

        Example:
            Gamma.plot_multiple(A=Gamma(10, scale=2), B=Gamma(20, scale=3))
        """
        if ax is None:
            fig, ax = plt.subplots()

        for key, value in kwargs.items():
            value.plot(label=key, ax=ax)

        plt.legend()
        plt.show()

    def to_json(self):
        """Exports gamma distribution parameters as a python dictionary.

        Returns:
            dict: gamma distribution parameters.
        """
        return vars(self)

    @staticmethod
    def from_json(json):
        """
        Load a Gamma instance from json (dict) object. 

        Args:
            json (dict): a dictionary with the parameters of the gamma distribution.

        Returns:
            Gamma: instance wtih given parameters. 
        """
        return Gamma(shape= json['shape'], 
                     scale = json['scale'])
