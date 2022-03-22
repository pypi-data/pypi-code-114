import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

from .base import BasePrior
from .gamma import Gamma


class Normal(BasePrior):
    def __init__(self, mu=0, var=1, n=0, **kwargs):
        """
        Define a new Normal distribution of given mean, variance and sample size.

        Args:
            mu (int/float, optional): the mean of the sample. Defaults to 0.
            var (int/float, optional): the variance of the sample. Defaults to 1.
            n (int, optional): the sample size. Defaults to 0.
        """
        self.mu = mu
        self.var = var
        self.n = n

    def update(self,
               mu=None,
               var=None,
               n=None,
               data=None):
        """
        Update the Normal distribution with new observations given by an array of new data or summary statistics.

        Args:
            mu (int/float, optional): the mean of the new observations. Defaults to None.
            var (int/float, optional): the variance of the new observations. Defaults to None.
            n (int, optional): the number of new observations. Defaults to None.
            data (iterable, optional): array of new observations. if given, other arguments are ignored. Defaults to None.

        Raises:
            ValueError: 
            - Must provide either data array or mu, var AND n.
            - Given or found variance is equal to 0.

        Returns:
            Normal object with updated parameters.
        """
        # update by data vector
        if data is not None:
            new_mu, new_var, new_n = np.mean(data), np.var(data), len(data)

        # update by mean, variance and sample size
        elif np.all([mu, var, n]) is not None:
            new_mu, new_var, new_n = mu, var, n

        else:
            raise ValueError(
                "Must provide iterable data array (data) OR measured mean (mu), variance (var) AND number of samples (n).")

        post_n = self.n + new_n
        
        # handle cases of the new variance equals to zero, use known variance instead
        if new_var == 0 and self.var == 0:
            post_nu = (self.mu * self.n + new_mu * new_n) / post_n
            post_tau = (self.n * np.power(self.mu - post_nu, 2) + new_n * np.power(new_mu - post_nu, 2)) / post_n
        else:
            if new_var == 0 and self.var != 0:
                new_var = self.var

            elif new_var != 0 and self.var == 0:
                self.var = new_var

            weights = (self.n / self.var), (new_n / new_var)
            post_nu = np.average((self.mu, new_mu), weights=weights)
            post_tau = 1 / np.sqrt(np.sum(weights))
        
        
        return Normal(mu=post_nu, var=post_tau, n=post_n)

    def to_scipy(self):
        '''
        Returns current distribution as scipy.stats.norm instance.
        '''
        return stats.norm(loc=self.mu, scale=np.sqrt(self.var))

    def sample(self, size=1):
        '''
        Draw a sample from the modeled distribution of a given size.
        '''
        return np.random.normal(loc=self.mu,
                                scale=np.sqrt(self.var),
                                size=size)

    def pdf(self, x):
        """
        Returns probability density function (PDF) value at given x drawn from the distribution.
        """
        return self.to_scipy().pdf(x)

    def cdf(self, x):
        """
        Returns commutative distribution function (CDF) value at given x drawn from the distribution.
        """
        return self.to_scipy().cdf(x)

    def posterior(self, l, u):
        """
        Returns posterior probability drawn from the  distribution for values in the range of 'l' to 'u'. 
        Equivalent to cdf(u) - cdf(l).
        """
        if l > u:
            return 0.0

        return self.cdf(u) - self.cdf(l)

    def plot(self, lim: tuple = None,
             ax: plt.axes = None, label="", pp=200, normalize=False):
        """
        Plot the normal distribution on an axes.

        Args:
            lim(tuple, optional): lower and upper limit to plot. Default: None (mean +- 4 std)
            ax (plt.axes, optional): Matplotlib axes to draw on. New one will be created if none is given. Defaults to None.
            label (str, optional): Unique label to be added to the plot. Defaults to None.
            pp (int, optional): Numer of points to draw probability for (similar to resolution). Defaults to 200.

        Return:
            matplotlib.pyplot.axes with the distribution ploted.
        """
        if lim is None:
            l = self.mu - 4 * np.sqrt(self.var)
            u = self.mu + 4 * np.sqrt(self.var)
        else:
            l, u = lim

        x = np.linspace(u, l, pp)
        y = self.pdf(x)
        if normalize:
            y = y / y.sum()

        if ax is None:
            fig, ax = plt.subplots()

        ax.plot(x, y, label="{} \u03bc={}, \u03c3={}".format(label,
                                                             round(self.mu, 2),
                                                             round(np.sqrt(self.var), 2)))
        ax.margins(y=0)
        interval = self.to_scipy().interval(0.95)
        ax.fill_between(x, y, where=(x > interval[0]) & (
            x < interval[1]), alpha=.5)

        return ax

    @staticmethod
    def plot_multiple(ax=None, **kwargs):
        """
        Plot multiple Normal distributions on the same axes.

        Args:
            ax (matplotlib.pyplot.axes, optional): The axes to plot on. If None, new axes will be reated. Defaults to None.
            kwargs : normal distributions to plot (with label as key).
        """
        if ax is None:
            fig, ax = plt.subplots()

        for key, value in kwargs.items():
            value.plot(label=key, ax=ax)

        plt.legend()
        plt.show()

    def to_json(self):
        """Exports normal distribution parameters as a python dictionary.

        Returns:
            dict: normal distribution parameters.
        """
        return vars(self)

    @staticmethod
    def from_json(json):
        """
        Load a Normal instance from json (dict) object. 

        Args:
            json (dict): a dictionary with the parameters of the normal distribution.

        Returns:
            Normal: instance wtih given parameters. 
        """
        return Normal(**json)


