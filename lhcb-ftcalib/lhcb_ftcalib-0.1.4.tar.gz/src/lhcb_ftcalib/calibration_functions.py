import numpy as np

def p_conversion_matrix(npar):
    r""" Returns matrix :math:`C` that converts internal representation of
        parameters into the traditional form
        :math:`C\cdot (p^+_0,\cdots, p^+_n, p^-_0,\cdots,p^-_n) = (p_0,\cdots, p_n, \Delta p_0,\cdots,\Delta p_n)`

        :param npar: number of calibration parameters per flavour
        :type npar: int
        :return: parameter transformation
        :rtype: numpy.ndarray
    """
    upper = np.concatenate([0.5 * np.eye(npar), 0.5 * np.eye(npar)]).T
    lower = np.concatenate([np.eye(npar), -np.eye(npar)]).T
    return np.concatenate([upper, lower])


class CalibrationFunction:
    r"""
    Calibration function base type. All calibration classes should inherit from this type.
    Calibration functions receive calibration parameters in the following order

    params :math:`= (p^+_0,\cdots, p^+_n, p^-_0,\cdots,p^-_n)`
    """

    def __init__(self, npar, link):
        self.npar = npar
        self.start_params = np.zeros(2 * self.npar)
        self.param_names        = [f"p{i}+" for i in range(npar)]
        self.param_names       += [f"p{i}-" for i in range(npar)]
        self.param_names_delta  = [f"p{i}"  for i in range(npar)]
        self.param_names_delta += [f"Dp{i}" for i in range(npar)]
        self.link  = link


