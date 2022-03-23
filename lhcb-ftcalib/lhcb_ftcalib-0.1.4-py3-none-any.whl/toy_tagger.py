import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(384994875)


def gaussian_mistag(N, dist="normal", mean=0.25):
    if dist == "normal":
        return np.clip(np.random.normal(loc=mean, scale=0.05, size=N), 0, 0.5)


def distribution_mistag(tagdec, dist="OSMuon"):
    # Draw random mistag values from pre-sampled distributions

    def smear(distr, binwidth):
        # Add noise to sampled values so that they are uniformly distributed between bins
        N = len(distr)
        smear = np.random.uniform(-binwidth / 2, binwidth / 2, size=N)
        distr += smear
        distr[distr > 0.5] -= 0.5
        return distr

    taghists = pickle.load(open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "tagger_distributions.dict"), "rb"))
    Npos = np.sum(tagdec == 1)
    Nneg = np.sum(tagdec == -1)

    histbins = taghists["nbins"]
    histcenters = taghists["centers"]
    dist_pos = taghists[dist][1]["bins"]
    dist_neg = taghists[dist][-1]["bins"]
    p_density_pos = dist_pos / (2 * histbins)
    p_density_neg = dist_neg / (2 * histbins)

    eta = np.zeros(len(tagdec))
    eta[tagdec == +1] = smear(np.random.choice(histcenters, size=Npos, p=p_density_pos), 0.5 / histbins)
    eta[tagdec == -1] = smear(np.random.choice(histcenters, size=Nneg, p=p_density_neg), 0.5 / histbins)
    return eta


def decay_time_generator(chunk, lifetime):
    # Returns decay time distribution with arctan accepance model
    while True:
        tau = np.random.exponential(scale = 1.0 / lifetime, size=chunk)
        tau_choose  = np.random.uniform(0, 1, chunk)
        tau = tau[tau_choose < 2 * np.arctan(2 * tau) / np.pi]
        yield tau


