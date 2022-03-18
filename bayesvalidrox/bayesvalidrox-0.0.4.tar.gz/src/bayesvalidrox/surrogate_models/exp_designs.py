#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math
import itertools
import chaospy
import scipy.stats as st
from tqdm import tqdm

from .apoly_construction import apoly_construction


class ExpDesigns:
    """
    This class generates samples from the prescribed marginals for the model
    parameters using the `Input` object.

    Attributes
    ----------
    Input : obj
        Input object containing the parameter marginals, i.e. name,
        distribution type and distribution parameters or available raw data.
    method : str
        Type of the experimental design. The default is `'normal'`. Other
        option is `'sequential'`.
    meta_Model : str
        Type of the meta_model.
    sampling_method : str
        Name of the sampling method for the experimental design. The following
        sampling method are supported:

        * random
        * latin_hypercube
        * sobol
        * halton
        * hammersley
        * korobov
        * chebyshev(FT)
        * grid(FT)
        * nested_grid(FT)
        * user
    hdf5_file : str
        Name of the hdf5 file that contains the experimental design.
    n_new_samples : int
        Number of (initial) training points.
    n_max_samples : int
        Number of maximum training points.
    mod_LOO_threshold : float
        The modified leave-one-out cross validation threshold where the
        sequential design stops.
    tradeoff_scheme : str
        Trade-off scheme to assign weights to the exploration and exploitation
        scores in the sequential design.
    n_canddidate : int
        Number of candidate training sets to calculate the scores for.
    explore_method : str
        Type of the exploration method for the sequential design. The following
        methods are supported:

        * Voronoi
        * random
        * latin_hypercube
        * LOOCV
        * dual annealing
    exploit_method : str
        Type of the exploitation method for the sequential design. The
        following methods are supported:

        * BayesOptDesign
        * BayesActDesign
        * VarOptDesign
        * alphabetic
        * Space-filling
    util_func : str or list
        The utility function to be specified for the `exploit_method`. For the
        available utility functions see Note section.
    n_cand_groups : int
        Number of candidate groups. Each group of candidate training sets will
        be evaulated separately in parallel.
    n_replication : int
        Number of replications. Only for comparison. The default is 1.
    post_snapshot : int
        Whether to plot the posterior in the sequential design. The default is
        `True`.
    step_snapshot : int
        The number of steps to plot the posterior in the sequential design. The
        default is 1.
    max_a_post : list or array
        Maximum a posteriori of the posterior distribution, if known. The
        default is `[]`.
    adapt_verbose : bool
        Whether to plot the model response vs that of metamodel for the new
        trining point in the sequential design.

    Note
    ----------
    The following utiliy functions for the **exploitation** methods are
    supported:

    #### BayesOptDesign (when data is available)
    - DKL (Kullback-Leibler Divergence)
    - DPP (D-Posterior-percision)
    - APP (A-Posterior-percision)

    #### VarBasedOptDesign -> when data is not available
    - Entropy (Entropy/MMSE/active learning)
    - EIGF (Expected Improvement for Global fit)
    - LOOCV (Leave-one-out Cross Validation)

    #### alphabetic
    - D-Opt (D-Optimality)
    - A-Opt (A-Optimality)
    - K-Opt (K-Optimality)
    """

    def __init__(self, Input, method='normal', meta_Model='pce',
                 sampling_method='random', hdf5_file=None,
                 n_new_samples=1, n_max_samples=None, mod_LOO_threshold=1e-16,
                 tradeoff_scheme=None, n_canddidate=1, explore_method='random',
                 exploit_method='Space-filling', util_func='Space-filling',
                 n_cand_groups=4, n_replication=1, post_snapshot=False,
                 step_snapshot=1, max_a_post=[], adapt_verbose=False):

        self.InputObj = Input
        self.method = method
        self.meta_Model = meta_Model
        self.sampling_method = sampling_method
        self.hdf5_file = hdf5_file
        self.n_new_samples = n_new_samples
        self.n_max_samples = n_max_samples
        self.mod_LOO_threshold = mod_LOO_threshold
        self.explore_method = explore_method
        self.exploit_method = exploit_method
        self.util_func = util_func
        self.tradeoff_scheme = tradeoff_scheme
        self.n_canddidate = n_canddidate
        self.n_cand_groups = n_cand_groups
        self.n_replication = n_replication
        self.post_snapshot = post_snapshot
        self.step_snapshot = step_snapshot
        self.max_a_post = max_a_post
        self.adapt_verbose = adapt_verbose

    # -------------------------------------------------------------------------
    def generate_samples(self, n_samples, sampling_method='random',
                         transform=False):
        """
        Generates samples with given sampling method

        Parameters
        ----------
        n_samples : int
            Number of requested samples.
        sampling_method : str, optional
            Sampling method. The default is `'random'`.
        transform : bool, optional
            Transformation via an isoprobabilistic transformation method. The
            default is `False`.

        Returns
        -------
        samples: array of shape (n_samples, n_params)
            Generated samples from defined model input object.

        """
        try:
            samples = chaospy.generate_samples(
                int(n_samples), domain=self.JDist, rule=sampling_method
                )
        except:
            samples = self.JDist.resample(int(n_samples))

        # Transform samples to the original space
        if transform:
            tr_samples = self.transform(samples.T)
            return samples.T, tr_samples
        else:
            return samples.T

    # -------------------------------------------------------------------------
    def generate_ED(self, n_samples, sampling_method='random', transform=False,
                    max_pce_deg=None):
        """
        Generates experimental designs (training set) with the given method.

        Parameters
        ----------
        n_samples : int
            Number of requested training points.
        sampling_method : str, optional
            Sampling method. The default is `'random'`.
        transform : bool, optional
            Isoprobabilistic transformation. The default is `False`.
        max_pce_deg : int, optional
            Maximum PCE polynomial degree. The default is `None`.

        Returns
        -------
        samples : array of shape (n_samples, n_params)
            Selected training samples.

        """
        Inputs = self.InputObj
        self.ndim = len(Inputs.Marginals)
        if not hasattr(self, 'n_init_samples'):
            self.n_init_samples = self.ndim + 1
        n_samples = int(n_samples)

        # Check if PCE or aPCE metamodel is selected.
        if self.meta_Model.lower() == 'apce':
            self.apce = True
        else:
            self.apce = False

        # Check if input is given as dist or input_data.
        if len(Inputs.Marginals[0].input_data):
            self.input_data_given = True
        else:
            self.input_data_given = False

        # Get the bounds if input_data are directly defined by user:
        if self.input_data_given:
            for i in range(self.ndim):
                low_bound = np.min(Inputs.Marginals[i].input_data)
                up_bound = np.max(Inputs.Marginals[i].input_data)
                Inputs.Marginals[i].parameters = [low_bound, up_bound]

        # Generate the samples based on requested method
        self.raw_data, self.bound_tuples = self.init_param_space(max_pce_deg)

        # Pass user-defined samples as ED
        if sampling_method == 'user':
            samples = self.X
            self.n_samples = len(samples)

        # Sample the distribution of parameters
        elif self.input_data_given:
            # Case II: Input values are directly given by the user.

            if sampling_method == 'random':
                samples = self.random_sampler(n_samples)

            elif sampling_method == 'PCM' or \
                    sampling_method == 'LSCM':
                samples = self.pcm_sampler(max_pce_deg)

            else:
                # Create ExpDesign in the actual space using chaospy
                try:
                    samples = chaospy.generate_samples(n_samples,
                                                       domain=self.JDist,
                                                       rule=sampling_method).T
                except:
                    samples = self.JDist.sample(n_samples)

        elif not self.input_data_given:
            # Case I = User passed known distributions
            samples = chaospy.generate_samples(n_samples, domain=self.JDist,
                                               rule=sampling_method).T

        # Transform samples to the original space
        if transform:
            tr_samples = self.transform(samples)
            return samples, tr_samples
        else:
            return samples

    # -------------------------------------------------------------------------
    def init_param_space(self, max_deg=None):
        """
        Initializes parameter space.

        Parameters
        ----------
        max_deg : int, optional
            Maximum degree. The default is `None`.

        Returns
        -------
        raw_data : array of shape (n_params, n_samples)
            Raw data.
        bound_tuples : list of tuples
            A list containing lower and upper bounds of parameters.

        """
        Inputs = self.InputObj
        ndim = self.ndim
        rosenblatt_flag = Inputs.Rosenblatt
        mc_size = 50000

        # Save parameter names
        self.par_names = []
        for parIdx in range(ndim):
            self.par_names.append(Inputs.Marginals[parIdx].name)

        # Create a multivariate probability distribution
        if max_deg is not None:
            JDist, poly_types = self.build_dist(rosenblatt=rosenblatt_flag)
            self.JDist, self.poly_types = JDist, poly_types

        if self.input_data_given:

            self.MCSize = len(Inputs.Marginals[0].input_data)
            self.raw_data = np.zeros((ndim, self.MCSize))

            for parIdx in range(ndim):
                # Save parameter names
                try:
                    self.raw_data[parIdx] = np.array(
                        Inputs.Marginals[parIdx].input_data)
                except:
                    self.raw_data[parIdx] = self.JDist[parIdx].sample(mc_size)

        else:
            # Generate random samples based on parameter distributions
            self.raw_data = chaospy.generate_samples(mc_size,
                                                     domain=self.JDist)

        # Create orthogonal polynomial coefficients if necessary
        if self.apce and max_deg is not None and Inputs.poly_coeffs_flag:
            self.polycoeffs = {}
            for parIdx in tqdm(range(ndim), ascii=True,
                               desc="Computing orth. polynomial coeffs"):
                poly_coeffs = apoly_construction(self.raw_data[parIdx],
                                                 max_deg)
                self.polycoeffs[f'p_{parIdx+1}'] = poly_coeffs

        # Extract moments
        for parIdx in range(ndim):
            mu = np.mean(self.raw_data[parIdx])
            std = np.std(self.raw_data[parIdx])
            self.InputObj.Marginals[parIdx].moments = [mu, std]

        # Generate the bounds based on given inputs for marginals
        bound_tuples = []
        for i in range(ndim):
            if Inputs.Marginals[i].dist_type == 'unif':
                low_bound, up_bound = Inputs.Marginals[i].parameters
            else:
                low_bound = np.min(self.raw_data[i])
                up_bound = np.max(self.raw_data[i])

            bound_tuples.append((low_bound, up_bound))

        self.bound_tuples = tuple(bound_tuples)

        return self.raw_data, self.bound_tuples

    # -------------------------------------------------------------------------
    def build_dist(self, rosenblatt):
        """
        Creates the polynomial types to be passed to univ_basis_vals method of
        the MetaModel object.

        Parameters
        ----------
        rosenblatt : bool
            Rosenblatt transformation flag.

        Returns
        -------
        orig_space_dist : object
            A chaospy JDist object or a gaussian_kde object.
        poly_types : list
            List of polynomial types for the parameters.

        """
        Inputs = self.InputObj
        all_data = []
        all_dist_types = []
        orig_joints = []
        poly_types = []

        for parIdx in range(self.ndim):

            if Inputs.Marginals[parIdx].dist_type is None:
                data = Inputs.Marginals[parIdx].input_data
                all_data.append(data)
                dist_type = None
            else:
                dist_type = Inputs.Marginals[parIdx].dist_type
                params = Inputs.Marginals[parIdx].parameters

            if rosenblatt:
                polytype = 'hermite'
                dist = chaospy.Normal()

            elif dist_type is None:
                polytype = 'arbitrary'
                dist = None

            elif 'unif' in dist_type.lower():
                polytype = 'legendre'
                dist = chaospy.Uniform(lower=params[0], upper=params[1])

            elif 'norm' in dist_type.lower() and \
                 'log' not in dist_type.lower():
                polytype = 'hermite'
                dist = chaospy.Normal(mu=params[0], sigma=params[1])

            elif 'gamma' in dist_type.lower():
                polytype = 'laguerre'
                dist = chaospy.Gamma(shape=params[0],
                                     scale=params[1],
                                     shift=params[2])

            elif 'beta' in dist_type.lower():
                polytype = 'jacobi'
                dist = chaospy.Beta(alpha=params[0], beta=params[1],
                                    lower=params[2], upper=params[3])

            elif 'lognorm' in dist_type.lower():
                polytype = 'hermite'
                Mu = np.log(params[0]**2/np.sqrt(params[0]**2 + params[1]**2))
                Sigma = np.sqrt(np.log(1 + params[1]**2 / params[0]**2))
                dist = chaospy.LogNormal(mu=Mu, sigma=Sigma)

            elif 'expon' in dist_type.lower():
                polytype = 'arbitrary'
                dist = chaospy.Exponential(scale=params[0], shift=params[1])

            elif 'weibull' in dist_type.lower():
                polytype = 'arbitrary'
                dist = chaospy.Weibull(shape=params[0], scale=params[1],
                                       shift=params[2])

            else:
                message = (f"DistType {dist_type} for parameter"
                           f"{parIdx+1} is not available.")
                raise ValueError(message)

            if self.input_data_given or self.apce:
                polytype = 'arbitrary'

            # Store dists and poly_types
            orig_joints.append(dist)
            poly_types.append(polytype)
            all_dist_types.append(dist_type)

        # Prepare final output to return
        if None in all_dist_types:
            # Naive approach: Fit a gaussian kernel to the provided data
            Data = np.asarray(all_data)
            orig_space_dist = st.gaussian_kde(Data)
            self.prior_space = orig_space_dist
        else:
            orig_space_dist = chaospy.J(*orig_joints)
            self.prior_space = st.gaussian_kde(orig_space_dist.sample(10000))

        return orig_space_dist, poly_types

    # -------------------------------------------------------------------------
    def random_sampler(self, n_samples):
        """
        Samples the given raw data randomly.

        Parameters
        ----------
        n_samples : int
            Number of requested samples.

        Returns
        -------
        samples: array of shape (n_samples, n_params)
            The sampling locations in the input space.

        """
        samples = np.zeros((n_samples, self.ndim))

        for idxPa in range(self.ndim):
            # input_data given
            sample_size = len(self.raw_data[idxPa])
            randIdx = np.random.randint(0, sample_size, n_samples)
            samples[:, idxPa] = self.raw_data[idxPa, randIdx]

        return samples

    # -------------------------------------------------------------------------
    def pcm_sampler(self, max_deg):
        """
        Generates collocation points based on the root of the polynomial
        degrees.

        Parameters
        ----------
        max_deg : int
            Maximum degree defined by user.

        Returns
        -------
        opt_col_points: array of shape (n_samples, n_params)
            Collocation points.

        """

        raw_data = self.raw_data

        # Guess the closest degree to self.n_samples
        def M_uptoMax(deg):
            result = []
            for d in range(1, deg+1):
                result.append(math.factorial(self.ndim+d) //
                              (math.factorial(self.ndim) * math.factorial(d)))
            return np.array(result)

        guess_Deg = np.where(M_uptoMax(max_deg) > self.n_samples)[0][0]

        c_points = np.zeros((guess_Deg+1, self.ndim))

        def PolynomialPa(parIdx):
            return apoly_construction(self.raw_data[parIdx], max_deg)

        for i in range(self.ndim):
            poly_coeffs = PolynomialPa(i)[guess_Deg+1][::-1]
            c_points[:, i] = np.trim_zeros(np.roots(poly_coeffs))

        #  Construction of optimal integration points
        Prod = itertools.product(np.arange(1, guess_Deg+2), repeat=self.ndim)
        sort_dig_unique_combos = np.array(list(filter(lambda x: x, Prod)))

        # Ranking relatively mean
        Temp = np.empty(shape=[0, guess_Deg+1])
        for j in range(self.ndim):
            s = abs(c_points[:, j]-np.mean(raw_data[j]))
            Temp = np.append(Temp, [s], axis=0)
        temp = Temp.T

        index_CP = np.sort(temp, axis=0)
        sort_cpoints = np.empty((0, guess_Deg+1))

        for j in range(self.ndim):
            sort_cp = c_points[index_CP[:, j], j]
            sort_cpoints = np.vstack((sort_cpoints, sort_cp))

        # Mapping of Combination to Cpoint Combination
        sort_unique_combos = np.empty(shape=[0, self.ndim])
        for i in range(len(sort_dig_unique_combos)):
            sort_un_comb = []
            for j in range(self.ndim):
                SortUC = sort_cpoints[j, sort_dig_unique_combos[i, j]-1]
                sort_un_comb.append(SortUC)
                sort_uni_comb = np.asarray(sort_un_comb)
            sort_unique_combos = np.vstack((sort_unique_combos, sort_uni_comb))

        # Output the collocation points
        if self.sampling_method.lower() == 'lscm':
            opt_col_points = sort_unique_combos
        else:
            opt_col_points = sort_unique_combos[0:self.n_samples]

        return opt_col_points

    # -------------------------------------------------------------------------
    def transform(self, X, params=None):
        """
        Transform the samples via either a Rosenblatt or an isoprobabilistic
        transformation.

        Parameters
        ----------
        X : array of shape (n_samples,n_params)
            Samples to be transformed.

        Returns
        -------
        tr_X: array of shape (n_samples,n_params)
            Transformed samples.

        """
        if self.InputObj.Rosenblatt:
            self.origJDist, _ = self.build_dist(False)
            tr_X = self.origJDist.inv(self.JDist.fwd(X.T)).T
        else:
            # Transform samples via an isoprobabilistic transformation
            n_samples, n_params = X.shape
            Inputs = self.InputObj
            origJDist = self.JDist
            poly_types = self.poly_types

            disttypes = []
            for par_i in range(n_params):
                disttypes.append(Inputs.Marginals[par_i].dist_type)

            # Pass non-transformed X, if arbitrary PCE is selected.
            if None in disttypes or self.input_data_given or self.apce:
                return X

            cdfx = np.zeros((X.shape))
            tr_X = np.zeros((X.shape))

            for par_i in range(n_params):

                # Extract the parameters of the original space
                disttype = disttypes[par_i]
                if disttype is not None:
                    dist = origJDist[par_i]
                else:
                    dist = None
                polytype = poly_types[par_i]
                cdf = np.vectorize(lambda x: dist.cdf(x))

                # Extract the parameters of the transformation space based on
                # polyType
                if polytype == 'legendre' or disttype == 'uniform':
                    # Generate Y_Dists based
                    params_Y = [-1, 1]
                    dist_Y = st.uniform(loc=params_Y[0],
                                        scale=params_Y[1]-params_Y[0])
                    inv_cdf = np.vectorize(lambda x: dist_Y.ppf(x))

                elif polytype == 'hermite' or disttype == 'norm':
                    params_Y = [0, 1]
                    dist_Y = st.norm(loc=params_Y[0], scale=params_Y[1])
                    inv_cdf = np.vectorize(lambda x: dist_Y.ppf(x))

                elif polytype == 'laguerre' or disttype == 'gamma':
                    params_Y = [1, params[1]]
                    dist_Y = st.gamma(loc=params_Y[0], scale=params_Y[1])
                    inv_cdf = np.vectorize(lambda x: dist_Y.ppf(x))

                # Compute CDF_x(X)
                cdfx[:, par_i] = cdf(X[:, par_i])

                # Compute invCDF_y(cdfx)
                tr_X[:, par_i] = inv_cdf(cdfx[:, par_i])

        return tr_X

    # -------------------------------------------------------------------------
    def fit_dist(self, y):
        """
        Fits the known distributions to the data.

        Parameters
        ----------
        y : array of shape (n_samples)
            Data to be fitted.

        Returns
        -------
        sel_dist: string
            Selected distribution type from `lognorm`, `norm`, `uniform` or
            `expon`.
        params : list
            Parameters corresponding to the selected distibution type.

        """
        dist_results = []
        params = {}
        dist_names = ['lognorm', 'norm', 'uniform', 'expon']
        for dist_name in dist_names:
            dist = getattr(st, dist_name)

            try:
                if dist_name != 'lognorm':
                    param = dist.fit(y)
                else:
                    param = dist.fit(np.exp(y), floc=0)
            except:
                param = dist.fit(y)

            params[dist_name] = param
            # Applying the Kolmogorov-Smirnov test
            D, p = st.kstest(y, dist_name, args=param)
            dist_results.append((dist_name, D))

        # select the best fitted distribution
        sel_dist, D = (min(dist_results, key=lambda item: item[1]))

        if sel_dist == 'uniform':
            params[sel_dist] = [params[sel_dist][0], params[sel_dist][0] +
                                params[sel_dist][1]]
        if D < 0.05:
            return sel_dist, params[sel_dist]
        else:
            return None, None
