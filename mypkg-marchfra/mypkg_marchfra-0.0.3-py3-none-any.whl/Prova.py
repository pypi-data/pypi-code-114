import pandas as pd
from uncertainties import ufloat, unumpy as unp
import numpy as np
from mypkg.stattest import calc_chisquare
import matplotlib.pyplot as plt

plt.style.use(['grid', 'science', 'notebook'])

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



df_absorb = pd.read_excel('/Users/francescomarchisotti/Documents/Uni/Terzo anno/IFNS/dati.xlsx', sheet_name=2).dropna()
# print(df_absorb)

x = 0.21  # cm
sx = 0.01  # cm
ro = 11.34  # g cm^-3


def absorb(x, p0, mu_ro):
	return p0 * np.exp(-mu_ro * x * ro)




N_tot = df_absorb['N_tot']
N_bkg = df_absorb['N_bkg']
N_net = unp.uarray(N_tot - N_bkg, np.sqrt(N_tot + N_bkg))
n_spessori = df_absorb['n_spessori']
t_live = df_absorb['t_live [s]']
R = N_net / t_live





xerr = n_spessori * sx
# xerr = None




par_names = ['R_0', 'mu_ro']
par_um = ['s^-1', 'cm^2 / g']
pars, cov = curve_fit(absorb, n_spessori * x, np.array([r.n for r in R]), xerr=xerr, yerr=np.array([r.s for r in R]), p0=[1, 0.1035])
chisq, NDF, p = calc_chisquare(absorb, n_spessori * x, np.array([r.n for r in R]), xerr=n_spessori * sx, yerr=np.array([r.s for r in R]), pars=pars)
# print('\n\nFit Coefficiente di assorbimento di massa')
# print(f'Chisq / NDF: {chisq:.3g} / {NDF}')
# print(f'p-value: {p:.3g}, good fit: {p > 0.05}\n')

print(f'Fit parameters: R(X) = R_0 * exp(-mu/ro X)')
for (name, val, err, um) in zip(par_names, pars, np.diag(cov)**0.5, par_um):
	print(f'{name}: {ufloat(val, err)} {um}')



fig, ax = plt.subplots(1, 1)
ax.errorbar(n_spessori * x, np.array([r.n for r in R]), xerr=n_spessori * sx, yerr=np.array([r.s for r in R]), c='k', ecolor='k', capsize=3, linestyle='none')
xdense = np.linspace(0, n_spessori.to_numpy()[-1] * x)
ydense = absorb(xdense, *pars)
ax.plot(xdense, ydense, c='tab:red', zorder=1)

ax.set_title('Coefficiente di assorbimento di massa')
ax.set_xlabel(r'$\Delta x$ $[cm]$')
ax.set_ylabel(r'$Rate$ $[s^{-1}]$')

print(f'Compatibile con 0.1035 cm^2 / g: {abs((0.1035 - ufloat(pars[1], cov[1][1]**0.5)).std_score(0)) < 1.96}')


fig.tight_layout()
plt.show()
