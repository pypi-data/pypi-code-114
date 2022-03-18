#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 09:21:18 2022

@author: farid
"""
import numpy as np
from scipy import stats, signal, linalg, sparse
from scipy.spatial import distance
from copy import deepcopy, copy
import tqdm
import scipy.optimize as opt
from sklearn.metrics import mean_squared_error
import multiprocessing
import matplotlib.pyplot as plt
import sys
import os
import seaborn as sns

from .exploration import Exploration


class SeqDesign():
    """ Sequential experimental design
    This class provieds method for trainig the meta-model in an iterative
    manners.
    The main method to execute the task is `train_seq_design`, which
     recieves a model object and returns the trained metamodel.
    """

    def __init__(self, MetaModel):
        self.MetaModel = MetaModel
        self.Model = MetaModel.ModelObj

    # -------------------------------------------------------------------------
    def train_seq_design(self, Model):
        """
        Starts the adaptive sequential design for refining the surrogate model
        by selecting training points in a sequential manner.

        Parameters
        ----------
        Model : object
            An object containing all model specifications.

        Returns
        -------
        PCEModel : object
            Meta model object.

        """
        MetaModel = self.MetaModel
        self.Model = MetaModel.ModelObj

        # Initialization
        errorIncreases = False
        MetaModel.SeqModifiedLOO = {}
        MetaModel.seqValidError = {}
        MetaModel.SeqBME = {}
        MetaModel.SeqKLD = {}
        MetaModel.SeqDistHellinger = {}
        MetaModel.seqRMSEMean = {}
        MetaModel.seqRMSEStd = {}
        MetaModel.seqMinDist = []
        pce = True if MetaModel.meta_model_type.lower() != 'gpe' else False
        mc_ref = True if hasattr(Model, 'MCReference') else False
        if mc_ref:
            Model.read_mc_reference()

        if not hasattr(MetaModel, 'valid_likelihoods'):
            MetaModel.valid_samples = []
            MetaModel.valid_model_runs = []
            MetaModel.valid_likelihoods = []

        # Get the parameters
        max_n_samples = MetaModel.ExpDesign.n_max_samples
        mod_LOO_threshold = MetaModel.ExpDesign.mod_LOO_threshold
        n_canddidate = MetaModel.ExpDesign.n_canddidate
        post_snapshot = MetaModel.ExpDesign.post_snapshot
        n_replication = MetaModel.ExpDesign.n_replication

        # Handle if only one UtilityFunctions is provided
        if not isinstance(MetaModel.ExpDesign.util_func, list):
            util_func = [MetaModel.ExpDesign.util_func]

        # Read observations or MCReference
        if len(Model.observations) != 0:
            self.observations = self.Model.read_observation()
        # ---------- Initial PCEModel ----------
        PCEModel = MetaModel.train_norm_design(Model)
        initPCEModel = deepcopy(PCEModel)

        # TODO: Loop over outputs
        OutputName = Model.Output.names

        # Estimation of the integral via Monte Varlo integration
        obs_data = self.observations

        # Check if data is provided
        TotalSigma2 = np.empty((0, 1))
        if len(obs_data) != 0 and hasattr(PCEModel, 'Discrepancy'):
            # ------ Prepare diagonal enteries for co-variance matrix ---------
            for keyIdx, key in enumerate(Model.Output.names):
                # optSigma = 'B'
                sigma2 = np.array(PCEModel.Discrepancy.parameters[key])
                TotalSigma2 = np.append(TotalSigma2, sigma2)

            # Calculate the initial BME
            out = self.__BME_Calculator(initPCEModel, obs_data, TotalSigma2)
            initBME, initKLD, initPosterior, initDistHellinger = out
            print("\nInitial BME:", initBME)
            print("Initial KLD:", initKLD)

            # Posterior snapshot (initial)
            if post_snapshot:
                MAP = PCEModel.ExpDesign.max_a_post
                parNames = PCEModel.ExpDesign.par_names
                print('Posterior snapshot (initial) is being plotted...')
                self.__posteriorPlot(initPosterior, MAP, parNames,
                                   'SeqPosterior_init')

        # Check the convergence of the Mean & Std
        if mc_ref and pce:
            initRMSEMean, initRMSEStd = self.__error_Mean_Std()
            print(f"Initial Mean and Std error: {initRMSEMean}, {initRMSEStd}")

        # Read the initial experimental design
        Xinit = initPCEModel.ExpDesign.X
        initTotalNSamples = len(PCEModel.ExpDesign.X)
        initYprev = initPCEModel.ModelOutputDict
        initLCerror = initPCEModel.LCerror

        # Read the initial ModifiedLOO
        if pce:
            Scores_all, varExpDesignY = [], []
            for OutName in OutputName:
                y = initPCEModel.ExpDesign.Y[OutName]
                Scores_all.append(list(
                    initPCEModel.score_dict[OutName].values()))
                if PCEModel.dim_red_method.lower() == 'pca':
                    pca = PCEModel.pca[OutName]
                    components = pca.transform(y)
                    varExpDesignY.append(np.var(components, axis=0))
                else:
                    varExpDesignY.append(np.var(y, axis=0))

            Scores = [item for sublist in Scores_all for item in sublist]
            weights = [item for sublist in varExpDesignY for item in sublist]
            initModifiedLOO = [np.average([1-score for score in Scores],
                                          weights=weights)]

        if len(PCEModel.valid_model_runs) != 0:
            initValidError = self.__validError()
            initValidError = list(initValidError.values())
            print("\nInitial ValidError:", initValidError)

        # Replicate the sequential design
        for repIdx in range(n_replication):
            print(f'>>>> Replication: {repIdx+1}<<<<')

            # To avoid changes ub original aPCE object
            # PCEModel = copy.deepcopy(initPCEModel)
            PCEModel.ExpDesign.X = Xinit
            PCEModel.ExpDesign.Y = initYprev
            PCEModel.LCerror = initLCerror

            for util_f in util_func:
                print(f'>>>> UtilityFunction: {util_f} <<<<')
                # To avoid changes ub original aPCE object
                # PCEModel = copy.deepcopy(initPCEModel)
                PCEModel.ExpDesign.X = Xinit
                PCEModel.ExpDesign.Y = initYprev
                PCEModel.LCerror = initLCerror

                # Set the experimental design
                Xprev = Xinit
                total_n_samples = initTotalNSamples
                Yprev = initYprev

                Xfull = []
                Yfull = []

                # Store the initial ModifiedLOO
                if pce:
                    print("\nInitial ModifiedLOO:", initModifiedLOO)
                    ModifiedLOO = initModifiedLOO
                    SeqModifiedLOO = np.array(ModifiedLOO)

                if len(PCEModel.valid_model_runs) != 0:
                    ValidError = initValidError
                    SeqValidError = np.array(ValidError)

                # Check if data is provided
                if len(obs_data) != 0:
                    SeqBME = np.array([initBME])
                    SeqKLD = np.array([initKLD])
                    SeqDistHellinger = np.array([initDistHellinger])

                if mc_ref and pce:
                    seqRMSEMean = np.array([initRMSEMean])
                    seqRMSEStd = np.array([initRMSEStd])

                # Start Sequential Experimental Design
                postcnt = 1
                itrNr = 1
                while total_n_samples < max_n_samples:

                    # Optimal Bayesian Design
                    PCEModel.ExpDesignFlag = 'sequential'
                    Xnew, updatedPrior = self.opt_SeqDesign(TotalSigma2,
                                                            n_canddidate,
                                                            util_f)

                    S = np.min(distance.cdist(Xinit, Xnew, 'euclidean'))
                    PCEModel.seqMinDist.append(S)
                    print("\nmin Dist from OldExpDesign:", S)
                    print("\n")

                    # Evaluate the full model response at the new sample:
                    Ynew, _ = Model.run_model_parallel(
                        Xnew, prevRun_No=total_n_samples
                        )
                    total_n_samples += Xnew.shape[0]

                    # ------ Plot the surrogate model vs Origninal Model ------
                    if hasattr(PCEModel, 'adapt_verbose') and \
                       PCEModel.adapt_verbose:
                        from post_processing.adaptPlot import adaptPlot
                        y_hat, std_hat = PCEModel.eval_metamodel(samples=Xnew)
                        adaptPlot(PCEModel, Ynew, y_hat, std_hat, plotED=False)

                    # -------- Retrain the surrogate model -------
                    # Extend new experimental design
                    Xfull = np.vstack((Xprev, Xnew))

                    # Updating existing key's value
                    for OutIdx in range(len(OutputName)):
                        OutName = OutputName[OutIdx]
                        try:
                            Yfull = np.vstack((Yprev[OutName], Ynew[OutName]))
                        except:
                            Yfull = np.vstack((Yprev[OutName], Ynew))

                        PCEModel.ModelOutputDict[OutName] = Yfull

                    PCEModel.ExpDesign.sampling_method = 'user'
                    PCEModel.ExpDesign.X = Xfull
                    PCEModel.ExpDesign.Y = PCEModel.ModelOutputDict

                    # save the Experimental Design for next iteration
                    Xprev = Xfull
                    Yprev = PCEModel.ModelOutputDict

                    # Pass the new prior as the input
                    PCEModel.input_obj.poly_coeffs_flag = False
                    if updatedPrior is not None:
                        PCEModel.input_obj.poly_coeffs_flag = True
                        print("updatedPrior:", updatedPrior.shape)
                        # Arbitrary polynomial chaos
                        for i in range(updatedPrior.shape[1]):
                            PCEModel.Inputs.Marginals[i].dist_type = None
                            x = updatedPrior[:, i]
                            PCEModel.Inputs.Marginals[i].raw_data = x

                    prevPCEModel = PCEModel
                    PCEModel = PCEModel.train_norm_design(Model)

                    # -------- Evaluate the retrain surrogate model -------
                    # Compute the validation error
                    if len(PCEModel.valid_model_runs) != 0:
                        validError = self.__validError()
                        ValidError = list(validError.values())
                        print("\nUpdated ValidError:", ValidError)

                    # Extract Modified LOO from Output
                    if pce:
                        Scores_all, varExpDesignY = [], []
                        for OutName in OutputName:
                            y = initPCEModel.ExpDesign.Y[OutName]
                            Scores_all.append(list(
                                PCEModel.score_dict[OutName].values()))
                            if PCEModel.dim_red_method.lower() == 'pca':
                                pca = PCEModel.pca[OutName]
                                components = pca.transform(y)
                                varExpDesignY.append(np.var(components,
                                                            axis=0))
                            else:
                                varExpDesignY.append(np.var(y, axis=0))
                        Scores = [item for sublist in Scores_all for item
                                  in sublist]
                        weights = [item for sublist in varExpDesignY for item
                                   in sublist]
                        ModifiedLOO = [np.average(
                            [1-score for score in Scores], weights=weights)]

                        print('\n')
                        print(f"Updated ModifiedLOO {util_f}:\n", ModifiedLOO)
                        print("Xfull:", Xfull.shape)
                        print('\n')

                    # check the direction of the error (on average):
                    # if it increases consistently stop the iterations
                    n_checks = 3
                    if itrNr > n_checks * PCEModel.ExpDesign.n_new_samples:
                        # ss<0 error increasing
                        ss = np.sign(SeqModifiedLOO - ModifiedLOO)
                        errorIncreases = np.sum(np.mean(ss[-2:], axis=1)) <= \
                            -1*n_checks

                    # If error is increasing in the last n_check iteration,
                    # stop the search and return the previous PCEModel
                    if errorIncreases:
                        print("Warning: The modified error is increasing "
                              "compared to the last {n_checks} iterations.")
                        PCEModel = prevPCEModel
                        break
                    else:
                        prevPCEModel = PCEModel

                    # Store updated ModifiedLOO
                    if pce:
                        SeqModifiedLOO = np.vstack(
                            (SeqModifiedLOO, ModifiedLOO))
                        if len(PCEModel.valid_model_runs) != 0:
                            SeqValidError = np.vstack(
                                (SeqValidError, ValidError))

                    # -------- Caclulation of BME as accuracy metric -------
                    # Check if data is provided
                    if len(obs_data) != 0:
                        # Calculate the initial BME
                        out = self.__BME_Calculator(PCEModel, obs_data,
                                                    TotalSigma2)
                        BME, KLD, Posterior, DistHellinger = out
                        print('\n')
                        print("Updated BME:", BME)
                        print("Updated KLD:", KLD)
                        print('\n')

                        # Plot some snapshots of the posterior
                        step_snapshot = PCEModel.ExpDesign.step_snapshot
                        if post_snapshot and postcnt % step_snapshot == 0:
                            MAP = PCEModel.ExpDesign.max_a_post
                            parNames = PCEModel.ExpDesign.par_names
                            print('Posterior snapshot is being plotted...')
                            self.__posteriorPlot(Posterior, MAP, parNames,
                                                 'SeqPosterior_{postcnt}')
                        postcnt += 1

                    # Check the convergence of the Mean&Std
                    if mc_ref and pce:
                        print('\n')
                        RMSE_Mean, RMSE_std = self.__error_Mean_Std()
                        print(f"Updated Mean and Std error: {RMSE_Mean}, "
                              f"{RMSE_std}")
                        print('\n')

                    # Store the updated BME & KLD
                    # Check if data is provided
                    if len(obs_data) != 0:
                        SeqBME = np.vstack((SeqBME, BME))
                        SeqKLD = np.vstack((SeqKLD, KLD))
                        SeqDistHellinger = np.vstack((SeqDistHellinger,
                                                      DistHellinger))
                    if mc_ref and pce:
                        seqRMSEMean = np.vstack((seqRMSEMean, RMSE_Mean))
                        seqRMSEStd = np.vstack((seqRMSEStd, RMSE_std))

                    if pce and any(LOO < mod_LOO_threshold
                                   for LOO in ModifiedLOO):
                        break
                itrNr += 1
                # Store updated ModifiedLOO and BME in dictonary
                strKey = f'{util_f}_rep_{repIdx+1}'
                if pce:
                    PCEModel.SeqModifiedLOO[strKey] = SeqModifiedLOO
                if len(PCEModel.valid_model_runs) != 0:
                    PCEModel.seqValidError[strKey] = SeqValidError

                # Check if data is provided
                if len(obs_data) != 0:
                    PCEModel.SeqBME[strKey] = SeqBME
                    PCEModel.SeqKLD[strKey] = SeqKLD
                if len(PCEModel.valid_likelihoods) != 0:
                    PCEModel.SeqDistHellinger[strKey] = SeqDistHellinger
                if mc_ref and pce:
                    PCEModel.seqRMSEMean[strKey] = seqRMSEMean
                    PCEModel.seqRMSEStd[strKey] = seqRMSEStd

        return PCEModel

    # -------------------------------------------------------------------------
    def util_VarBasedDesign(self, X_can, index, util_func='Entropy'):
        """
        Computes the exploitation scores based on:
        active learning MacKay(ALM) and active learning Cohn (ALC)
        Paper: Sequential Design with Mutual Information for Computer
        Experiments (MICE): Emulation of a Tsunami Model by Beck and Guillas
        (2016)

        Parameters
        ----------
        X_can : array of shape (n_samples, n_params)
            Candidate samples.
        index : int
            Model output index.
        UtilMethod : string, optional
            Exploitation utility function. The default is 'Entropy'.

        Returns
        -------
        float
            Score.

        """
        out_dict_y = self.MetaModel.ExpDesign.Y
        out_names = self.MetaModel.ModelObj.Output.names

        if util_func == 'Entropy':
            # ----- Entropy/MMSE/active learning MacKay(ALM)  -----
            # Compute perdiction variance of the old model
            Y_PC_can, std_PC_can = self.MetaModel.eval_metamodel(samples=X_can)
            canPredVar = {key: std_PC_can[key]**2 for key in out_names}

            varPCE = np.zeros((len(out_names), X_can.shape[0]))
            for KeyIdx, key in enumerate(out_names):
                varPCE[KeyIdx] = np.max(canPredVar[key], axis=1)
            score = np.max(varPCE, axis=0)

        elif util_func == 'EIGF':
            # ----- Expected Improvement for Global fit -----
            # Eq (5) from Liu et al.(2018)
            # Compute perdiction error and variance of the old model
            Y_PC_can, std_PC_can = self.eval_metamodel(samples=X_can)
            predError = {key: Y_PC_can[key] for key in out_names}
            canPredVar = {key: std_PC_can[key]**2 for key in out_names}

            EIGF_PCE = np.zeros((len(out_names), X_can.shape[0]))
            for KeyIdx, key in enumerate(out_names):
                residual = predError[key] - out_dict_y[key][int(index)]
                var = canPredVar[key]
                EIGF_PCE[KeyIdx] = np.max(residual**2 + var, axis=1)
            score = np.max(EIGF_PCE, axis=0)

        return -1 * score   # -1 is for minimization instead of maximization

    # -------------------------------------------------------------------------
    def util_BayesianActiveDesign(self, X_can, sigma2Dict, var='DKL'):
        """
        Computes scores based on Bayesian active design criterion (var).

        It is based on the following paper:
        Oladyshkin, Sergey, Farid Mohammadi, Ilja Kroeker, and Wolfgang Nowak.
        "Bayesian3 active learning for the gaussian process emulator using
        information theory." Entropy 22, no. 8 (2020): 890.

        Parameters
        ----------
        X_can : array of shape (n_samples, n_params)
            Candidate samples.
        sigma2Dict : dict
            A dictionary containing the measurement errors (sigma^2).
        var : string, optional
            BAL design criterion. The default is 'DKL'.

        Returns
        -------
        float
            Score.

        """

        # Evaluate the PCE metamodels at that location ???
        Y_mean_can, Y_std_can = self.eval_metamodel(samples=np.array([X_can]))

        # Get the data
        obs_data = self.observations
        nObs = self.Model.n_obs
        # TODO: Analytical DKL
        # Sample a distribution for a normal dist
        # with Y_mean_can as the mean and Y_std_can as std.

        # priorMean, priorSigma2, Obs = np.empty((0)),np.empty((0)),np.empty((0))

        # for key in list(Y_mean_can):
        #     # concatenate the measurement error
        #     Obs = np.hstack((Obs,ObservationData[key]))

        #     # concatenate the mean and variance of prior predictive
        #     means, stds = Y_mean_can[key][0], Y_std_can[key][0]
        #     priorMean = np.hstack((priorSigma2,means))
        #     priorSigma2 = np.hstack((priorSigma2,stds**2))

        # # Covariance Matrix of prior
        # covPrior = np.zeros((priorSigma2.shape[0], priorSigma2.shape[0]), float)
        # np.fill_diagonal(covPrior, priorSigma2)

        # # Covariance Matrix of Likelihood
        # covLikelihood = np.zeros((sigma2Dict.shape[0], sigma2Dict.shape[0]), float)
        # np.fill_diagonal(covLikelihood, sigma2Dict)

        # # Calculate moments of the posterior (Analytical derivation)
        # n = priorSigma2.shape[0]
        # covPost = np.dot(np.dot(covPrior,np.linalg.inv(covPrior+(covLikelihood/n))),covLikelihood/n)

        # meanPost = np.dot(np.dot(covPrior,np.linalg.inv(covPrior+(covLikelihood/n))) , Obs) + \
        #             np.dot(np.dot(covPrior,np.linalg.inv(covPrior+(covLikelihood/n))),
        #                     priorMean/n)
        # # Compute DKL from prior to posterior
        # term1 = np.trace(np.dot(np.linalg.inv(covPrior),covPost))
        # deltaMean = priorMean-meanPost
        # term2 = np.dot(np.dot(deltaMean,np.linalg.inv(covPrior)),deltaMean[:,None])
        # term3 = np.log(np.linalg.det(covPrior)/np.linalg.det(covPost))
        # DKL = 0.5 * (term1 + term2 - n + term3)[0]

        # ---------- Inner MC simulation for computing Utility Value ----------
        # Estimation of the integral via Monte Varlo integration
        MCsize = 20000
        ESS = 0

        while ((ESS > MCsize) or (ESS < 1)):

            # Sample a distribution for a normal dist
            # with Y_mean_can as the mean and Y_std_can as std.
            Y_MC, std_MC = {}, {}
            logPriorLikelihoods = np.zeros((MCsize))
            for key in list(Y_mean_can):
                means, stds = Y_mean_can[key][0], Y_std_can[key][0]
                # cov = np.zeros((means.shape[0], means.shape[0]), float)
                # np.fill_diagonal(cov, stds**2)

                Y_MC[key] = np.zeros((MCsize, nObs))
                logsamples = np.zeros((MCsize, nObs))
                for i in range(nObs):
                    NormalDensity = stats.norm(means[i], stds[i])
                    Y_MC[key][:, i] = NormalDensity.rvs(MCsize)
                    logsamples[:, i] = NormalDensity.logpdf(Y_MC[key][:, i])

                logPriorLikelihoods = np.sum(logsamples, axis=1)
                std_MC[key] = np.zeros((MCsize, means.shape[0]))

            #  Likelihood computation (Comparison of data and simulation
            #  results via PCE with candidate design)
            likelihoods = self.__normpdf(Y_MC, std_MC, obs_data, sigma2Dict)

            # Check the Effective Sample Size (1<ESS<MCsize)
            ESS = 1 / np.sum(np.square(likelihoods/np.nansum(likelihoods)))

            # Enlarge sample size if it doesn't fulfill the criteria
            if ((ESS > MCsize) or (ESS < 1)):
                MCsize *= 10
                ESS = 0

        # Rejection Step
        # Random numbers between 0 and 1
        unif = np.random.rand(1, MCsize)[0]

        # Reject the poorly performed prior
        accepted = (likelihoods/np.max(likelihoods)) >= unif

        # Prior-based estimation of BME
        logBME = np.log(np.nanmean(likelihoods))

        # Posterior-based expectation of likelihoods
        postLikelihoods = likelihoods[accepted]
        postExpLikelihoods = np.mean(np.log(postLikelihoods))

        # Posterior-based expectation of prior densities
        postExpPrior = np.mean(logPriorLikelihoods[accepted])

        # Utility function Eq.2 in Ref. (2)
        # Posterior covariance matrix after observing data y
        # Kullback-Leibler Divergence (Sergey's paper)
        if var == 'DKL':

            # TODO: Calculate the correction factor for BME
            # BMECorrFactor = self.BME_Corr_Weight(PCE_SparseBayes_can,
            #                                      ObservationData, sigma2Dict)
            # BME += BMECorrFactor
            # Haun et al implementation
            # U_J_d = np.mean(np.log(Likelihoods[Likelihoods!=0])- logBME)
            U_J_d = postExpLikelihoods - logBME

        # Marginal log likelihood
        elif var == 'BME':
            U_J_d = logBME

        # Entropy-based information gain
        elif var == 'infEntropy':
            logBME = np.log(np.nanmean(likelihoods))
            infEntropy = logBME - postExpPrior - postExpLikelihoods
            U_J_d = infEntropy * -1  # -1 for minimization

        # Bayesian information criterion
        elif var == 'BIC':
            coeffs = self.MetaModel.coeffs_dict.values()
            nModelParams = max(len(v) for val in coeffs for v in val.values())
            maxL = np.nanmax(likelihoods)
            U_J_d = -2 * np.log(maxL) + np.log(nObs) * nModelParams

        # Akaike information criterion
        elif var == 'AIC':
            coeffs = self.MetaModel.coeffs_dict.values()
            nModelParams = max(len(v) for val in coeffs for v in val.values())
            maxlogL = np.log(np.nanmax(likelihoods))
            AIC = -2 * maxlogL + 2 * nModelParams
            # 2 * nModelParams * (nModelParams+1) / (nObs-nModelParams-1)
            penTerm = 0
            U_J_d = 1*(AIC + penTerm)

        # Deviance information criterion
        elif var == 'DIC':
            # D_theta_bar = np.mean(-2 * Likelihoods)
            N_star_p = 0.5 * np.var(np.log(likelihoods[likelihoods != 0]))
            Likelihoods_theta_mean = self.__normpdf(Y_mean_can, Y_std_can,
                                                  obs_data, sigma2Dict)
            DIC = -2 * np.log(Likelihoods_theta_mean) + 2 * N_star_p

            U_J_d = DIC

        else:
            print('The algorithm you requested has not been implemented yet!')

        # Handle inf and NaN (replace by zero)
        if np.isnan(U_J_d) or U_J_d == -np.inf or U_J_d == np.inf:
            U_J_d = 0.0

        return -1 * U_J_d   # -1 is for minimization instead of maximization

    # -------------------------------------------------------------------------
    def util_BayesianDesign(self, X_can, X_MC, sigma2Dict, var='DKL'):
        """
        Computes scores based on Bayesian sequential design criterion (var).

        Parameters
        ----------
        X_can : array of shape (n_samples, n_params)
            Candidate samples.
        sigma2Dict : dict
            A dictionary containing the measurement errors (sigma^2).
        var : string, optional
            Bayesian design criterion. The default is 'DKL'.

        Returns
        -------
        float
            Score.

        """

        # To avoid changes ub original aPCE object
        Model = self.Model
        PCEModel = deepcopy(self.MetaModel)

        # Old Experimental design
        oldExpDesignX = PCEModel.ExpDesign.X
        oldExpDesignY = PCEModel.ExpDesign.Y

        # Evaluate the PCE metamodels at that location ???
        Y_PC_can, _ = self.MetaModel.eval_metamodel(samples=np.array([X_can]))

        # Add all suggestion as new ExpDesign
        NewExpDesignX = np.vstack((oldExpDesignX, X_can))

        NewExpDesignY = {}
        for key in oldExpDesignY.keys():
            try:
                NewExpDesignY[key] = np.vstack((oldExpDesignY[key],
                                                Y_PC_can[key]))
            except:
                NewExpDesignY[key] = oldExpDesignY[key]

        PCEModel.ExpDesign.sampling_method = 'user'
        PCEModel.ExpDesign.X = NewExpDesignX
        PCEModel.ExpDesign.Y = NewExpDesignY

        # Create the SparseBayes-based PCE metamodel:
        PCEModel.Inputs.__poly_coeffs_flag = False
        univ_p_val = self.MetaModel.univ_basis_vals(X_can)
        G_n_m_all = np.zeros((len(Model.Output.names), Model.nObs))

        for idx, key in enumerate(Model.Output.names):
            for i in range(Model.nObs):
                BasisIndices = PCEModel.basis_dict[key]["y_"+str(i+1)]
                clf_poly = PCEModel.clf_poly[key]["y_"+str(i+1)]
                Mn = clf_poly.coef_
                Sn = clf_poly.sigma_
                beta = clf_poly.alpha_
                active = clf_poly.active_
                Psi = self.MetaModel.create_psi(BasisIndices, univ_p_val)

                Sn_new_inv = np.linalg.inv(Sn)
                Sn_new_inv += beta * np.dot(Psi[:, active].T, Psi[:, active])
                Sn_new = np.linalg.inv(Sn_new_inv)

                Mn_new = np.dot(Sn_new_inv, Mn[active]).reshape(-1, 1)
                Mn_new += beta * np.dot(Psi[:, active].T, Y_PC_can[key][0, i])
                Mn_new = np.dot(Sn_new, Mn_new).flatten()

                # Compute new moments
                mean_old = Mn[0]
                mean_new = Mn_new[0]
                std_old = np.sqrt(np.sum(np.square(Mn[1:])))
                std_new = np.sqrt(np.sum(np.square(Mn_new[1:])))

                G_n_m = np.log(std_old/std_new) - 1./2
                G_n_m += std_new**2 / (2*std_new**2)
                G_n_m += (mean_new - mean_old)**2 / (2*std_old**2)

                G_n_m_all[idx, i] = G_n_m

                clf_poly.coef_[active] = Mn_new
                clf_poly.sigma_ = Sn_new
                PCEModel.clf_poly[key]["y_"+str(i+1)] = clf_poly

        # return np.sum(G_n_m_all)
        # PCEModel.train_norm_design(Model, verbose=True)
        PCE_SparseBayes_can = PCEModel

        # Get the data
        obs_data = self.observations

        # ---------- Inner MC simulation for computing Utility Value ----------
        # Estimation of the integral via Monte Varlo integration
        MCsize = X_MC.shape[0]
        ESS = 0

        while ((ESS > MCsize) or (ESS < 1)):

            # Enriching Monte Carlo samples if need be
            if ESS != 0:
                X_MC = self.MetaModel.ExpDesign.generate_samples(MCsize,
                                                                 'random')

            # Evaluate the PCEModel at the given samples
            Y_MC, std_MC = PCE_SparseBayes_can.eval_metamodel(samples=X_MC)

            # Likelihood computation (Comparison of data and simulation
            # results via PCE with candidate design)
            likelihoods = self.__normpdf(Y_MC, std_MC, obs_data, sigma2Dict)

            # Check the Effective Sample Size (1<ESS<MCsize)
            ESS = 1 / np.sum(np.square(likelihoods/np.sum(likelihoods)))

            # Enlarge sample size if it doesn't fulfill the criteria
            if ((ESS > MCsize) or (ESS < 1)):
                MCsize *= 10
                ESS = 0

        # Rejection Step
        # Random numbers between 0 and 1
        unif = np.random.rand(1, MCsize)[0]

        # Reject the poorly performed prior
        accepted = (likelihoods/np.max(likelihoods)) >= unif

        # -------------------- Utility functions --------------------
        # Utility function Eq.2 in Ref. (2)
        # Kullback-Leibler Divergence (Sergey's paper)
        if var == 'DKL':

            # Prior-based estimation of BME
            logBME = np.log(np.nanmean(likelihoods))

            # Posterior-based expectation of likelihoods
            postLikelihoods = likelihoods[accepted]
            postExpLikelihoods = np.mean(np.log(postLikelihoods))

            # Haun et al implementation
            U_J_d = np.mean(np.log(likelihoods[likelihoods != 0])- logBME)

            U_J_d = np.sum(G_n_m_all)
            # Ryan et al (2014) implementation
            # importanceWeights = Likelihoods[Likelihoods!=0]/np.sum(Likelihoods[Likelihoods!=0])
            # U_J_d = np.mean(importanceWeights*np.log(Likelihoods[Likelihoods!=0])) - logBME

            # U_J_d = postExpLikelihoods - logBME

        # Marginal likelihood
        elif var == 'BME':

            # Prior-based estimation of BME
            logBME = np.log(np.nanmean(likelihoods))
            U_J_d = logBME

        # Bayes risk likelihood
        elif var == 'BayesRisk':

            U_J_d = -1 * np.var(likelihoods)

        # Entropy-based information gain
        elif var == 'infEntropy':
            # Prior-based estimation of BME
            logBME = np.log(np.nanmean(likelihoods))

            # Posterior-based expectation of likelihoods
            postLikelihoods = likelihoods[accepted] / np.nansum(likelihoods[accepted])
            postExpLikelihoods = np.mean(np.log(postLikelihoods))

            # Posterior-based expectation of prior densities
            postExpPrior = np.mean(logPriorLikelihoods[accepted])

            infEntropy = logBME - postExpPrior - postExpLikelihoods

            U_J_d = infEntropy * -1  # -1 for minimization

        # D-Posterior-precision
        elif var == 'DPP':
            X_Posterior = X_MC[accepted]
            # covariance of the posterior parameters
            U_J_d = -np.log(np.linalg.det(np.cov(X_Posterior)))

        # A-Posterior-precision
        elif var == 'APP':
            X_Posterior = X_MC[accepted]
            # trace of the posterior parameters
            U_J_d = -np.log(np.trace(np.cov(X_Posterior)))

        else:
            print('The algorithm you requested has not been implemented yet!')

        return -1 * U_J_d   # -1 is for minimization instead of maximization

    # -------------------------------------------------------------------------
    def subdomain(self, Bounds, n_new_samples):
        """
        Divides a domain defined by Bounds into sub domains.

        Parameters
        ----------
        Bounds : list of tuples
            List of lower and upper bounds.
        n_new_samples : TYPE
            DESCRIPTION.

        Returns
        -------
        Subdomains : TYPE
            DESCRIPTION.

        """
        n_params = self.MetaModel.n_params
        n_subdomains = n_new_samples + 1
        LinSpace = np.zeros((n_params, n_subdomains))

        for i in range(n_params):
            LinSpace[i] = np.linspace(start=Bounds[i][0], stop=Bounds[i][1],
                                      num=n_subdomains)
        Subdomains = []
        for k in range(n_subdomains-1):
            mylist = []
            for i in range(n_params):
                mylist.append((LinSpace[i, k+0], LinSpace[i, k+1]))
            Subdomains.append(tuple(mylist))

        return Subdomains

    # -------------------------------------------------------------------------
    def run_util_func(self, method, candidates, index, sigma2Dict=None,
                      var=None, X_MC=None):
        """
        Runs the utility function based on the given method.

        Parameters
        ----------
        method : string
            Exploitation method: `VarOptDesign`, `BayesActDesign` and
            `BayesOptDesign`.
        candidates : array of shape (n_samples, n_params)
            All candidate parameter sets.
        index : int
            ExpDesign index.
        sigma2Dict : dict, optional
            A dictionary containing the measurement errors (sigma^2). The
            default is None.
        var : string, optional
            Utility function. The default is None.
        X_MC : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        index : TYPE
            DESCRIPTION.
        TYPE
            DESCRIPTION.

        """

        if method.lower() == 'varoptdesign':
            U_J_d = self.util_VarBasedDesign(candidates, index, var)

        elif method.lower() == 'bayesactdesign':
            NCandidate = candidates.shape[0]
            U_J_d = np.zeros((NCandidate))
            for idx, X_can in tqdm(enumerate(candidates), ascii=True,
                                   desc="OptBayesianDesign"):
                U_J_d[idx] = self.util_BayesianActiveDesign(X_can, sigma2Dict,
                                                            var)
        elif method.lower() == 'bayesoptdesign':
            NCandidate = candidates.shape[0]
            U_J_d = np.zeros((NCandidate))
            for idx, X_can in tqdm(enumerate(candidates), ascii=True,
                                   desc="OptBayesianDesign"):
                U_J_d[idx] = self.util_BayesianDesign(X_can, X_MC, sigma2Dict,
                                                      var)
        return (index, -1 * U_J_d)

    # -------------------------------------------------------------------------
    def dual_annealing(self, method, Bounds, sigma2Dict, var, Run_No,
                       verbose=False):
        """
        Exploration algorithim to find the optimum parameter space.

        Parameters
        ----------
        method : string
            Exploitation method: `VarOptDesign`, `BayesActDesign` and
            `BayesOptDesign`.
        Bounds : list of tuples
            List of lower and upper boundaries of parameters.
        sigma2Dict : dict
            A dictionary containing the measurement errors (sigma^2).
        Run_No : int
            Run number.
        verbose : bool, optional
            Print out a summary. The default is False.

        Returns
        -------
        Run_No : int
            Run number.
        array
            Optimial candidate.

        """

        Model = self.Model
        max_func_itr = self.MetaModel.ExpDesign.max_func_itr

        if method == 'VarOptDesign':
            Res_Global = opt.dual_annealing(self.util_VarBasedDesign,
                                            bounds=Bounds,
                                            args=(Model, var),
                                            maxfun=max_func_itr)

        elif method == 'BayesOptDesign':
            Res_Global = opt.dual_annealing(self.util_BayesianDesign,
                                            bounds=Bounds,
                                            args=(Model, sigma2Dict, var),
                                            maxfun=max_func_itr)

        if verbose:
            print(f"global minimum: xmin = {Res_Global.x}, "
                  f"f(xmin) = {Res_Global.fun:.6f}, nfev = {Res_Global.nfev}")

        return (Run_No, Res_Global.x)

    # -------------------------------------------------------------------------
    def tradoff_weights(self, tradeoff_scheme, old_EDX, old_EDY):
        """
        Calculates weights for exploration scores based on the requested
        scheme: `None`, `equal`, `epsilon-decreasing` and `adaptive`.

        `None`: No exploration.
        `equal`: Same weights for exploration and exploitation scores.
        `epsilon-decreasing`: Start with more exploration and increase the
            influence of exploitation along the way with a exponential decay
            function
        `adaptive`: An adaptive method based on:
            Liu, Haitao, Jianfei Cai, and Yew-Soon Ong. "An adaptive sampling
            approach for Kriging metamodeling by maximizing expected prediction
            error." Computers & Chemical Engineering 106 (2017): 171-182.

        Parameters
        ----------
        tradeoff_scheme : string
            Trade-off scheme for exloration and exploitation scores.
        old_EDX : array (n_samples, n_params)
            Old experimental design (training points).
        old_EDY : dict
            Old model responses (targets).

        Returns
        -------
        exploration_weight : float
            Exploration weight.
        exploitation_weight: float
            Exploitation weight.

        """
        if tradeoff_scheme is None:
            exploration_weight = 0

        elif tradeoff_scheme == 'equal':
            exploration_weight = 0.5

        elif tradeoff_scheme == 'epsilon-decreasing':
            # epsilon-decreasing scheme
            # Start with more exploration and increase the influence of
            # exploitation along the way with a exponential decay function
            initNSamples = self.MetaModel.ExpDesign.initNrSamples
            n_max_samples = self.MetaModel.ExpDesign.n_max_samples

            itrNumber = (self.MetaModel.ExpDesign.X.shape[0] - initNSamples)
            itrNumber //= self.MetaModel.ExpDesign.n_new_samples

            tau2 = -(n_max_samples-initNSamples-1) / np.log(1e-8)
            exploration_weight = signal.exponential(n_max_samples-initNSamples,
                                                    0, tau2, False)[itrNumber]

        elif tradeoff_scheme == 'adaptive':

            # Extract itrNumber
            initNSamples = self.MetaModel.ExpDesign.initNrSamples
            n_max_samples = self.MetaModel.ExpDesign.n_max_samples
            itrNumber = (self.ExpDesign.X.shape[0] - initNSamples)
            itrNumber //= self.ExpDesign.n_new_samples

            if itrNumber == 0:
                exploration_weight = 0.5
            else:
                # # Extract the model errors from the last and next to last
                # # iterations
                # errorModel_i , errorModel_i_1 = self.errorModel[itrNumber],
                # self.errorModel[itrNumber-1]

                # # Evaluate the error models for all selected samples so far
                # eLCAllCands_i, _ = errorModel_i.eval_errormodel(OldExpDesign)
                # eLCAllCands_i_1, _ = errorModel_i_1.eval_errormodel(OldExpDesign)

                # # Local improvement of LC error at last selected design
                # sl_i = np.max(np.dstack(eLCAllCands_i.values())[-1])
                # sl_i_1 = np.max(np.dstack(eLCAllCands_i_1.values())[-1])

                # p = sl_i**2 / sl_i_1**2

                # # Global improvement of LC error at OldExpDesign
                # sg_i = np.max(np.dstack(eLCAllCands_i.values()),axis=1)
                # sg_i_1 = np.max(np.dstack(eLCAllCands_i_1.values()),axis=1)

                # q = np.sum(np.square(sg_i)) / np.sum(np.square(sg_i_1))

                # weightExploration = min([0.5*p/q, 1])

                # TODO: New adaptive trade-off according to Liu et al. (2017)
                # Mean squared error for last design point
                last_EDX = old_EDX[-1].reshape(1, -1)
                lastPCEY, _ = self.MetaModel.eval_metamodel(samples=last_EDX)
                pce_y = np.array(list(lastPCEY.values()))[:, 0]
                y = np.array(list(old_EDY.values())[1:])[:, -1, :]
                mseError = mean_squared_error(pce_y, y)

                # Mean squared CV - error for last design point
                error = []
                for V in self.MetaModel.LCerror.values():
                    for v in V.values():
                        error.append(v[-1])
                mseCVError = np.mean(np.square(error))
                exploration_weight = 0.99 * min([0.5*mseError/mseCVError, 1])

        # Exploitation weight
        exploitation_weight = 1 - exploration_weight

        return exploration_weight, exploitation_weight

    # -------------------------------------------------------------------------
    def opt_SeqDesign(self, sigma2, n_candidates=5, var='DKL'):
        """
        Runs optimal sequential design.

        Parameters
        ----------
        sigma2 : dict, optional
            A dictionary containing the measurement errors (sigma^2). The
            default is None.
        n_candidates : int, optional
            Number of candidate samples. The default is 5.
        var : string, optional
            Utility function. The default is None.

        Raises
        ------
        NameError
            Wrong utility function.

        Returns
        -------
        Xnew : array (n_samples, n_params)
            Selected new training point(s).
        """

        # Initialization
        PCEModel = self.MetaModel
        Bounds = PCEModel.bound_tuples
        n_new_samples = PCEModel.ExpDesign.n_new_samples
        explore_method = PCEModel.ExpDesign.explore_method
        exploit_method = PCEModel.ExpDesign.exploit_method
        n_cand_groups = PCEModel.ExpDesign.n_cand_groups
        tradeoff_scheme = PCEModel.ExpDesign.tradeoff_scheme

        old_EDX = PCEModel.ExpDesign.X
        old_EDY = PCEModel.ExpDesign.Y.copy()
        ndim = PCEModel.ExpDesign.X.shape[1]
        OutputNames = PCEModel.ModelObj.Output.names

        # -----------------------------------------
        # ----------- CUSTOMIZED METHODS ----------
        # -----------------------------------------
        # Utility function exploit_method provided by user
        if exploit_method.lower() == 'user':

            Xnew, filteredSamples = PCEModel.ExpDesign.ExploitFunction(self)

            print("\n")
            print("\nXnew:\n", Xnew)

            return Xnew, filteredSamples

        # -----------------------------------------
        # ---------- EXPLORATION METHODS ----------
        # -----------------------------------------
        if explore_method == 'dual annealing':
            # ------- EXPLORATION: OPTIMIZATION -------
            import time
            start_time = time.time()

            # Divide the domain to subdomains
            args = []
            subdomains = self.subdomain(Bounds, n_new_samples)
            for i in range(n_new_samples):
                args.append((exploit_method, subdomains[i], sigma2, var, i))

            # Multiprocessing
            pool = multiprocessing.Pool(multiprocessing.cpu_count())

            # With Pool.starmap_async()
            results = pool.starmap_async(self.dual_annealing, args).get()

            # Close the pool
            pool.close()

            Xnew = np.array([results[i][1] for i in range(n_new_samples)])

            print("\nXnew:\n", Xnew)

            elapsed_time = time.time() - start_time
            print("\n")
            print(f"elapsed_time: {round(elapsed_time,2)} sec.")
            print('-'*20)

        elif explore_method == 'LOOCV':
            # -----------------------------------------------------------------
            # TODO: LOOCV model construnction based on Feng et al. (2020)
            # 'LOOCV':
            # Initilize the ExploitScore array

            # Generate random samples
            allCandidates = PCEModel.ExpDesign.generate_samples(n_candidates,
                                                                'random')

            # Construct error model based on LCerror
            errorModel = PCEModel.create_ModelError(old_EDX, self.LCerror)
            self.errorModel.append(copy(errorModel))

            # Evaluate the error models for allCandidates
            eLCAllCands, _ = errorModel.eval_errormodel(allCandidates)
            # Select the maximum as the representative error
            eLCAllCands = np.dstack(eLCAllCands.values())
            eLCAllCandidates = np.max(eLCAllCands, axis=1)[:, 0]

            # Normalize the error w.r.t the maximum error
            scoreExploration = eLCAllCandidates / np.sum(eLCAllCandidates)

        else:
            # ------- EXPLORATION: SPACE-FILLING DESIGN -------
            # Generate candidate samples from Exploration class
            explore = Exploration(PCEModel, n_candidates)
            explore.w = 100  # * ndim #500
            # Select criterion (mc-intersite-proj-th, mc-intersite-proj)
            explore.mc_criterion = 'mc-intersite-proj'
            allCandidates, scoreExploration = explore.get_exploration_samples()

            # Temp: ---- Plot all candidates -----
            if ndim == 2:
                def plotter(points, allCandidates, Method,
                            scoreExploration=None):
                    if Method == 'Voronoi':
                        from scipy.spatial import Voronoi, voronoi_plot_2d
                        vor = Voronoi(points)
                        fig = voronoi_plot_2d(vor)
                        ax1 = fig.axes[0]
                    else:
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111)
                    ax1.scatter(points[:, 0], points[:, 1], s=10, c='r',
                                marker="s", label='Old Design Points')
                    ax1.scatter(allCandidates[:, 0], allCandidates[:, 1], s=10,
                                c='b', marker="o", label='Design candidates')
                    for i in range(points.shape[0]):
                        txt = 'p'+str(i+1)
                        ax1.annotate(txt, (points[i, 0], points[i, 1]))
                    if scoreExploration is not None:
                        for i in range(allCandidates.shape[0]):
                            txt = str(round(scoreExploration[i], 5))
                            ax1.annotate(txt, (allCandidates[i, 0],
                                               allCandidates[i, 1]))

                    plt.xlim(self.bound_tuples[0])
                    plt.ylim(self.bound_tuples[1])
                    # plt.show()
                    plt.legend(loc='upper left')

        # -----------------------------------------
        # --------- EXPLOITATION METHODS ----------
        # -----------------------------------------
        if exploit_method == 'BayesOptDesign' or\
           exploit_method == 'BayesActDesign':

            # ------- Calculate Exoploration weight -------
            # Compute exploration weight based on trade off scheme
            explore_w, exploit_w = self.tradoff_weights(tradeoff_scheme,
                                                        old_EDX,
                                                        old_EDY)
            print(f"\nweightExploration={explore_w:0.3f} "
                  f"weightExploitation={exploit_w:0.3f}")

            # ------- EXPLOITATION: BayesOptDesign & ActiveLearning -------
            if explore_w != 1.0:

                # Create a sample pool for rejection sampling
                MCsize = 15000
                X_MC = PCEModel.ExpDesign.generate_samples(MCsize, 'random')

                # Multiprocessing
                pool = multiprocessing.Pool(multiprocessing.cpu_count())

                # Split the candidates in groups for multiprocessing
                split_cand = np.array_split(allCandidates,
                                            n_cand_groups, axis=0)
                args = []
                for i in range(n_cand_groups):
                    args.append((exploit_method, split_cand[i], i, sigma2, var,
                                 X_MC))

                # With Pool.starmap_async()
                results = pool.starmap_async(self.run_util_func, args).get()

                # Close the pool
                pool.close()

                # Retrieve the results and append them
                U_J_d = np.concatenate([results[NofE][1] for NofE in
                                        range(n_cand_groups)])

                # Get the expected value (mean) of the Utility score
                # for each cell
                if explore_method == 'Voronoi':
                    U_J_d = np.mean(U_J_d.reshape(-1, n_candidates), axis=1)

                # Normalize U_J_d
                norm_U_J_d = U_J_d / np.sum(U_J_d)
                print("norm_U_J_d:\n", norm_U_J_d)
            else:
                norm_U_J_d = np.zeros((len(scoreExploration)))

            # ------- Calculate Total score -------
            # ------- Trade off between EXPLORATION & EXPLOITATION -------
            # Total score
            totalScore = exploit_w * norm_U_J_d
            totalScore += explore_w * scoreExploration

            # temp: Plot
            # dim = self.ExpDesign.X.shape[1]
            # if dim == 2:
            #     plotter(self.ExpDesign.X, allCandidates, explore_method)

            # ------- Select the best candidate -------
            # find an optimal point subset to add to the initial design by
            # maximization of the utility score and taking care of NaN values
            temp = totalScore.copy()
            temp[np.isnan(totalScore)] = -np.inf
            sorted_idxtotalScore = np.argsort(temp)[::-1]
            bestIdx = sorted_idxtotalScore[:n_new_samples]

            # select the requested number of samples
            if explore_method == 'Voronoi':
                Xnew = np.zeros((n_new_samples, ndim))
                for i, idx in enumerate(bestIdx):
                    X_can = explore.closestPoints[idx]

                    # Calculate the maxmin score for the region of interest
                    newSamples, maxminScore = explore.get_mc_samples(X_can)

                    # select the requested number of samples
                    Xnew[i] = newSamples[np.argmax(maxminScore)]
            else:
                Xnew = allCandidates[sorted_idxtotalScore[:n_new_samples]]

        elif exploit_method == 'VarOptDesign':
            # ------- EXPLOITATION: VarOptDesign -------
            UtilMethod = var

            # ------- Calculate Exoploration weight -------
            # Compute exploration weight based on trade off scheme
            explore_w, exploit_w = self.tradoff_weights(tradeoff_scheme,
                                                        old_EDX,
                                                        old_EDY)
            print(f"\nweightExploration={explore_w:0.3f} "
                  f"weightExploitation={exploit_w:0.3f}")

            # Generate candidate samples from Exploration class
            nMeasurement = old_EDY[OutputNames[0]].shape[1]

            # Find sensitive region
            if UtilMethod == 'LOOCV':
                LCerror = PCEModel.LCerror
                allModifiedLOO = np.zeros((len(old_EDX), len(OutputNames),
                                           nMeasurement))
                for y_idx, y_key in enumerate(OutputNames):
                    for idx, key in enumerate(LCerror[y_key].keys()):
                        allModifiedLOO[:, y_idx, idx] = abs(
                            LCerror[y_key][key])

                ExploitScore = np.max(np.max(allModifiedLOO, axis=1), axis=1)

            elif UtilMethod in ['EIGF', 'Entropy']:
                # ----- All other in  ['EIGF', 'Entropy', 'ALM'] -----
                # Initilize the ExploitScore array
                ExploitScore = np.zeros((len(old_EDX), len(OutputNames)))

                # Split the candidates in groups for multiprocessing
                if explore_method != 'Voronoi':
                    split_cand = np.array_split(allCandidates,
                                                n_cand_groups,
                                                axis=0)
                    goodSampleIdx = range(n_cand_groups)
                else:
                    # Find indices of the Vornoi cells with samples
                    goodSampleIdx = []
                    for idx in range(len(explore.closest_points)):
                        if len(explore.closest_points[idx]) != 0:
                            goodSampleIdx.append(idx)
                    split_cand = explore.closest_points

                # Split the candidates in groups for multiprocessing
                args = []
                for index in goodSampleIdx:
                    args.append((exploit_method, split_cand[index], index,
                                 sigma2, var))

                # Multiprocessing
                pool = multiprocessing.Pool(multiprocessing.cpu_count())
                # With Pool.starmap_async()
                results = pool.starmap_async(self.run_util_func, args).get()

                # Close the pool
                pool.close()

                # Retrieve the results and append them
                if explore_method == 'Voronoi':
                    ExploitScore = [np.mean(results[k][1]) for k in
                                    range(len(goodSampleIdx))]
                else:
                    ExploitScore = np.concatenate(
                        [results[k][1] for k in range(len(goodSampleIdx))])

            else:
                raise NameError('The requested utility function is not '
                                'available.')

            # print("ExploitScore:\n", ExploitScore)

            # find an optimal point subset to add to the initial design by
            # maximization of the utility score and taking care of NaN values
            # Total score
            # Normalize U_J_d
            ExploitScore = ExploitScore / np.sum(ExploitScore)
            totalScore = exploit_w * ExploitScore
            totalScore += explore_w * scoreExploration

            temp = totalScore.copy()
            sorted_idxtotalScore = np.argsort(temp, axis=0)[::-1]
            bestIdx = sorted_idxtotalScore[:n_new_samples]

            Xnew = np.zeros((n_new_samples, ndim))
            if explore_method != 'Voronoi':
                Xnew = allCandidates[bestIdx]
            else:
                for i, idx in enumerate(bestIdx.flatten()):
                    X_can = explore.closest_points[idx]
                    # plotter(self.ExpDesign.X, X_can, explore_method,
                    # scoreExploration=None)

                    # Calculate the maxmin score for the region of interest
                    newSamples, maxminScore = explore.get_mc_samples(X_can)

                    # select the requested number of samples
                    Xnew[i] = newSamples[np.argmax(maxminScore)]

        elif exploit_method == 'alphabetic':
            # ------- EXPLOITATION: ALPHABETIC -------
            Xnew = self.util_AlphOptDesign(allCandidates, var)

        elif exploit_method == 'Space-filling':
            # ------- EXPLOITATION: SPACE-FILLING -------
            totalScore = scoreExploration

            # ------- Select the best candidate -------
            # find an optimal point subset to add to the initial design by
            # maximization of the utility score and taking care of NaN values
            temp = totalScore.copy()
            temp[np.isnan(totalScore)] = -np.inf
            sorted_idxtotalScore = np.argsort(temp)[::-1]

            # select the requested number of samples
            Xnew = allCandidates[sorted_idxtotalScore[:n_new_samples]]

        else:
            raise NameError('The requested design method is not available.')

        print("\n")
        print("\nRun No. {}:".format(old_EDX.shape[0]+1))
        print("Xnew:\n", Xnew)

        return Xnew, None

    # -------------------------------------------------------------------------
    def util_AlphOptDesign(self, candidates, var='D-Opt'):
        """
        Enriches the Experimental design with the requested alphabetic
        criterion based on exploring the space with number of sampling points.

        Ref: Hadigol, M., & Doostan, A. (2018). Least squares polynomial chaos
        expansion: A review of sampling strategies., Computer Methods in
        Applied Mechanics and Engineering, 332, 382-407.

        Arguments
        ---------
        NCandidate : int
            Number of candidate points to be searched

        var : string
            Alphabetic optimality criterion

        Returns
        -------
        X_new : array of shape (1, n_params)
            The new sampling location in the input space.
        """
        PCEModelOrig = self.PCEModel
        Model = self.ModelObj
        n_new_samples = PCEModelOrig.ExpDesign.n_new_samples
        NCandidate = candidates.shape[0]

        # TODO: Loop over outputs
        OutputName = Model.Output.names[0]

        # To avoid changes ub original aPCE object
        PCEModel = deepcopy(PCEModelOrig)

        # Old Experimental design
        oldExpDesignX = PCEModel.ExpDesign.X

        # TODO: Only one psi can be selected.
        # Suggestion: Go for the one with the highest LOO error
        Scores = list(PCEModel.score_dict[OutputName].values())
        ModifiedLOO = [1-score for score in Scores]
        outIdx = np.argmax(ModifiedLOO)

        # Initialize Phi to save the criterion's values
        Phi = np.zeros((NCandidate))

        BasisIndices = PCEModelOrig.basis_dict[OutputName]["y_"+str(outIdx+1)]
        P = len(BasisIndices)

        # ------ Old Psi ------------
        univ_p_val = PCEModelOrig.univ_basis_vals(oldExpDesignX)
        Psi = PCEModelOrig.create_psi(BasisIndices, univ_p_val)

        # ------ New candidates (Psi_c) ------------
        # Assemble Psi_c
        univ_p_val_c = self.univ_basis_vals(candidates)
        Psi_c = self.create_psi(BasisIndices, univ_p_val_c)

        for idx in range(NCandidate):

            # Include the new row to the original Psi
            Psi_cand = np.vstack((Psi, Psi_c[idx]))

            # Information matrix
            PsiTPsi = np.dot(Psi_cand.T, Psi_cand)
            M = PsiTPsi / (len(oldExpDesignX)+1)

            if np.linalg.cond(PsiTPsi) > 1e-12 \
               and np.linalg.cond(PsiTPsi) < 1 / sys.float_info.epsilon:
                # faster
                invM = linalg.solve(M, sparse.eye(PsiTPsi.shape[0]).toarray())
            else:
                # stabler
                invM = np.linalg.pinv(M)

            # ---------- Calculate optimality criterion ----------
            # Optimality criteria according to Section 4.5.1 in Ref.

            # D-Opt
            if var == 'D-Opt':
                Phi[idx] = (np.linalg.det(invM)) ** (1/P)

            # A-Opt
            elif var == 'A-Opt':
                Phi[idx] = np.trace(invM)

            # K-Opt
            elif var == 'K-Opt':
                Phi[idx] = np.linalg.cond(M)

            else:
                raise Exception('The optimality criterion you requested has '
                      'not been implemented yet!')

        # find an optimal point subset to add to the initial design
        # by minimization of the Phi
        sorted_idxtotalScore = np.argsort(Phi)

        # select the requested number of samples
        Xnew = candidates[sorted_idxtotalScore[:n_new_samples]]

        return Xnew

    # -------------------------------------------------------------------------
    def __normpdf(self, PCEOutputs, std_PC_MC, obs_data, Sigma2s):

        output_names = self.Model.Output.names

        SampleSize, index = PCEOutputs[output_names[0]].shape

        # Flatten the ObservationData
        TotalData = obs_data[output_names].to_numpy().flatten('F')

        # Remove NaN
        TotalData = TotalData[~np.isnan(TotalData)]
        Sigma2s = Sigma2s[~np.isnan(Sigma2s)]

        # Flatten the Output
        TotalOutputs = np.empty((SampleSize, 0))
        for idx, key in enumerate(output_names):
            TotalOutputs = np.hstack((TotalOutputs, PCEOutputs[key]))

        # Covariance Matrix
        covMatrix = np.zeros((Sigma2s.shape[0], Sigma2s.shape[0]), float)
        np.fill_diagonal(covMatrix, Sigma2s)

        # Add the std of the PCE.
        covMatrix_PCE = np.zeros((Sigma2s.shape[0], Sigma2s.shape[0]), float)
        stdPCE = np.empty((SampleSize, 0))
        for idx, key in enumerate(output_names):
            stdPCE = np.hstack((stdPCE, std_PC_MC[key]))

        # Expected value of variance (Assump: i.i.d stds)
        varPCE = np.mean(stdPCE**2, axis=0)
        # # varPCE = np.var(stdPCE, axis=1)
        np.fill_diagonal(covMatrix_PCE, varPCE)

        # Aggregate the cov matrices
        covMatrix += covMatrix_PCE

        # Compute likelihood
        self.Likelihoods = stats.multivariate_normal.pdf(TotalOutputs,
                                                         mean=TotalData,
                                                         cov=covMatrix,
                                                         allow_singular=True)
        return self.Likelihoods

    # -------------------------------------------------------------------------
    def __posteriorPlot(self, Posterior, MAP, parNames, key, figsize=(10, 10)):

        # Initialization
        newpath = (r'Outputs_SeqPosteriorComparison')
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        lw = 3.
        bound_tuples = self.bound_tuples
        n_params = len(MAP)

        # This is the true mean of the second mode that we used above:
        value1 = MAP

        # This is the empirical mean of the sample:
        value2 = np.mean(Posterior, axis=0)

        if n_params == 2:

            figPosterior, ax = plt.subplots()
            plt.hist2d(Posterior[:, 0], Posterior[:, 1], bins=(200, 200),
                       range=np.array([bound_tuples[0], bound_tuples[1]]),
                       cmap=plt.cm.jet)

            plt.xlabel(parNames[0])
            plt.ylabel(parNames[1])

            plt.xlim(bound_tuples[0])
            plt.ylim(bound_tuples[1])

            ax.axvline(value1[0], color="g", lw=lw)
            ax.axhline(value1[1], color="g", lw=lw)
            ax.plot(value1[0], value1[1], "sg", lw=lw+1)

            ax.axvline(value2[0], ls='--', color="r", lw=lw)
            ax.axhline(value2[1], ls='--', color="r", lw=lw)
            ax.plot(value2[0], value2[1], "sr", lw=lw+1)

        else:
            import corner
            figPosterior = corner.corner(Posterior, labels=parNames,
                                         title_fmt='.2e', show_titles=True,
                                         title_kwargs={"fontsize": 12})

            # Extract the axes
            axes = np.array(figPosterior.axes).reshape((n_params, n_params))

            # Loop over the diagonal
            for i in range(n_params):
                ax = axes[i, i]
                ax.axvline(value1[i], color="g")
                ax.axvline(value2[i], ls='--', color="r")

            # Loop over the histograms
            for yi in range(n_params):
                for xi in range(yi):
                    ax = axes[yi, xi]
                    ax.axvline(value1[xi], color="g")
                    ax.axvline(value2[xi], ls='--', color="r")
                    ax.axhline(value1[yi], color="g")
                    ax.axhline(value2[yi], ls='--', color="r")
                    ax.plot(value1[xi], value1[yi], "sg")
                    ax.plot(value2[xi], value2[yi], "sr")

        figPosterior.savefig(f'./{newpath}/{key}.svg', bbox_inches='tight')
        plt.close()

        # Save the posterior as .npy
        np.save(f'./{newpath}/{key}.npy', Posterior)

        return figPosterior

    # -------------------------------------------------------------------------
    def __hellinger_distance(self, P, Q):
        """
        Hellinger distance between two continuous distributions.

        The maximum distance 1 is achieved when P assigns probability zero to
        every set to which Q assigns a positive probability, and vice versa.
        0 (identical) and 1 (maximally different)

        Parameters
        ----------
        P : array
            Reference likelihood.
        Q : array
            Estimated likelihood.

        Returns
        -------
        float
            Hellinger distance of two distributions.

        """
        mu1 = P.mean()
        Sigma1 = np.std(P)

        mu2 = Q.mean()
        Sigma2 = np.std(Q)

        term1 = np.sqrt(2*Sigma1*Sigma2 / (Sigma1**2 + Sigma2**2))

        term2 = np.exp(-.25 * (mu1 - mu2)**2 / (Sigma1**2 + Sigma2**2))

        H_squared = 1 - term1 * term2

        return np.sqrt(H_squared)

    # -------------------------------------------------------------------------
    def __BME_Calculator(self, PCEModel, obs_data, sigma2Dict):
        """
        This function computes the Bayesian model evidence (BME) via Monte
        Carlo integration.

        """
        # Initializations
        valid_likelihoods = PCEModel.valid_likelihoods

        post_snapshot = PCEModel.ExpDesign.post_snapshot
        if post_snapshot or len(valid_likelihoods) != 0:
            newpath = (r'Outputs_SeqPosteriorComparison')
            if not os.path.exists(newpath):
                os.makedirs(newpath)

        SamplingMethod = 'random'
        MCsize = 100000
        ESS = 0

        # Estimation of the integral via Monte Varlo integration
        while ((ESS > MCsize) or (ESS < 1)):

            # Generate samples for Monte Carlo simulation
            if len(valid_likelihoods) == 0:
                X_MC = PCEModel.ExpDesign.generate_samples(MCsize,
                                                           SamplingMethod)
            else:
                X_MC = PCEModel.valid_samples
                MCsize = X_MC.shape[0]

            # Monte Carlo simulation for the candidate design
            Y_MC, std_MC = PCEModel.eval_metamodel(samples=X_MC)

            # Likelihood computation (Comparison of data and
            # simulation results via PCE with candidate design)
            Likelihoods = self.__normpdf(Y_MC, std_MC, obs_data, sigma2Dict)

            # Check the Effective Sample Size (1000<ESS<MCsize)
            ESS = 1 / np.sum(np.square(Likelihoods/np.sum(Likelihoods)))

            # Enlarge sample size if it doesn't fulfill the criteria
            if ((ESS > MCsize) or (ESS < 1)):
                print('ESS={0} MC size should be larger.'.format(ESS))
                MCsize = MCsize * 10
                ESS = 0

        # Rejection Step
        # Random numbers between 0 and 1
        unif = np.random.rand(1, MCsize)[0]

        # Reject the poorly performed prior
        accepted = (Likelihoods/np.max(Likelihoods)) >= unif
        X_Posterior = X_MC[accepted]

        # ------------------------------------------------------------
        # --- Kullback-Leibler Divergence & Information Entropy ------
        # ------------------------------------------------------------
        # Prior-based estimation of BME
        logBME = np.log(np.nanmean(Likelihoods))

        # Posterior-based expectation of likelihoods
        postExpLikelihoods = np.mean(np.log(Likelihoods[accepted]))

        # Posterior-based expectation of prior densities
        # postExpPrior = np.mean([log_prior(sample) for sample in X_Posterior])

        # Calculate Kullback-Leibler Divergence
        # KLD = np.mean(np.log(Likelihoods[Likelihoods!=0])- logBME)
        KLD = postExpLikelihoods - logBME

        # Information Entropy based on Entropy paper Eq. 38
        # infEntropy = logBME - postExpPrior - postExpLikelihoods

        # If post_snapshot is True, plot likelihood vs refrence
        if post_snapshot or len(valid_likelihoods) != 0:
            idx = len([name for name in os.listdir(newpath) if 'Likelihoods_'
                       in name and os.path.isfile(os.path.join(newpath, name))])
            fig, ax = plt.subplots()
            sns.kdeplot(np.log(valid_likelihoods[valid_likelihoods > 0]),
                        shade=True, color="g", label='Ref. Likelihood')
            sns.kdeplot(np.log(Likelihoods[Likelihoods > 0]), shade=True,
                        color="b", label='Likelihood with PCE')

            # Hellinger distance
            ref_like = np.log(valid_likelihoods[valid_likelihoods > 0])
            est_like = np.log(Likelihoods[Likelihoods > 0])
            distHellinger = self.__hellinger_distance(ref_like, est_like)
            text = f"Hellinger Dist.={distHellinger:.3f}\n logBME={logBME:.3f}"
            "\n DKL={KLD:.3f}"

            plt.text(0.05, 0.75, text, bbox=dict(facecolor='wheat',
                                                 edgecolor='black',
                                                 boxstyle='round,pad=1'),
                     transform=ax.transAxes)

            fig.savefig(f'./{newpath}/Likelihoods_{idx}.svg',
                        bbox_inches='tight')
            plt.close()

        else:
            distHellinger = 0.0

        return (logBME, KLD, X_Posterior, distHellinger)

    # -------------------------------------------------------------------------
    def __validError(self):

        PCEModel = self.MetaModel
        Model = self.Model
        OutputName = Model.Output.names

        # Generate random samples
        Samples = PCEModel.valid_samples

        # Extract the original model with the generated samples
        ModelOutputs = PCEModel.valid_model_runs

        # Run the PCE model with the generated samples
        PCEOutputs, PCEOutputs_std = PCEModel.eval_metamodel(samples=Samples)

        validError_dict = {}
        # Loop over the keys and compute RMSE error.
        for key in OutputName:
            weight = np.mean(np.square(PCEOutputs_std[key]), axis=0)
            if all(weight == 0):
                weight = 'variance_weighted'
            validError_dict[key] = mean_squared_error(ModelOutputs[key],
                                                      PCEOutputs[key])
            validError_dict[key] /= np.var(ModelOutputs[key], ddof=1)

        return validError_dict

    # -------------------------------------------------------------------------
    def __error_Mean_Std(self):

        PCEModel = self.MetaModel
        # Extract the mean and std provided by user
        df_MCReference = PCEModel.ModelObj.MCReference

        # Compute the mean and std based on the PCEModel
        PCEMeans = dict()
        PCEStds = dict()
        for Outkey, ValuesDict in PCEModel.coeffs_dict.items():
            PCEMean = np.zeros((len(ValuesDict)))
            PCEStd = np.zeros((len(ValuesDict)))

            for Inkey, InIdxValues in ValuesDict.items():
                idx = int(Inkey.split('_')[1]) - 1
                coeffs = PCEModel.coeffs_dict[Outkey][Inkey]

                # Mean = c_0
                if coeffs[0] != 0:
                    PCEMean[idx] = coeffs[0]
                else:
                    PCEMean[idx] = PCEModel.clf_poly[Outkey][Inkey].intercept_

                # Std = sqrt(sum(coeffs[1:]**2))
                PCEStd[idx] = np.sqrt(np.sum(np.square(coeffs[1:])))

            if PCEModel.dim_red_method.lower() == 'pca':
                PCA = PCEModel.pca[Outkey]
                PCEMean = PCA.mean_ + np.dot(PCEMean, PCA.components_)
                PCEStd = np.dot(PCEStd, PCA.components_)

            # Compute the error between mean and std of PCEModel and OrigModel
            RMSE_Mean = mean_squared_error(df_MCReference['mean'], PCEMean,
                                           squared=False)
            RMSE_std = mean_squared_error(df_MCReference['std'], PCEStd,
                                          squared=False)

            PCEMeans[Outkey] = PCEMean
            PCEStds[Outkey] = PCEStd

        return RMSE_Mean, RMSE_std
