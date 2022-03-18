#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import warnings
import numpy as np
import math
import h5py
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import scipy as sp
from tqdm import tqdm
from sklearn.decomposition import PCA as sklearnPCA
import sklearn.linear_model as lm
from sklearn.gaussian_process import GaussianProcessRegressor
import sklearn.gaussian_process.kernels as kernels
import os
import sys
from joblib import Parallel, delayed

from .exp_designs import ExpDesigns
from .glexindex import glexindex
from .eval_rec_rule import eval_univ_basis
from .reg_fast_ard import RegressionFastARD
from .reg_fast_laplace import RegressionFastLaplace
from .bayes_linear import VBLinearRegression, EBLinearRegression
warnings.filterwarnings("ignore")
# Load the mplstyle
plt.style.use(os.path.join(os.path.split(__file__)[0],
                           '../', 'bayesvalidrox.mplstyle'))


class MetaModel:
    """
    Meta (surrogate) model

    This class trains a surrogate model. It accepts an input object (input_obj)
    containing the specification of the distributions for uncertain parameters
    and a model object with instructions on how to run the computational model.

    Attributes
    ----------
    input_obj : obj
        Input object with the information on the model input parameters.
    meta_model_type : str
        Surrogate model types. Three surrogate model types are supported:
        polynomial chaos expansion (`PCE`), arbitrary PCE (`aPCE`) and
        Gaussian process regression (`GPE`). Default is PCE.
    pce_reg_method : str
        PCE regression method to compute the coefficients. The following
        regression methods are available:

        1. OLS: Ordinary Least Square method
        2. BRR: Bayesian Ridge Regression
        3. LARS: Least angle regression
        4. ARD: Bayesian ARD Regression
        5. FastARD: Fast Bayesian ARD Regression
        6. VBL: Variational Bayesian Learning
        7. EBL: Emperical Bayesian Learning
        Default is `OLS`.
    pce_deg : int or list of int
        Polynomial degree(s). If a list is given, an adaptive algorithm is used
        to find the best degree with the lowest Leave-One-Out cross-validation
        (LOO) error (or the highest score=1-LOO). Default is `1`.
    pce_q_norm : float
        Hyperbolic (or q-norm) truncation for multi-indices of multivariate
        polynomials. Default is `1.0`.
    dim_red_method : str
        Dimensionality reduction method for the output space. The available
        method is based on principal component analysis (PCA). The Default is
        `'no'`. There are two ways to select number of components: use
        percentage of the explainable variance threshold (between 0 and 100)
        (Option A) or direct prescription of components' number (Option B):

            >>> MetaModelOpts.dim_red_method = 'PCA'
            >>> MetaModelOpts.var_pca_threshold = 99.999  # Option A
            >>> MetaModelOpts.n_pca_components = 12 # Option B

    verbose : bool
        Prints summary of the regression results. Default is `False`.

    Note
    -------
    To define the sampling methods and the training set, an experimental design
    instance shall be defined. This can be done by:

    >>> MetaModelOpts.add_ExpDesign()

    Two experimental design schemes are supported: one-shot (`normal`) and
    adaptive sequential (`sequential`) designs.
    For experimental design refer to `ExpDesigns`.

    """

    def __init__(self, input_obj, meta_model_type='PCE', pce_reg_method='OLS',
                 pce_deg=1, pce_q_norm=1.0, dim_red_method='no',
                 verbose=False):

        self.input_obj = input_obj
        self.meta_model_type = meta_model_type
        self.pce_reg_method = pce_reg_method
        self.pce_deg = pce_deg
        self.pce_q_norm = pce_q_norm
        self.dim_red_method = dim_red_method
        self.verbose = False

    # -------------------------------------------------------------------------
    def create_metamodel(self, Model):
        """
        Starts the training of the meta-model for the model objects containg
         the given computational model.

        Parameters
        ----------
        Model : obj
            Model object.

        Returns
        -------
        metamodel : obj
            The meta model object.

        """
        self.ModelObj = Model
        self.n_params = len(self.input_obj.Marginals)
        self.ExpDesignFlag = 'normal'
        # --- Prepare pce degree ---
        if self.meta_model_type.lower() == 'pce':
            if type(self.pce_deg) is not np.ndarray:
                self.pce_deg = np.array(self.pce_deg)

        if self.ExpDesign.method == 'sequential':
            from .sequential_design import SeqDesign
            seq_design = SeqDesign(self)
            metamodel = seq_design.train_seq_design(Model)

        elif self.ExpDesign.method == 'normal':
            self.ExpDesignFlag = 'normal'
            metamodel = self.train_norm_design(Model)

        else:
            raise Exception("The method for experimental design you requested"
                            " has not been implemented yet.")

        # Zip the model run directories
        if self.ModelObj.link_type.lower() == 'pylink':
            Model.zip_subdirs(Model.name, f'{Model.name}_')

        return metamodel

    # -------------------------------------------------------------------------
    def train_norm_design(self, Model, verbose=False):
        """
        This function loops over the outputs and each time step/point and fits
        the meta model.

        Parameters
        ----------
        Model : obj
            Model object.
        verbose : bool, optional
            Flag for a sequential design in silent mode. The default is False.

        Returns
        -------
        self: obj
            Meta-model object.

        """

        # Get the collocation points to run the forward model
        CollocationPoints, OutputDict = self.generate_ExpDesign(Model)

        # Initialize the nested dictionaries
        self.deg_dict = self.auto_vivification()
        self.q_norm_dict = self.auto_vivification()
        self.coeffs_dict = self.auto_vivification()
        self.basis_dict = self.auto_vivification()
        self.score_dict = self.auto_vivification()
        self.clf_poly = self.auto_vivification()
        self.gp_poly = self.auto_vivification()
        self.pca = self.auto_vivification()
        self.LCerror = self.auto_vivification()
        self.x_scaler = {}

        # Define the DegreeArray
        nSamples, ndim = CollocationPoints.shape
        self.DegreeArray = self.__select_degree(ndim, nSamples)

        # Generate all basis indices
        self.allBasisIndices = self.auto_vivification()
        for deg in self.DegreeArray:
            keys = self.allBasisIndices.keys()
            if deg not in np.fromiter(keys, dtype=float):
                # Generate the polynomial basis indices
                for qidx, q in enumerate(self.pce_q_norm):
                    basis_indices = self.create_basis_indices(degree=deg,
                                                              q_norm=q)
                    self.allBasisIndices[str(deg)][str(q)] = basis_indices

        # Evaluate the univariate polynomials on ExpDesign
        if self.meta_model_type.lower() != 'gpe':
            self.univ_p_val = self.univ_basis_vals(CollocationPoints)

        if 'x_values' in OutputDict:
            self.ExpDesign.x_values = OutputDict['x_values']
            del OutputDict['x_values']

        # --- Loop through data points and fit the surrogate ---
        if not verbose:
            print(f"\n>>>> Training the {self.meta_model_type} metamodel "
                  "started. <<<<<<\n")
            items = tqdm(OutputDict.items(), desc="Fitting regression")
        else:
            items = OutputDict.items()

        # For loop over the components/outputs
        for key, Output in items:

            # Dimensionality reduction with PCA, if specified
            if self.dim_red_method.lower() == 'pca':
                self.pca[key], target = self.pca_transformation(Output)
            else:
                target = Output

            # Parallel fit regression
            if self.meta_model_type.lower() == 'gpe':
                # Prepare the input matrix
                scaler = MinMaxScaler()
                X_S = scaler.fit_transform(CollocationPoints)

                self.x_scaler[key] = scaler

                out = Parallel(n_jobs=-1, prefer='threads')(
                    delayed(self.gaussian_process_emulator)(X_S, target[:, idx])
                    for idx in range(target.shape[1]))

                for idx in range(target.shape[1]):
                    self.gp_poly[key][f"y_{idx+1}"] = out[idx]

            else:
                out = Parallel(n_jobs=-1, prefer='threads')(
                    delayed(self.adaptive_regression)(CollocationPoints,
                                                      target[:, idx], idx)
                    for idx in range(target.shape[1]))

                for i in range(target.shape[1]):
                    # Create a dict to pass the variables
                    self.deg_dict[key][f"y_{i+1}"] = out[i]['degree']
                    self.q_norm_dict[key][f"y_{i+1}"] = out[i]['qnorm']
                    self.coeffs_dict[key][f"y_{i+1}"] = out[i]['coeffs']
                    self.basis_dict[key][f"y_{i+1}"] = out[i]['multi_indices']
                    self.score_dict[key][f"y_{i+1}"] = out[i]['LOOCVScore']
                    self.clf_poly[key][f"y_{i+1}"] = out[i]['clf_poly']
                    self.LCerror[key][f"y_{i+1}"] = out[i]['LCerror']

        if not verbose:
            print(f"\n>>>> Training the {self.meta_model_type} metamodel"
                  " sucessfully completed. <<<<<<\n")

        return self

    # -------------------------------------------------------------------------
    def create_basis_indices(self, degree, q_norm):
        """
        Creates set of selected multi-indices of multivariate polynomials for
        certain parameter numbers, polynomial degree, hyperbolic (or q-norm)
        truncation scheme.

        Parameters
        ----------
        degree : int
            Polynomial degree.
        q_norm : float
            hyperbolic (or q-norm) truncation.

        Returns
        -------
        basis_indices : array of shape (n_terms, n_params)
            Multi-indices of multivariate polynomials.

        """
        basis_indices = glexindex(start=0, stop=degree+1,
                                  dimensions=self.n_params,
                                  cross_truncation=q_norm,
                                  reverse=False, graded=True)
        return basis_indices

    # -------------------------------------------------------------------------
    def add_ExpDesign(self):
        """
        Instanciates experimental design object.

        Returns
        -------
        None.

        """
        self.ExpDesign = ExpDesigns(self.input_obj,
                                    meta_Model=self.meta_model_type)

    # -------------------------------------------------------------------------
    def generate_ExpDesign(self, Model):
        """
        Prepares the experimental design either by reading from the prescribed
        data or running simulations.

        Parameters
        ----------
        Model : obj
            Model object.

        Raises
        ------
        Exception
            If model sumulations are not provided properly.

        Returns
        -------
        ED_X_tr: array of shape (n_samples, n_params)
            Training samples transformed by an isoprobabilistic transformation.
        ED_Y: dict
            Model simulations (target) for all outputs.
        """
        ExpDesign = self.ExpDesign
        if self.ExpDesignFlag != 'sequential':
            # Read ExpDesign (training and targets) from the provided hdf5
            if ExpDesign.hdf5_file is not None:

                # Read hdf5 file
                f = h5py.File(ExpDesign.hdf5_file, 'r+')

                # Read EDX and pass it to ExpDesign object
                try:
                    ExpDesign.X = np.array(f["EDX/New_init_"])
                except KeyError:
                    ExpDesign.X = np.array(f["EDX/init_"])

                # Update number of initial samples
                ExpDesign.n_init_samples = ExpDesign.X.shape[0]

                # Read EDX and pass it to ExpDesign object
                out_names = self.ModelObj.Output.names
                ExpDesign.Y = {}

                # Extract x values
                try:
                    ExpDesign.Y["x_values"] = dict()
                    for varIdx, var in enumerate(out_names):
                        x = np.array(f[f"x_values/{var}"])
                        ExpDesign.Y["x_values"][var] = x
                except KeyError:
                    ExpDesign.Y["x_values"] = np.array(f["x_values"])

                # Store the output
                for varIdx, var in enumerate(out_names):
                    try:
                        y = np.array(f[f"EDY/{var}/New_init_"])
                    except KeyError:
                        y = np.array(f[f"EDY/{var}/init_"])
                    ExpDesign.Y[var] = y
                f.close()
            else:
                # Check if an old hdf5 file exists: if yes, rename it
                hdf5file = f'ExpDesign_{self.ModelObj.name}.hdf5'
                if os.path.exists(hdf5file):
                    os.rename(hdf5file, 'old_'+hdf5file)

        # ---- Prepare X samples ----
        ED_X, ED_X_tr = ExpDesign.generate_ED(ExpDesign.n_init_samples,
                                              ExpDesign.sampling_method,
                                              transform=True,
                                              max_pce_deg=np.max(self.pce_deg))
        ExpDesign.X = ED_X
        ExpDesign.collocationPoints = ED_X_tr
        self.bound_tuples = ExpDesign.bound_tuples

        # ---- Run simulations at X ----
        if not hasattr(ExpDesign, 'Y') or ExpDesign.Y is None:
            print('\n Now the forward model needs to be run!\n')
            ED_Y, up_ED_X = Model.run_model_parallel(ED_X)
            ExpDesign.X = up_ED_X
            self.ModelOutputDict = ED_Y
            ExpDesign.Y = ED_Y
        else:
            # Check if a dict has been passed.
            if type(ExpDesign.Y) is dict:
                self.ModelOutputDict = ExpDesign.Y
            else:
                raise Exception('Please provide either a dictionary or a hdf5'
                                'file to ExpDesign.hdf5_file argument.')

        return ED_X_tr, self.ModelOutputDict

    # -------------------------------------------------------------------------
    def univ_basis_vals(self, samples, n_max=None):
        """
        Evaluates univariate regressors along input directions.

        Parameters
        ----------
        samples : array of shape (n_samples, n_params)
            Samples.
        n_max : int, optional
            Maximum polynomial degree. The default is `None`.

        Returns
        -------
        univ_basis: array of shape (n_samples, n_params, n_max+1)
            All univariate regressors up to n_max.
        """
        # Extract information
        poly_types = self.ExpDesign.poly_types
        if samples.ndim != 2:
            samples = samples.reshape(1, len(samples))
        n_max = np.max(self.pce_deg) if n_max is None else n_max

        # Extract poly coeffs
        if self.ExpDesign.input_data_given or self.ExpDesign.apce:
            apolycoeffs = self.ExpDesign.polycoeffs
        else:
            apolycoeffs = None

        # Evaluate univariate basis
        univ_basis = eval_univ_basis(samples, n_max, poly_types, apolycoeffs)

        return univ_basis

    # -------------------------------------------------------------------------
    def create_psi(self, basis_indices, univ_p_val):
        """
        This function assemble the design matrix Psi from the given basis index
        set INDICES and the univariate polynomial evaluations univ_p_val.

        Parameters
        ----------
        basis_indices : array of shape (n_terms, n_params)
            Multi-indices of multivariate polynomials.
        univ_p_val : array of (n_samples, n_params, n_max+1)
            All univariate regressors up to `n_max`.

        Raises
        ------
        ValueError
            n_terms in arguments do not match.

        Returns
        -------
        psi : array of shape (n_samples, n_terms)
            Multivariate regressors.

        """
        # Check if BasisIndices is a sparse matrix
        sparsity = sp.sparse.issparse(basis_indices)
        if sparsity:
            basis_indices = basis_indices.toarray()

        # Initialization and consistency checks
        # number of input variables
        n_params = univ_p_val.shape[1]

        # Size of the experimental design
        n_samples = univ_p_val.shape[0]

        # number of basis terms
        n_terms = basis_indices.shape[0]

        # check that the variables have consistent sizes
        if n_params != basis_indices.shape[1]:
            raise ValueError("The shapes of basis_indices and univ_p_val don't"
                             " match!!")

        # Preallocate the Psi matrix for performance
        psi = np.ones((n_samples, n_terms))
        # Assemble the Psi matrix
        for m in range(basis_indices.shape[1]):
            aa = np.where(basis_indices[:, m] > 0)[0]
            try:
                basisIdx = basis_indices[aa, m]
                bb = np.reshape(univ_p_val[:, m, basisIdx], psi[:, aa].shape)
                psi[:, aa] = np.multiply(psi[:, aa], bb)
            except ValueError as err:
                raise err

        return psi

    # -------------------------------------------------------------------------
    def fit(self, X, y, basis_indices, reg_method=None):
        """
        Fit regression using the regression method provided.

        Parameters
        ----------
        X : array of shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.
        y : array of shape (n_samples,)
            Target values.
        basis_indices : array of shape (n_terms, n_params)
            Multi-indices of multivariate polynomials.
        reg_method : str, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        return_out_dict : Dict
            Fitted estimator, spareMulti-Index, sparseX and coefficients.

        """
        if reg_method is None:
            reg_method = self.pce_reg_method

        # Check if BasisIndices is a sparse matrix
        sparsity = sp.sparse.issparse(basis_indices)

        clf_poly = []
        compute_score = True if self.verbose else False

        #  inverse of the observed variance of the data
        if np.var(y) != 0:
            Lambda = 1 / np.var(y)
        else:
            Lambda = 1e-6

        # Bayes sparse adaptive aPCE
        if reg_method.lower() != 'ols':
            if reg_method.lower() == 'brr' or np.var(y) == 0:
                clf_poly = lm.BayesianRidge(n_iter=1000, tol=1e-7,
                                            fit_intercept=True,
                                            normalize=True,
                                            compute_score=compute_score,
                                            alpha_1=1e-04, alpha_2=1e-04,
                                            lambda_1=Lambda, lambda_2=Lambda)
                clf_poly.converged = True

            elif reg_method.lower() == 'ard':
                clf_poly = lm.ARDRegression(fit_intercept=True,
                                            normalize=True,
                                            compute_score=compute_score,
                                            n_iter=1000, tol=0.0001,
                                            alpha_1=1e-3, alpha_2=1e-3,
                                            lambda_1=Lambda, lambda_2=Lambda)

            elif reg_method.lower() == 'fastard':
                clf_poly = RegressionFastARD(fit_intercept=True,
                                             normalize=True,
                                             compute_score=compute_score,
                                             n_iter=300, tol=1e-10)

            elif reg_method.lower() == 'bcs':
                clf_poly = RegressionFastLaplace(fit_intercept=False,
                                                 n_iter=1000, tol=1e-7)

            elif reg_method.lower() == 'lars':
                clf_poly = lm.LassoLarsCV(fit_intercept=False)

            elif reg_method.lower() == 'sgdr':
                clf_poly = lm.SGDRegressor(fit_intercept=False,
                                           max_iter=5000, tol=1e-7)

            elif reg_method.lower() == 'omp':
                clf_poly = lm.OrthogonalMatchingPursuitCV(fit_intercept=False,
                                                          max_iter=10)

            elif reg_method.lower() == 'vbl':
                clf_poly = VBLinearRegression(fit_intercept=False)

            elif reg_method.lower() == 'ebl':
                clf_poly = EBLinearRegression(optimizer='em')

            # Fit
            clf_poly.fit(X, y)

            # Select the nonzero entries of coefficients
            # The first column must be kept (For mean calculations)
            nnz_idx = np.nonzero(clf_poly.coef_)[0]

            if len(nnz_idx) == 0 or nnz_idx[0] != 0:
                nnz_idx = np.insert(np.nonzero(clf_poly.coef_)[0], 0, 0)
                # Remove the zero entries for Bases and PSI if need be
                if sparsity:
                    sparse_basis_indices = basis_indices.toarray()[nnz_idx]
                else:
                    sparse_basis_indices = basis_indices[nnz_idx]
                sparse_X = X[:, nnz_idx]

                # Store the coefficients of the regression model
                clf_poly.fit(sparse_X, y)
                coeffs = clf_poly.coef_
            else:
                # This is for the case where all outputs are zero, thereby
                # all coefficients are zero
                if sparsity:
                    sparse_basis_indices = basis_indices.toarray()
                else:
                    sparse_basis_indices = basis_indices
                sparse_X = X
                coeffs = clf_poly.coef_

        # Ordinary least square method (OLS)
        else:
            if sparsity:
                sparse_basis_indices = basis_indices.toarray()
            else:
                sparse_basis_indices = basis_indices
            sparse_X = X

            X_T_X = np.dot(sparse_X.T, sparse_X)

            if np.linalg.cond(X_T_X) > 1e-12 and \
               np.linalg.cond(X_T_X) < 1 / sys.float_info.epsilon:
                # faster
                coeffs = sp.linalg.solve(X_T_X, np.dot(sparse_X.T, y))
            else:
                # stabler
                coeffs = np.dot(np.dot(np.linalg.pinv(X_T_X), sparse_X.T), y)

        # Create a dict to pass the outputs
        return_out_dict = dict()
        return_out_dict['clf_poly'] = clf_poly
        return_out_dict['spareMulti-Index'] = sparse_basis_indices
        return_out_dict['sparePsi'] = sparse_X
        return_out_dict['coeffs'] = coeffs
        return return_out_dict

    # --------------------------------------------------------------------------------------------------------
    def adaptive_regression(self, ED_X, ED_Y, varIdx, verbose=False):
        """
        Adaptively fits the PCE model by comparing the scores of different
        degrees and q-norm.

        Parameters
        ----------
        ED_X : array of shape (n_samples, n_params)
            Experimental design.
        ED_Y : array of shape (n_samples,)
            Target values, i.e. simulation results for the Experimental design.
        varIdx : int
            Index of the output.
        verbose : bool, optional
            Print out summary. The default is False.

        Returns
        -------
        returnVars : Dict
            Fitted estimator, best degree, best q-norm, LOOCVScore and
            coefficients.

        """

        NrSamples, n_params = ED_X.shape
        # Initialization
        qAllCoeffs, AllCoeffs = {}, {}
        qAllIndices_Sparse, AllIndices_Sparse = {}, {}
        qAllclf_poly, Allclf_poly = {}, {}
        qAllnTerms, AllnTerms = {}, {}
        qAllLCerror, AllLCerror = {}, {}

        # Extract degree array and qnorm array
        DegreeArray = np.array([*self.allBasisIndices], dtype=int)
        qnorm = [*self.allBasisIndices[str(int(DegreeArray[0]))]]

        # Some options for EarlyStop
        errorIncreases = False
        # Stop degree, if LOO error does not decrease n_checks_degree times
        n_checks_degree = 3
        # Stop qNorm, if criterion isn't fulfilled n_checks_qNorm times
        n_checks_qNorm = 2
        nqnorms = len(qnorm)
        qNormEarlyStop = True
        if nqnorms < n_checks_qNorm+1:
            qNormEarlyStop = False

        # =====================================================================
        # basis adaptive polynomial chaos: repeat the calculation by increasing
        # polynomial degree until the highest accuracy is reached
        # =====================================================================
        # For each degree check all q-norms and choose the best one
        scores = -np.inf * np.ones(DegreeArray.shape[0])
        qNormScores = -np.inf * np.ones(nqnorms)

        for degIdx, deg in enumerate(DegreeArray):

            for qidx, q in enumerate(qnorm):

                # Extract the polynomial basis indices from the pool of
                # allBasisIndices
                BasisIndices = self.allBasisIndices[str(deg)][str(q)]

                # Assemble the Psi matrix
                Psi = self.create_psi(BasisIndices, self.univ_p_val)

                # Calulate the cofficients of the meta model
                outs = self.fit(Psi, ED_Y, BasisIndices)

                # Calculate and save the score of LOOCV
                score, LCerror = self.corr_loocv_error(outs['clf_poly'],
                                                       outs['sparePsi'],
                                                       outs['coeffs'],
                                                       ED_Y)

                # Check the convergence of noise for FastARD
                if self.pce_reg_method == 'FastARD' and \
                   outs['clf_poly'].alpha_ < np.finfo(np.float32).eps:
                    score = -np.inf

                qNormScores[qidx] = score
                qAllCoeffs[str(qidx+1)] = outs['coeffs']
                qAllIndices_Sparse[str(qidx+1)] = outs['spareMulti-Index']
                qAllclf_poly[str(qidx+1)] = outs['clf_poly']
                qAllnTerms[str(qidx+1)] = BasisIndices.shape[0]
                qAllLCerror[str(qidx+1)] = LCerror

                # EarlyStop check
                # if there are at least n_checks_qNorm entries after the
                # best one, we stop
                if qNormEarlyStop and \
                   sum(np.isfinite(qNormScores)) > n_checks_qNorm:
                    # If the error has increased the last two iterations, stop!
                    qNormScores_nonInf = qNormScores[np.isfinite(qNormScores)]
                    deltas = np.sign(np.diff(qNormScores_nonInf))
                    if sum(deltas[-n_checks_qNorm+1:]) == 2:
                        # stop the q-norm loop here
                        break
                if np.var(ED_Y) == 0:
                    break

            # Store the score in the scores list
            best_q = np.nanargmax(qNormScores)
            scores[degIdx] = qNormScores[best_q]

            AllCoeffs[str(degIdx+1)] = qAllCoeffs[str(best_q+1)]
            AllIndices_Sparse[str(degIdx+1)] = qAllIndices_Sparse[str(best_q+1)]
            Allclf_poly[str(degIdx+1)] = qAllclf_poly[str(best_q+1)]
            AllnTerms[str(degIdx+1)] = qAllnTerms[str(best_q+1)]
            AllLCerror[str(degIdx+1)] = qAllLCerror[str(best_q+1)]

            # Check the direction of the error (on average):
            # if it increases consistently stop the iterations
            if len(scores[scores != -np.inf]) > n_checks_degree:
                scores_nonInf = scores[scores != -np.inf]
                ss = np.sign(scores_nonInf - np.max(scores_nonInf))
                # ss<0 error decreasing
                errorIncreases = np.sum(np.sum(ss[-2:])) <= -1*n_checks_degree

            if errorIncreases:
                break

            # Check only one degree, if target matrix has zero variance
            if np.var(ED_Y) == 0:
                break

        # ------------------ Summary of results ------------------
        # Select the one with the best score and save the necessary outputs
        best_deg = np.nanargmax(scores)+1
        coeffs = AllCoeffs[str(best_deg)]
        basis_indices = AllIndices_Sparse[str(best_deg)]
        clf_poly = Allclf_poly[str(best_deg)]
        LOOCVScore = np.nanmax(scores)
        P = AllnTerms[str(best_deg)]
        LCerror = AllLCerror[str(best_deg)]
        degree = DegreeArray[np.nanargmax(scores)]
        qnorm = float(qnorm[best_q])

        # ------------------ Print out Summary of results ------------------
        if self.verbose:
            # Create PSI_Sparse by removing redundent terms
            nnz_idx = np.nonzero(coeffs)[0]
            BasisIndices_Sparse = basis_indices[nnz_idx]

            print(f'Output variable {varIdx+1}:')
            print('The estimation of PCE coefficients converged at polynomial '
                  f'degree {DegreeArray[best_deg-1]} with '
                  f'{len(BasisIndices_Sparse)} terms (Sparsity index = '
                  f'{round(len(BasisIndices_Sparse)/P, 3)}).')

            print(f'Final ModLOO error estimate: {1-max(scores):.3e}')
            print('\n'+'-'*50)

        if verbose:
            print('='*50)
            print(' '*10 + ' Summary of results ')
            print('='*50)

            print("scores:\n", scores)
            print("Best score's degree:", self.DegreeArray[best_deg-1])
            print("NO. of terms:", len(basis_indices))
            print("Sparsity index:", round(len(basis_indices)/P, 3))
            print("Best Indices:\n", basis_indices)

            if self.pce_reg_method in ['BRR', 'ARD']:
                fig, ax = plt.subplots(figsize=(12, 10))
                plt.title("Marginal log-likelihood")
                plt.plot(clf_poly.scores_, color='navy', linewidth=2)
                plt.ylabel("Score")
                plt.xlabel("Iterations")
                if self.pce_reg_method.lower() == 'bbr':
                    text = f"$\\alpha={clf_poly.alpha_:.1f}$\n"
                    f"$\\lambda={clf_poly.lambda_:.3f}$\n"
                    f"$L={clf_poly.scores_[-1]:.1f}$"
                else:
                    text = f"$\\alpha={clf_poly.alpha_:.1f}$\n$"
                    f"\\L={clf_poly.scores_[-1]:.1f}$"

                plt.text(0.75, 0.5, text, fontsize=18, transform=ax.transAxes)
                plt.show()
            print('='*80)

        # Create a dict to pass the outputs
        returnVars = dict()
        returnVars['clf_poly'] = clf_poly
        returnVars['degree'] = degree
        returnVars['qnorm'] = qnorm
        returnVars['coeffs'] = coeffs
        returnVars['multi_indices'] = basis_indices
        returnVars['LOOCVScore'] = LOOCVScore
        returnVars['LCerror'] = LCerror

        return returnVars

    # -------------------------------------------------------------------------
    def corr_loocv_error(self, clf, psi, coeffs, y):
        """
        Calculates the corrected LOO error for regression on regressor
        matrix `psi` that generated the coefficients based on [1] and [2].

        [1] Blatman, G., 2009. Adaptive sparse polynomial chaos expansions for
            uncertainty propagation and sensitivity analysis (Doctoral
            dissertation, Clermont-Ferrand 2).

        [2] Blatman, G. and Sudret, B., 2011. Adaptive sparse polynomial chaos
            expansion based on least angle regression. Journal of computational
            Physics, 230(6), pp.2345-2367.

        Parameters
        ----------
        clf : object
            Fitted estimator.
        psi : array of shape (n_samples, n_features)
            The multivariate orthogonal polynomials (regressor).
        coeffs : array-like of shape (n_features,)
            Estimated cofficients.
        y : array of shape (n_samples,)
            Target values.

        Returns
        -------
        Q_2 : float
            LOOCV Validation score (1-LOOCV erro).
        residual : array of shape (n_samples,)
            Residual values (y - predicted targets).

        """
        psi = np.array(psi, dtype=float)

        # Create PSI_Sparse by removing redundent terms
        nnz_idx = np.nonzero(coeffs)[0]
        if len(nnz_idx) == 0:
            nnz_idx = [0]
        psi_sparse = psi[:, nnz_idx]

        # NrCoeffs of aPCEs
        P = len(nnz_idx)
        # NrEvaluation (Size of experimental design)
        N = psi.shape[0]

        # Build the projection matrix
        PsiTPsi = np.dot(psi_sparse.T, psi_sparse)

        if np.linalg.cond(PsiTPsi) > 1e-12 and \
           np.linalg.cond(PsiTPsi) < 1/sys.float_info.epsilon:
            # faster
            M = sp.linalg.solve(PsiTPsi,
                                sp.sparse.eye(PsiTPsi.shape[0]).toarray())
        else:
            # stabler
            M = np.linalg.pinv(PsiTPsi)

        # h factor (the full matrix is not calculated explicitly,
        # only the trace is, to save memory)
        PsiM = np.dot(psi_sparse, M)

        h = np.sum(np.multiply(PsiM, psi_sparse), axis=1, dtype=np.float128)

        # ------ Calculate Error Loocv for each measurement point ----
        # Residuals
        if isinstance(clf, list):
            residual = np.dot(psi, coeffs) - y
        else:
            residual = clf.predict(psi) - y

        # Variance
        varY = np.var(y)

        if varY == 0:
            normEmpErr = 0
            ErrLoo = 0
            LCerror = np.zeros((y.shape))
        else:
            normEmpErr = np.mean(residual**2)/varY

            # LCerror = np.divide(residual, (1-h))
            LCerror = residual / (1-h)[:, np.newaxis]
            ErrLoo = np.mean(np.square(LCerror)) / varY
            # if there are NaNs, just return an infinite LOO error (this
            # happens, e.g., when a strongly underdetermined problem is solved)
            if np.isnan(ErrLoo):
                ErrLoo = np.inf

        # Corrected Error for over-determined system
        trM = np.trace(M)
        if trM < 0 or abs(trM) > 1e6:
            trM = np.trace(np.linalg.pinv(np.dot(psi.T, psi)))

        # Over-determined system of Equation
        if N > P:
            T_factor = N/(N-P) * (1 + trM)

        # Under-determined system of Equation
        else:
            T_factor = np.inf

        CorrectedErrLoo = ErrLoo * T_factor

        Q_2 = 1 - CorrectedErrLoo

        return Q_2, residual

    # -------------------------------------------------------------------------
    def pca_transformation(self, Output):
        """
        Transforms the targets (outputs) via Principal Component Analysis

        Parameters
        ----------
        Output : array of shape (n_samples,)
            Target values.

        Returns
        -------
        pca : obj
            Fitted sklearnPCA object.
        OutputMatrix : array of shape (n_samples,)
            Transformed target values.

        """
        # Transform via Principal Component Analysis
        if hasattr(self, 'var_pca_threshold'):
            var_pca_threshold = self.var_pca_threshold
        else:
            var_pca_threshold = 100.0
        n_samples, n_features = Output.shape

        if hasattr(self, 'n_pca_components'):
            n_pca_components = self.n_pca_components
        else:
            # Instantiate and fit sklearnPCA object
            covar_matrix = sklearnPCA(n_components=None)
            covar_matrix.fit(Output)
            var = np.cumsum(np.round(covar_matrix.explained_variance_ratio_,
                                     decimals=5)*100)
            # Find the number of components to explain self.varPCAThreshold of
            # variance
            try:
                n_components = np.where(var >= var_pca_threshold)[0][0] + 1
            except IndexError:
                n_components = min(n_samples, n_features)

            n_pca_components = min(n_samples, n_features, n_components)

        # Print out a report
        print()
        print('-' * 50)
        print(f"PCA transformation is performed with {n_pca_components}"
              " components.")
        print('-' * 50)
        print()

        # Fit and transform with the selected number of components
        pca = sklearnPCA(n_components=n_pca_components,
                         svd_solver='randomized')
        OutputMatrix = pca.fit_transform(Output)

        return pca, OutputMatrix

    # -------------------------------------------------------------------------
    def gaussian_process_emulator(self, X, y, nug_term=None, autoSelect=False,
                                  varIdx=None):
        """
        Fits a Gaussian Process Emulator to the target given the training
         points.

        Parameters
        ----------
        X : array of shape (n_samples, n_params)
            Training points.
        y : array of shape (n_samples,)
            Target values.
        nug_term : float, optional
            Nugget term. The default is None, i.e. variance of y.
        autoSelect : bool, optional
            Loop over some kernels and select the best. The default is False.
        varIdx : int, optional
            The index number. The default is None.

        Returns
        -------
        gp : object
            Fitted estimator.

        """

        nug_term = nug_term if nug_term else np.var(y)

        Kernels = [nug_term * kernels.RBF(length_scale=1.0,
                                          length_scale_bounds=(1e-25, 1e15)),
                   nug_term * kernels.RationalQuadratic(length_scale=0.2,
                                                        alpha=1.0),
                   nug_term * kernels.Matern(length_scale=1.0,
                                             length_scale_bounds=(1e-15, 1e5),
                                             nu=1.5)]

        # Automatic selection of the kernel
        if autoSelect:
            gp = {}
            BME = []
            for i, kernel in enumerate(Kernels):
                gp[i] = GaussianProcessRegressor(kernel=kernel,
                                                 n_restarts_optimizer=3,
                                                 normalize_y=False)

                # Fit to data using Maximum Likelihood Estimation
                gp[i].fit(X, y)

                # Store the MLE as BME score
                BME.append(gp[i].log_marginal_likelihood())

            gp = gp[np.argmax(BME)]

        else:
            gp = GaussianProcessRegressor(kernel=Kernels[0],
                                          n_restarts_optimizer=3,
                                          normalize_y=False)
            gp.fit(X, y)

        # Compute score
        if varIdx is not None:
            Score = gp.score(X, y)
            print('-'*50)
            print(f'Output variable {varIdx}:')
            print('The estimation of GPE coefficients converged,')
            print(f'with the R^2 score: {Score:.3f}')
            print('-'*50)

        return gp

    # -------------------------------------------------------------------------
    def eval_metamodel(self, samples=None, nsamples=None,
                       sampling_method='random', return_samples=False):
        """
        Evaluates meta-model at the requested samples. One can also generate
        nsamples.

        Parameters
        ----------
        samples : array of shape (n_samples, n_params), optional
            Samples to evaluate meta-model at. The default is None.
        nsamples : int, optional
            Number of samples to generate, if no `samples` is provided. The
            default is None.
        sampling_method : str, optional
            Type of sampling, if no `samples` is provided. The default is
            'random'.
        return_samples : bool, optional
            Retun samples, if no `samples` is provided. The default is False.

        Returns
        -------
        mean_pred : dict
            Mean of the predictions.
        std_pred : dict
            Standard deviatioon of the predictions.
        """
        if self.meta_model_type.lower() == 'gpe':
            model_dict = self.gp_poly
        else:
            model_dict = self.coeffs_dict

        if samples is None:
            if nsamples is None:
                self.n_samples = 100000
            else:
                self.n_samples = nsamples

            samples = self.ExpDesign.generate_samples(self.n_samples,
                                                      sampling_method)
        else:
            self.samples = samples
            self.n_samples = len(samples)

        # Transform samples
        samples = self.ExpDesign.transform(samples)

        if self.meta_model_type.lower() != 'gpe':
            univ_p_val = self.univ_basis_vals(samples,
                                              n_max=np.max(self.pce_deg))

        mean_pred = {}
        std_pred = {}

        # Loop over outputs
        for ouput, values in model_dict.items():

            mean = np.zeros((len(samples), len(values)))
            std = np.zeros((len(samples), len(values)))
            idx = 0
            for in_key, InIdxValues in values.items():

                # Perdiction with GPE
                if self.meta_model_type.lower() == 'gpe':
                    X_T = self.x_scaler[ouput].transform(samples)
                    gp = self.gp_poly[ouput][in_key]
                    y_mean, y_std = gp.predict(X_T, return_std=True)

                else:
                    # Perdiction with PCE or pcekriging
                    # Assemble Psi matrix
                    psi = self.create_psi(self.basis_dict[ouput][in_key],
                                          univ_p_val)
                    # Perdiction
                    try:
                        # with error bar
                        clf_poly = self.clf_poly[ouput][in_key]
                        y_mean, y_std = clf_poly.predict(psi, return_std=True)

                    except:
                        # without error bar
                        coeffs = self.coeffs_dict[ouput][in_key]
                        y_mean = np.dot(psi, coeffs)
                        y_std = np.zeros_like(y_mean)

                mean[:, idx] = y_mean
                std[:, idx] = y_std
                idx += 1

            if self.dim_red_method.lower() == 'pca':
                PCA = self.pca[ouput]
                mean_pred[ouput] = PCA.mean_ + np.dot(mean, PCA.components_)
                std_pred[ouput] = np.sqrt(np.dot(std**2, PCA.components_**2))
            else:
                mean_pred[ouput] = mean
                std_pred[ouput] = std

        if return_samples:
            return mean_pred, std_pred, samples
        else:
            return mean_pred, std_pred

    # -------------------------------------------------------------------------
    def create_model_error(self, X, y, name='Calib'):
        """
        Fits a GPE-based model error.

        Parameters
        ----------
        X : array of shape (n_outputs, n_inputs)
            Input array. It can contain any forcing inputs or coordinates of
             extracted data.
        y : array of shape (n_outputs,)
            The model response for the MAP parameter set.
        name : str, optional
            Calibration or validation. The default is `'Calib'`.

        Returns
        -------
        self: object
            Self object.

        """
        Model = self.ModelObj
        outputNames = Model.Output.Names
        self.errorRegMethod = 'GPE'
        self.errorclf_poly = self.auto_vivification()
        self.errorScale = self.auto_vivification()

        # Read data
        MeasuredData = Model.read_observation(case=name)

        # Fitting GPR based bias model
        for out in outputNames:
            nan_idx = ~np.isnan(MeasuredData[out])
            # Select data
            try:
                data = MeasuredData[out].values[nan_idx]
            except AttributeError:
                data = MeasuredData[out][nan_idx]

            # Prepare the input matrix
            scaler = MinMaxScaler()
            delta = data  # - y[out][0]
            BiasInputs = np.hstack((X[out], y[out].reshape(-1, 1)))
            X_S = scaler.fit_transform(BiasInputs)
            gp = self.gaussian_process_emulator(X_S, delta)

            self.errorScale[out]["y_1"] = scaler
            self.errorclf_poly[out]["y_1"] = gp

        return self

    # -------------------------------------------------------------------------
    def eval_model_error(self, X, y_pred):
        """
        Evaluates the error model.

        Parameters
        ----------
        X : array
            Inputs.
        y_pred : dict
            Predictions.

        Returns
        -------
        mean_pred : dict
            Mean predition of the GPE-based error model.
        std_pred : dict
            standard deviation of the GPE-based error model.

        """
        mean_pred = {}
        std_pred = {}

        for Outkey, ValuesDict in self.errorclf_poly.items():

            pred_mean = np.zeros_like(y_pred[Outkey])
            pred_std = np.zeros_like(y_pred[Outkey])

            for Inkey, InIdxValues in ValuesDict.items():

                gp = self.errorclf_poly[Outkey][Inkey]
                scaler = self.errorScale[Outkey][Inkey]

                # Transform Samples using scaler
                for j, pred in enumerate(y_pred[Outkey]):
                    BiasInputs = np.hstack((X[Outkey], pred.reshape(-1, 1)))
                    Samples_S = scaler.transform(BiasInputs)
                    y_hat, y_std = gp.predict(Samples_S, return_std=True)
                    pred_mean[j] = y_hat
                    pred_std[j] = y_std
                    # pred_mean[j] += pred

            mean_pred[Outkey] = pred_mean
            std_pred[Outkey] = pred_std

        return mean_pred, std_pred

    # -------------------------------------------------------------------------
    class auto_vivification(dict):
        """
        Implementation of perl's AutoVivification feature.

        Source: https://stackoverflow.com/a/651879/18082457
        """

        def __getitem__(self, item):
            try:
                return dict.__getitem__(self, item)
            except KeyError:
                value = self[item] = type(self)()
                return value

    # -------------------------------------------------------------------------
    def __select_degree(self, ndim, nSamples):
        """
        Selects degree based on the number of samples and parameters in the
        sequential design.

        Parameters
        ----------
        ndim : TYPE
            DESCRIPTION.
        nSamples : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        # Define the DegreeArray
        max_deg = np.max(self.pce_deg)
        min_Deg = np.min(self.pce_deg)
        nitr = nSamples - self.ExpDesign.n_init_samples

        # Check q-norm
        if not np.isscalar(self.pce_q_norm):
            self.pce_q_norm = np.array(self.pce_q_norm)
        else:
            self.pce_q_norm = np.array([self.pce_q_norm])

        def M_uptoMax(maxDeg):
            n_combo = np.zeros(maxDeg)
            for i, d in enumerate(range(1, maxDeg+1)):
                n_combo[i] = math.factorial(ndim+d)
                n_combo[i] /= math.factorial(ndim) * math.factorial(d)
            return n_combo

        if self.ExpDesignFlag != 'sequential':
            degNew = max_deg
        else:
            d = nitr if nitr != 0 and self.n_params > 5 else 1
            min_index = np.argmin(abs(M_uptoMax(max_deg)-ndim*nSamples*d))
            degNew = range(1, max_deg+1)[min_index]

        if degNew > min_Deg and self.pce_reg_method.lower() != 'fastard':
            DegreeArray = np.arange(min_Deg, degNew+1)
        else:
            DegreeArray = np.array([degNew])

        return DegreeArray
