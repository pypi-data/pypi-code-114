def calc_chisquare(func, x, y, xerr=None, yerr=None, pars=None):
	'''
	This function calculates the chi square value for a set of data and a fit on that data.
	Args:
	- func (function) : the model function
	- x (numpy.ndarray) : the values on the x-axis
	- y (numpy.ndarray) : the values on the y-axis
	- xerr (numpy.ndarray) : the errors on the x-axis. Defaults to no error
	- yerr (numpy.ndarray) : the errors on the y-axis. Defaults to no error
	- pars (numpy.ndarray) : the parameters of the fitted function. Defaults to no parameters
	Returns:
	- chisq (float) : chi square value
	- NDF (int) : number of degrees of freedom
	- p (float) : p-value
	'''
	import numpy as np
	from scipy.misc import derivative
	from scipy.stats import chi2

	if pars is None:
		num = (y - func(x))**2
	else:
		num = (y - func(x, *pars))**2

	if xerr is None or xerr==0:
		if yerr is None or yerr==0:
			den = 1
		else:
			den = yerr**2
	else:
		if yerr is None:
			yerr = 0
		if pars is None:
			den = yerr**2 + (xerr * derivative(func, x, dx=0.001))**2
		else:
			den = yerr**2 + (xerr * derivative(func, x, args=pars, dx=0.001))**2

	chisq = np.sum(num / den)
	NDF = len(x) - len(pars)
	p = chi2.sf(chisq, NDF)
	return chisq, NDF, p


def curve_fit(func, x, y, xerr=None, yerr=None, p0=None, absolute_sigma=True, check_finite=True, bounds=None, signif_value=0.05, method=None, jac=None, **kwargs):
	'''
	Fits a model function on a set of data.
	Args:
	- func (function) : the model function
	- x (numpy.ndarray) : the values on the x-axis
	- y (numpy.ndarray) : the values on the y-axis
	- xerr (numpy.ndarray) : the errors on the x-axis. Defaults to no error
	- yerr (numpy.ndarray) : the errors on the y-axis. Defaults to no error
	- p0 (list) : the initial guess on the parameters
	- absolute_sigma (bool) : see scipy.optimize.curve_fit's documentation
	- check_finite (bool) : see scipy.optimize.curve_fit's documentation
	- bounds (2-tuple)
		Lower and upper bounds on parameters. Defaults to no bounds.
		Each element of the tuple must be either an array with the length equal
		to the number of parameters, or a scalar (in which case the bound is
		taken to be the same for all parameters). Use ``np.inf`` with an
		appropriate sign to disable bounds on all or some parameters.
	- signif_value (float) : significance value (used for p-value). Defaults to 5%
	- method, jac, **kwargs : see scipy.optimize.curve_fit's documentation
	Returns:
	- pars (numpy.ndarray) : the parameters of the fit
	- cov (numpy.ndarray) : the covariance matrix of the fit
	'''
	import numpy as np
	from scipy.misc import derivative
	from scipy.optimize import curve_fit

	if bounds is None:
		bounds = (-np.inf, np.inf)

	pars1, cov1 = curve_fit(f=func, xdata=x, ydata=y, p0=p0, sigma=yerr, absolute_sigma=absolute_sigma, check_finite=check_finite, bounds=bounds, method=method, jac=jac, **kwargs)

	if xerr is None or xerr.all(0):
		chisq, NDF, p = calc_chisquare(func, x, y, xerr, yerr, pars1)
		print(f'Chisq / NDF: {chisq:.3g} / {NDF}')
		print(f'p-value: {p:.3g}, good fit: {p > signif_value}\n')
		return pars1, cov1

	yerr = (yerr**2 + (xerr * derivative(func, x, args=pars1, dx=0.001))**2)**0.5
	pars, cov = curve_fit(f=func, xdata=x, ydata=y, p0=p0, sigma=yerr, absolute_sigma=absolute_sigma, check_finite=check_finite, bounds=bounds, method=method, jac=jac, **kwargs)

	chisq, NDF, p = calc_chisquare(func, x, y, xerr, yerr, pars)
	print(f'Chisq / NDF: {chisq:.3g} / {NDF}')
	print(f'p-value: {p:.3g}, good fit: {p > signif_value}\n')

	return pars, cov