def generate(N, func, params, osc, tagger_types, life=1.52, DM=0.5065, DG=0, Aprod=0, tag_effs=None):
    r""" Toy data generator
        Generated toy data for provided tagger qualities.

        :param N: Number of events to generate in total
        :type N: int
        :param func: Calibration function
        :type func: CalibrationFunction
        :param params: List of parameter lists of calibration parameters in flavour specific convention
        :type params: list
        :param osc: If true, oscillation is simulated
        :type osc: bool
        :param tagger_types: List of classical taggers whose distribution should be generated
        :type tagger_types: list of str
        :param life: B meson lifetime in ps
        :type life: float
        :param DM: :math:`\Delta m`
        :type DM: float
        :param DG: :math:`\Delta\Gamma`
        :type DG: float
        :param Aprod: Production asymmetry (WIP)
        :type Aprod: float
        :param tag_effs: Optional list of tagging efficiencies for each tagger
        :type tag_effs: list of float or None

        :return: pandas DataFrame with tagging data
        :return type: pandas.DataFrame
    """
    # PROD  == True production flavour
    # PRED  == Production flavour estimate as lhcb_ftcalib would compute it based on provided ID and decay time
    # DECAY == Decay flavour (B_ID)
    # OSC   == 1 if oscillated else 0 (truth info)
    # TAU   == Decay time
    # TOYX_DEC   == Tagging decision
    # TOYX_OMEGA == Calibrated mistag (here: generated mistag)
    # TOYX_ETA   == Measured mistag eta = omega^-1(eta)

    if osc:
        # Generate decay time with acceptance
        tau_gen = decay_time_generator(N, life)
        tau = next(tau_gen)
        while len(tau) < N:
            tau = np.append(tau, next(decay_time_generator(N, life)))
        tau = tau[:N]

    # Start with prod == dec
    toydata = pd.DataFrame({
        "eventNumber" : np.arange(N),
        "TOY_PROD"    : np.ones(N, dtype=np.int32),
        "TOY_PRED"    : np.ones(N, dtype=np.int32),
        "TOY_DECAY"   : np.ones(N, dtype=np.int32),
    })
    toydata.loc[N // 2:, "TOY_PROD"] *= -1
    toydata.loc[N // 2:, "TOY_PRED"] *= -1
    toydata.loc[N // 2:, "TOY_DECAY"] *= -1

    if osc:
        # Oscillate mesons by inverting prod if oscillation is likely
        # This way, there is a time dependence between tag decision and production flavour
        toydata["TAU"] = tau
        Amix = np.cos(DM * toydata.TAU) / np.cosh(0.5 * DG * toydata.TAU)
        osc_prob = 0.5 * (1 - Amix)
        rand_thresh = np.random.uniform(0, 1, N)
        has_oscillated = rand_thresh < osc_prob
        toydata.loc[has_oscillated, "TOY_PROD"] *= -1
        toydata["OSC"] = has_oscillated

        # Compute predicted production flavour if only ID and TAU are known
        toydata.loc[np.sign(Amix) == -1, "TOY_PRED"] *= -1

    # Generate the mistag distribution from stored histograms
    for t, tparams in enumerate(params):
        name = f"TOY{t}"
        toydata.eval(f"{name}_DEC=TOY_PROD", inplace=True)
        toydata[f"{name}_OMEGA"] = distribution_mistag(toydata[f"{name}_DEC"], dist=tagger_types[t])

        # Falsify tagging decisions using calibrated (true) mistag probability omega
        rand_thresh = np.random.uniform(0, 1, N)
        toydata.loc[rand_thresh < toydata[f"{name}_OMEGA"], f"{name}_DEC"] *= -1

        average_omega = np.mean(toydata[f"{name}_OMEGA"])

        # Compute true inverse omegas to get eta distributions
        inv_prec = 1000
        eta_lin = np.linspace(0, 0.5, inv_prec)
        # Reconstruct average eta which is unknown since calibration is
        # nonlinear, but: average_eta effectively shifts the mistag
        # distribution on eta axis.  Therefore, if we shift the omega distribution
        # so that it is centered at 0, we can measure the mean average eta shift
        # the calibration is applying to the eta distribution like this:
        # <eta>' = < omega^-1(omega - <omega>, 0) >
        # Then, when we shift the omega distribution back by <omega> we get
        # <eta> = <eta>' + <omega>
        # For less extreme/flavour asymmetric calibrations this seems to work sufficiently well

        omega_prime_lineshape = 0.5 * (func.eval(tparams, eta_lin - average_omega, np.ones(inv_prec), 0) + func.eval(tparams, eta_lin - average_omega, -np.ones(inv_prec), 0))
        average_etaprime = np.mean(np.interp(toydata[toydata["TOY_DECAY"] == +1][f"{name}_OMEGA"] - average_omega, omega_prime_lineshape, eta_lin - average_omega))
        average_eta = average_etaprime + average_omega

        # Numerical inversion of calibration function
        omegaP_lineshape = func.eval(tparams, eta_lin,  np.ones(inv_prec), average_eta)
        omegaM_lineshape = func.eval(tparams, eta_lin, -np.ones(inv_prec), average_eta)
        inv_omegaP = np.interp(toydata[toydata["TOY_PRED"] == +1][f"{name}_OMEGA"], omegaP_lineshape, eta_lin)
        inv_omegaM = np.interp(toydata[toydata["TOY_PRED"] == -1][f"{name}_OMEGA"], omegaM_lineshape, eta_lin)

        toydata.loc[toydata["TOY_PRED"] == +1, f"{name}_ETA"] = inv_omegaP
        toydata.loc[toydata["TOY_PRED"] == -1, f"{name}_ETA"] = inv_omegaM

    # Shuffle
    toydata = toydata.sample(frac=1)
    toydata.reset_index(drop=True, inplace=True)

    # Tagging efficiency -> remove percentage of tags
    if tag_effs is not None:
        assert len(tag_effs) == len(tagger_types), "You must provide as many tagging efficiencies as there are taggers"
        for i, tag_eff in enumerate(tag_effs):
            # Set events to untagged to match request tagging efficiency
            toydata.loc[int(tag_eff * len(toydata)):, f"TOY{i}_OMEGA"] = 0.5
            toydata.loc[int(tag_eff * len(toydata)):, f"TOY{i}_ETA"] = 0.5
            toydata.loc[int(tag_eff * len(toydata)):, f"TOY{i}_DEC"] = 0

        # Shuffle again
        toydata = toydata.sample(frac=1)
        toydata.reset_index(drop=True, inplace=True)

    # Set overflow events to untagged. This is not entirely realistic, as the
    # calibrated mistag can be > 0.5 (in this generator eta > 0.5 is possible,
    # omega > 0.5 is not) and therefore the calibration procedure itself is not
    # necessarily bijective. Here, we ignore that fact and set all those
    # "problematic" events to untagged beforehand. Since this negatively
    # impacts the toy data quality, a warning is raised
    for i in range(len(tagger_types)):
        overflow = np.logical_or(toydata[f"TOY{i}_OMEGA"] > 0.5, toydata[f"TOY{i}_ETA"] > 0.5)
        if overflow.sum() > 0:
            print(f"Warning TOY{i}: {overflow.sum()} mistags can overflow and will be additionally untagged!")
            toydata.loc[overflow:, f"TOY{i}_OMEGA"] = 0.5
            toydata.loc[overflow:, f"TOY{i}_ETA"] = 0.5
            toydata.loc[overflow:, f"TOY{i}_DEC"] = 0

    return toydata