class PolynomialCalibration(CalibrationFunction):
    r"""
    PolynomialCalibration computes a calibration polynomial
    depending on the measured flavour or the decay flavour during calibration

    :math:`\displaystyle\omega(\eta, d, \langle\eta\rangle, \vec{p}^+, \vec{p}^-)=\displaystyle g\left(\delta_{d,1}\left(g^{-1}(\langle\eta\rangle)+\sum_{i}p_i^+P_i\right)+\delta_{d,-1}\left(g^{-1}(\langle\eta\rangle)+\sum_{i}p_i^-P_i\right)\right)``

    whereby

    :math:`P_i = (g^{-1}(\eta)-g^{-1}(\langle\eta\rangle))^i`

    :param npar: Number of parameters per flavour (npar = polynomial degree + 1)
    :type npar: int
    :param link: link function :math:`g`
    :type link: link_function
    """

    def __init__(self, npar, link):
        CalibrationFunction.__init__(self, npar, link)

        # Set p1 parameters to 1
        self.start_params[1] = 1
        self.start_params[self.npar + 1] = 1

    def eval(self, params, eta, dec, avg_eta):
        r"""
        Compute the calibrated mistag given the calibration parameters params,
        the raw mistag eta, the tagging decision (or decay flavour) dec and the average raw mistag avg_eta

        :param params: Calibration parameters [p0+, ..., pn+, p0-, ..., pn-]
        :type params: list
        :param eta: mistags
        :type eta: list
        :param dec: tagging decision
        :type dec: list
        :param avg_eta: Mean mistag
        :type avg_eta: float

        :return: calibrated mistag :math:`\omega(\eta)`
        :rtype: list
        """
        eta_invl         = self.link.InvL(avg_eta)
        omega            = np.zeros(len(eta))
        omega[dec ==  1] = eta_invl + np.polyval(params[:self.npar][::-1], self.link.InvL(eta[dec ==  1]) - eta_invl)
        omega[dec == -1] = eta_invl + np.polyval(params[self.npar:][::-1], self.link.InvL(eta[dec == -1]) - eta_invl)
        return self.link.L(omega)

    def eval_ignore_delta(self, params, eta, avg_eta):
        r"""
        Compute the calibrated mistag given the calibration parameters params,
        the raw mistag eta, and the average raw mistag avg_eta while ignoring
        delta parameters. This method is always called when a calibration is
        applied, even for the calibrated mistags of a tagger that was just used
        to determine a calibration.

        :math:`\overline{\omega}=g\left(g^{-1}(\langle\eta\rangle) + \sum_{j=0}^mp_j(g^{-1}(\eta)-g^{-1}(\langle\eta\rangle))^j\right)`

        :param params: Flavour averaged calibration parameters [p0 ... pn]
        :type params: list
        :param eta: mistags
        :type eta: list
        :param avg_eta: Mean mistag
        :type avg_eta: float

        :return: calibrated mistag :math:`\omega`
        :rtype: list
        """
        eta_invl = self.link.InvL(avg_eta)
        return self.link.L(eta_invl + np.polyval(params[::-1], self.link.InvL(eta) - eta_invl))

    def eval_plotting(self, params, eta, dec, avg_eta):
        r"""
        Returns a single curve for both flavours by weighting it depending on how many events have been
        tagged for each flavour. Only used for plotting purposes
        :math:`\displaystyle\omega^\mathrm{plot}(\eta, d, \langle\eta\rangle, \vec{p}^+, \vec{p}^-)=\left.f^+\omega(\eta, d, \langle\eta\rangle, \vec{p}^+, \vec{p}^-)\right\vert_{d=1}+\left.f^-\omega(\eta, d, \langle\eta\rangle, \vec{p}^+, \vec{p}^-)\right\vert_{d=-1}`

        whereby :math:`f^+=N_{d=1}/N, f^-=N_{d=-1}/N`

        :param params: parameter list
        :type params: list
        :param eta: mistags
        :type eta: list
        :param dec: tagging decision
        :type dec: list
        :param avg_eta: Mean mistag
        :type avg_eta: float

        :return: calibrated mistag :math:`omega`
        :rtype: list
        """
        n_pos = np.sum(dec ==  1)
        n_neg = np.sum(dec == -1)
        f = n_pos / (n_pos + n_neg)
        eta_invl = self.link.InvL(avg_eta)

        omega  =       f * self.link.L(eta_invl + np.polyval(params[:self.npar][::-1], self.link.InvL(eta) - eta_invl))
        omega += (1 - f) * self.link.L(eta_invl + np.polyval(params[self.npar:][::-1], self.link.InvL(eta) - eta_invl))

        return omega

    def derivative(self, partial, params, eta, dec, avg_eta):
        r""" Computes the partial derivative wrt. a calibration parameter :math:`p_m^\pm`

            :math:`\displaystyle\frac{\partial\omega}{\partial p_m^\pm}(\eta_i, d_i)=\frac{\partial g}{\partial\eta}(\omega(\eta_i, d_i))(g^{-1}(\eta_i)-g^{-1}(\langle\eta\rangle))^m\delta_{d=\pm 1}`

            :param partial: partial derivative index, see base type constructor
            :type params: int
            :param params: parameter list
            :type params: list
            :param eta: mistags
            :type eta: list
            :param dec: tagging decision
            :type dec: list
            :param avg_eta: Mean mistag
            :type avg_eta: float

            :return: Partial calibration function derivative of given data
            :rtype: list
        """
        D = self.link.DL(self.eval(params, eta, dec, avg_eta))
        if partial < self.npar:
            D[dec ==  1] *= (self.link.InvL(eta[dec == 1]) - self.link.InvL(avg_eta)) ** partial
            D[dec == -1] = 0
        else:
            D[dec == -1] *= (self.link.InvL(eta[dec == -1]) - self.link.InvL(avg_eta)) ** (partial - self.npar)
            D[dec ==  1] = 0

        return D

    def gradient(self, params, eta, dec, avg_eta):
        r""" Computes the gradient of the calibration wrt. to the calibration parameters
            :math:`\nabla \omega=\sum_m\frac{\partial\omega}{\partial p_m}\vec{e}_m`

            :param params: parameter list
            :type params: list
            :param eta: mistags
            :type eta: list
            :param dec: tagging decision
            :type dec: list
            :param avg_eta: Mean mistag
            :type avg_eta: float

            :return: Partial calibration function derivative of given data
            :rtype: list
        """
        return np.array([self.derivative(i, params, eta, dec, avg_eta) for i in range(self.npar * 2)])