class NormalGamma(BasePrior):
    def __init__(self, mu=0, var=1, n=0, dof=None, **kwargs):
        """
        Define a new NormalGamma distribution of given mean, variance, sample size and degress of freedom.

        Args:
            mu (int/float, optional): the mean of the sample. Defaults to 0.
            var (int/float, optional): the variance of the sample. Defaults to 1.
            n (int, optional): the sample size. Defaults to 0.
            dof (int, optional): the degress of freedom. Equals to samples size minus 1 when None. Defaults to None. 
        """

        self.mu = mu
        self.var = var
        self.n = n

        if dof is None:
            self.dof = self.n - 1
        else:
            self.dof = dof

    def update(self, 
               mu=None,
               var=None,
               n=None,
               data=None):
        """
        Updates the NormalGamma distribution given summary statistics or a set of new observations.

        Args:
            data (iterable): array of new observations.

        Returns:
            NormalGamma: updated prior.
        """
        if data is not None:
            new_m, new_var, new_n = np.mean(data), np.var(data), len(data)

        # update by mean, variance and sample size
        elif np.all([mu, var, n]) is not None:
            new_m, new_var, new_n = mu, var, n

        else:
            raise ValueError(
                "Must provide iterable data array (data) or measured mean (mu), variance (var) and number of samples (n).")

        # TODO: clean code below to match update in Normal class

        prior_m, prior_var, prior_n = self.mu, self.var, self.n
        prior_dof = self.dof

        post_n = new_n + prior_n
        post_m = ((new_m * new_n) + (prior_m * prior_n)) / post_n
        post_dof = prior_dof + new_n

        new_ssd = new_var * (new_n - 1)
        prior_ssd = prior_var * prior_dof
        post_ssd = ((prior_n * new_n) / post_n) * \
            np.power((new_m - prior_m), 2)
        post_var = (1/post_dof) * np.sum((new_ssd, prior_ssd, post_ssd))

        return NormalGamma(mu=post_m, var=post_var, n=post_n, dof=post_dof)

    def to_scipy(self, var=None):
        '''
        Returns a tuple of normal and gamma distributions in scipy objects.
            (scipy.stats.norm, scipy.stats.gamma)
        '''
        return self.normal(var=var), self.gamma()

    def gamma(self):
        """
        Returns the Gamma prior of the NormalGamma.
        """
        shape = self.dof / 2
        rate = (self.dof * self.var) / 2

        return Gamma(shape=shape, rate=rate)

    def normal(self, var=None):
        """
        Returns the Normal prior of the NormalGamma for a given variance.
        If no variance is given, the mean variance will be used.
        """
        norm_mu = self.mu

        if var is None:
            var = self.var

        norm_var = var / self.n

        return Normal(mu=norm_mu, var=norm_var, n=1)

    def sample(self, size=1, return_var=False):
        '''
        Draw a sample from the modeled distribution of a given size.
        '''
        if (size <= 0) or type(size) is not int:
            raise ValueError("size must be positive non-zero integer.")

        gamma = self.gamma()
        sampled_var = 1/gamma.sample(size)

        # if sampling size is more than 1, sample normal mean for each variance
        if size > 1:
            sampled_mean = []
            for var in sampled_var:
                normal = self.normal(var)
                sampled_mean.append(normal.sample())

        normal = self.normal(sampled_var)
        sampled_mean = normal.sample(size)

        if return_var:
            return np.column_stack([sampled_mean, sampled_var])

        return np.array(sampled_mean)

    def pdf(self, x, var=None):
        """
        Returns probability density function (PDF) value at given x drawn from the distribution.
        """
        if var is None:
            var = 1/self.gamma().to_scipy().mean()

        return self.normal(var).pdf(x), self.gamma().pdf(1/var)

    def cdf(self, x, var=None):
        """
        Returns commutative distribution function (CDF) value at given x drawn from the distribution.
        """
        if var is None:
            var = 1/self.gamma().to_scipy().mean()

        return self.normal(var).cdf(x), self.gamma().cdf(1/var)

    def posterior(self, mu_l, mu_u, var_l, var_u):
        """
        Returns posterior probability drawn from the  distribution for values in the range of 'l' to 'u'. 
        Equivalent to cdf(u) - cdf(l).
        """
        if mu_l > mu_u or var_l > var_u:
            return 0.0

        # var values replaced because of we actually recieve inverse var from function.
        u_mu, l_var = self.cdf(mu_u, var_u)
        l_mu, u_var = self.cdf(mu_l, var_l)

        mu_proba = u_mu - l_mu
        var_proba = u_var - l_var

        return mu_proba * var_proba

    def plot(self, labels: tuple = (None, None), ax: np.ndarray = None):
        """
        Plot the normal-gamma distribution on two axes.
        The first axes will be used to plot the Gamma distribution of the inverse-variance and the second axes will be used to plot the Normal distibution of the mean given the mean variance.

        Args:
            lim(tuple, optional): lower and upper limit to plot. Default: None (mean +- 4 std)
            ax (np.ndarray of plt.axes, optional): a list of two matplotlib axes to draw on. New one will be created if none is given. Defaults to None.
            label (tuple, optional): tuple of two unique labels to be added to the plots. Defaults to (None,None).

        Return:
            matplotlib.pyplot.axes with the distributions ploted.
        """
        if ax is None:
            fig, ax = plt.subplots(1, 2)

        # inverse variance
        ax[0] = self.gamma().plot(label=labels[0], ax=ax[0])
        ax[0].set_xlabel("1/\u03c3")
        ax[0].set_title(
            r"$\phi \sim Gamma(\frac{\nu^2}{2}, \frac{\nu^2s^{2}}{2})$")

        # normal
        var = 1 / self.gamma().to_scipy().mean()
        ax[1] = self.normal(var).plot(label=labels[1], ax=ax[1])
        ax[1].set_xlabel("\u03bc")
        ax[1].set_title(
            r"$\mu | \sigma^2 \sim Normal(\bar{x}, \frac{\sigma^2}{n})$")

        return ax

    @staticmethod
    def plot_multiple(ax=None, **kwargs):
        """
        Plot multiple NormalGamma distributions on the same axes.

        Args:
            ax (np.ndarray of plt.axes, optional): The axes to plot on. If None, new axes will be reated. Defaults to None.
            kwargs : NormaGamma objects to plot (with label as key).
        """
        if ax is None:
            fig, ax = plt.subplots(1, 2)

        for key, value in kwargs.items():
            ax[0] = value.gamma().plot(label=key, ax=ax[0])
            ax[0].set_xlabel("1/\u03c3")
            ax[0].set_title(
            r"$\phi \sim Gamma(\frac{\nu^2}{2}, \frac{\nu^2s^{2}}{2})$")
            
            ax[1] = value.normal().plot(label=key, ax=ax[1])
            ax[1].set_xlabel("\u03bc")
            ax[1].set_title(
            r"$\mu | \sigma^2 \sim Normal(\bar{x}, \frac{\sigma^2}{n})$")
            
        return ax

    def to_json(self):
        """
        Exports object parameters to dictionary.
        """
        return vars(self)

    @staticmethod
    def from_json(json):
        """
        Returns new NormalGamma instance with parameters from json.
        """
        return NormalGamma(**json)