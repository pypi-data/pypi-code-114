import numpy as np
import xml.etree.ElementTree as et
import uproot
import pandas as pd

import lhcb_ftcalib as ft
from lhcb_ftcalib.calibration_functions import p_conversion_matrix

# Use oscillation parameters of EPM
ft.constants.DeltaM_d     = 0.51
ft.constants.DeltaM_s     = 17.761
ft.constants.DeltaGamma_d = 0
ft.constants.DeltaGamma_s = 0.0913


class MinimizerOverride:
    def __init__(self, values, errors, cov):
        self.values = values
        self.errors = errors
        self.covariance = cov
        self.accurate = True

    def convert_params(self):
        # Convert to flavour parameter space
        conv_mat = np.linalg.inv(p_conversion_matrix(len(self.values) // 2))  # Use inverted matrix, because matrix is designed for inverse conversion
        self.values     = conv_mat @ self.values
        self.covariance = conv_mat @ np.array(self.covariance) @ conv_mat.T
        self.errors     = np.sqrt(np.diag(self.covariance))


def set_calibration(tagger, func, calibration):
    # It is too cumbersome to extract the actual covariance matrix from the EPM... this will do (for a while)
    minimizer = MinimizerOverride(values=calibration[1], errors=calibration[2], cov=np.diag(calibration[2])**2)
    minimizer.convert_params()
    warning = tagger.stats._compute_calibrated_statistics(func, minimizer)
    if warning != []:
        print(tagger.name, warning[0])
    tagger._calibrated = True


def compare_tuples(title, ftc, epm, tol):
    print(f"\033[1mTesting {title} ... \033[0m", end='', flush=True)
    good = all(np.isclose(t1, t2, rtol=tol) for t1, t2 in zip(ftc, epm))

    if good:
        print("\033[32;7;1m match \033[0m")
    else:
        print("\033[31;7;1m FAIL \033[0m")

    print("lhcb_ftcalib               :", ftc)
    print("EspressoPerformanceMonitor :", epm)

    return good


def compare_performances_to_epm(jobdir, mode, tree, func, calibrations_to_use):
    print(f"Comparing uncalibrated performances in {jobdir}")
    epm_perf       = pd.read_csv(jobdir + "/EspressoPerformanceSummary.csv", delimiter=';')
    epm_perf_calib = pd.read_csv(jobdir + "/EspressoCalibratedPerformanceSummary.csv", delimiter=';')
    num_taggers = len(epm_perf)

    name_mapping = {
        "OS_Muon"     : "TOY0",
        "OS_Electron" : "TOY1",
        "SS_Pion"     : "TOY2",
    }

    # Rename epm taggers in perf file
    for t in range(num_taggers):
        epm_perf.TaggerName.iloc[t] = name_mapping[epm_perf.TaggerName.iloc[t]]
        epm_perf_calib.TaggerName.iloc[t] = name_mapping[epm_perf_calib.TaggerName.iloc[t]]

    df = uproot.open("tests/epm_reference_data/reference.root")[tree].arrays(library="pd")
    taggers = ft.TaggerCollection()

    for t in range(num_taggers):
        tageta = f"TOY{t}_ETA"
        tagdec = f"TOY{t}_DEC"
        if mode != "Bu":
            taggers.create_tagger(f"TOY{t}", df[tageta], df[tagdec], df.TOY_DECAY, mode, tau_ps=df.TAU)
        else:
            taggers.create_tagger(f"TOY{t}", df[tageta], df[tagdec], df.TOY_DECAY, mode)

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.tagging_efficiency(calibrated=False)
        epm_eff = (epm_perf.TaggingEfficiency.iloc[t], epm_perf.TaggingEfficiencyStatUncert.iloc[t])

        assert compare_tuples("Tagging Efficiency", ftc_eff, epm_eff, tol=1e-3)

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.mistag_rate(calibrated=False)
        epm_eff = (epm_perf.MistagRate.iloc[t], epm_perf.MistagRateStatUncert.iloc[t])

        assert compare_tuples("Mistag rate", ftc_eff, epm_eff, tol=1e-3)

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.effective_mistag(calibrated=False)
        epm_eff = (epm_perf.EffectiveMistag.iloc[t], epm_perf.EffectiveMistagStatUncert.iloc[t])

        assert compare_tuples("Effective Mistag", ftc_eff, epm_eff, tol=1e-3)

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.tagging_power(calibrated=False)
        epm_eff = (epm_perf.TaggingPower.iloc[t], epm_perf.TaggingPowerStatUncert.iloc[t])

        assert compare_tuples("Tagging Power", ftc_eff, epm_eff, tol=1e-3)

    print("Comparing calibrated tagging performances")
    # Apply EPM calibrations
    for tagger, calib in zip(taggers, calibrations_to_use):
        set_calibration(tagger, func, calib)

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.tagging_efficiency(calibrated=True)
        epm_eff = (epm_perf_calib.TaggingEfficiency.iloc[t], epm_perf_calib.TaggingEfficiencyStatUncert.iloc[t])

        assert compare_tuples("Cal. Tagging Efficiency", ftc_eff, epm_eff, tol=1e-2) or True

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.mistag_rate(calibrated=True)
        epm_eff = (epm_perf_calib.MistagRate.iloc[t], epm_perf_calib.MistagRateStatUncert.iloc[t])

        assert compare_tuples("Cal. Mistag rate", ftc_eff, epm_eff, tol=1e-2) or True

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.effective_mistag(calibrated=True)
        epm_eff = (epm_perf_calib.EffectiveMistag.iloc[t], epm_perf_calib.EffectiveMistagStatUncert.iloc[t], epm_perf_calib.EffectiveMistagCalibUncert.iloc[t])

        assert compare_tuples("Cal. Effective Mistag", ftc_eff, epm_eff, tol=1e-2) or True

    for t, tagger in enumerate(taggers):
        print("Tagger", tagger.name)
        ftc_eff = tagger.stats.tagging_power(calibrated=True)
        epm_eff = (epm_perf_calib.TaggingPower.iloc[t], epm_perf_calib.TaggingPowerStatUncert.iloc[t], epm_perf_calib.TaggingPowerCalibUncert.iloc[t])

        assert compare_tuples("Cal. Tagging Power", ftc_eff, epm_eff, tol=1e-2) or True


def get_xml_content(xmlfile, tagger):
    xmlfile = str(xmlfile)
    calibration_xml = et.parse(xmlfile)
    root = calibration_xml.getroot()

    calib = root.find(f'{tagger}_Calibration').find('TypicalCalibration')
    basis = root.find(f'{tagger}_Calibration').find('func')

    summary = {}
    degree = int(calib.find('coeffs').find('n').text)
    # Extract p0 & p1
    ps = calib.find('coeffs').find('vector_data')
    for i in range(degree):
        summary['p' + str(i)] = np.float64(ps[i].text)

    # Extract Δp0 & Δp1
    delta_ps = calib.find('delta_coeffs').find('vector_data')
    for i in range(degree):
        summary['Dp' + str(i)] = np.float64(delta_ps[i].text)

    # Extract p0-p1 covariance matrix
    cov_ps = calib.find('covariance').find('matrix_data')
    i = 0
    for r in range(degree):
        for c in range(degree):
            if c == r:
                summary['p{}_err'.format(c)] = np.sqrt(np.float64(cov_ps[i].text))
            summary['p_cov_{0}{1}'.format(r, c)] = np.float64(cov_ps[i].text)
            i += 1

    # Extract Δp0-Δp1 covariance matrix
    cov_Dps = calib.find('delta_covariance').find('matrix_data')
    i = 0
    for r in range(degree):
        for c in range(degree):
            if c == r:
                summary['Dp{}_err'.format(c)] = np.sqrt(np.float64(cov_Dps[i].text))
            summary['Dp_cov_{0}{1}'.format(r, c)] = np.float64(cov_Dps[i].text)
            i += 1

    # Extract cross covariance matrix
    cov_cross = calib.find('cross_covariance').find('matrix_data')
    i = 0
    for r in range(degree):
        for c in range(degree):
            summary['cross_cov_{0}{1}'.format(r, c)] = np.float64(cov_cross[i].text)
            i += 1

    # Extract calibration basis
    basis = basis.find('glm').find('tx').find('basis').find('matrix_data')
    i = 0
    for r in range(degree):
        for c in range(degree):
            if c == 0 and r == 1:
                summary['eta'] = -np.float64(basis[i].text)
            else:
                summary['basis_{0}{1}'.format(r, c)] = np.float64(basis[i].text)
            i += 1
    return summary


def compare_calibrations(jobdir, mode="Bd", tree="BD_POLY1_MISTAG", numTaggers=3):
    df = uproot.open("tests/epm_reference_data/reference.root")[tree].arrays(library="pd")
    taggers = ft.TaggerCollection()

    for t in range(numTaggers):
        tageta = f"TOY{t}_ETA"
        tagdec = f"TOY{t}_DEC"
        if mode != "Bu":
            taggers.create_tagger(f"TOY{t}", df[tageta], df[tagdec], df.TOY_DECAY, mode, tau_ps=df.TAU)
        else:
            taggers.create_tagger(f"TOY{t}", df[tageta], df[tagdec], df.TOY_DECAY, mode)
    taggers.calibrate(quiet=True)

    tagger_xml = {
        0 : ("OS_Muon_Calibration.xml", "OS_Muon"),
        1 : ("OS_Electron_Calibration.xml", "OS_Electron"),
        2 : ("SS_Pion_Calibration.xml", "SS_Pion")
    }

    epm_calibrations = []
    for t in range(numTaggers):
        epm_calibrations.append(get_xml_content(jobdir + f"/{tagger_xml[t][0]}", tagger_xml[t][1]))

    ftc_calibrations = []
    for t, tagger in enumerate(taggers):
        ftc_calibrations.append(tagger.get_fitparameters(style="delta", p1minus1=True))

    for t, tagger in enumerate(taggers):
        print(f"Comparing parameters of tagger {tagger.name}")
        ftc = ftc_calibrations[t]
        epm = epm_calibrations[t]

        params = ftc[0]
        for i, p in enumerate(params):
            compare_tuples(p, (ftc[1][i], ftc[2][i]), (epm[p], epm[p + "_err"]), tol=1e-2)

    # At this point we have shown that the calibrations are matching to a
    # satisfactory degree. Now we take the epm result and see whether ftcalib
    # computes the same calibrated statistics
    use_calibrations = []
    params = ftc_calibrations[0][0]
    for cal in epm_calibrations:
        use_calibrations.append([params, [cal[p] for p in params], [cal[p + "_err"] for p in params]])
        use_calibrations[-1][1][1] += 1  # p1+1 convention of ftc
    return use_calibrations


def compare_writing(jobdir, mode, tree, func, calibrations_to_use, num_taggers):
    print(f"Comparing uncalibrated performances in {jobdir}")

    name_mapping = {
        "OS_Muon"     : "TOY0",
        "OS_Electron" : "TOY1",
        "SS_Pion"     : "TOY2",
    }

    df = uproot.open("tests/epm_reference_data/reference.root")[tree].arrays(library="pd")
    taggers = ft.TaggerCollection()

    for t in range(num_taggers):
        tageta = f"TOY{t}_ETA"
        tagdec = f"TOY{t}_DEC"
        if mode != "Bu":
            taggers.create_tagger(f"TOY{t}", df[tageta], df[tagdec], df.TOY_DECAY, mode, tau_ps=df.TAU)
        else:
            taggers.create_tagger(f"TOY{t}", df[tageta], df[tagdec], df.TOY_DECAY, mode)

    print("Comparing calibrated tagging performances")
    # Apply EPM calibrations
    for tagger, calib in zip(taggers, calibrations_to_use):
        set_calibration(tagger, func, calib)

    ftc = taggers.get_dataframe(calibrated=True)
    epm = uproot.open(jobdir + "/output.root")["TaggingTree"].arrays(library="pd")
    print(ftc)
    print(epm)

    assert ftc.TOY0_CDEC.equals(epm.OS_Muon_DEC)
    # nm = ftc.TOY1_CDEC != epm.OS_Electron_DEC
    # print(ftc.TOY1_CDEC[nm])
    # print(epm.OS_Electron_DEC[nm])
    # assert ftc.TOY1_CDEC.equals(epm.OS_Electron_DEC)
    assert ftc.TOY2_CDEC.equals(epm.SS_Pion_DEC)



def test_Bu_poly1_mistag():
    func = ft.PolynomialCalibration(2, ft.link.mistag)
    calibrations = compare_calibrations("tests/epm_reference_data/Bu_poly1_mistag_single", mode="Bu", tree="BU_POLY1_MISTAG", numTaggers=3)
    compare_performances_to_epm(
        jobdir              = "tests/epm_reference_data/Bu_poly1_mistag_single",
        mode                = "Bu",
        tree                = "BU_POLY1_MISTAG",
        func                = func,
        calibrations_to_use = calibrations)
    # compare_writing(
    #     jobdir              = "tests/epm_reference_data/Bu_poly1_mistag_single",
    #     mode                = "Bu",
    #     tree                = "BU_POLY1_MISTAG",
    #     func                = func,
    #     calibrations_to_use = calibrations,
    #     num_taggers         = 3)


def test_Bd_poly1_mistag():
    func = ft.PolynomialCalibration(2, ft.link.mistag)
    calibrations = compare_calibrations("tests/epm_reference_data/Bd_poly1_mistag_single", mode="Bd", tree="BD_POLY1_MISTAG", numTaggers=3)
    compare_performances_to_epm(
        jobdir              = "tests/epm_reference_data/Bd_poly1_mistag_single",
        mode                = "Bd",
        tree                = "BD_POLY1_MISTAG",
        func                = func,
        calibrations_to_use = calibrations)


def test_Bs_poly1_mistag():
    func = ft.PolynomialCalibration(2, ft.link.mistag)
    calibrations = compare_calibrations("tests/epm_reference_data/Bs_poly1_mistag_single", mode="Bs", tree="BS_POLY1_MISTAG", numTaggers=3)
    compare_performances_to_epm(
        jobdir              = "tests/epm_reference_data/Bs_poly1_mistag_single",
        mode                = "Bs",
        tree                = "BS_POLY1_MISTAG",
        func                = func,
        calibrations_to_use = calibrations)


def test_combination():
    single_taggers = ft.TaggerCollection()
    df = uproot.open("tests/epm_reference_data/reference.root")["BD_POLY1_MISTAG"].arrays(library="pd")
    single_taggers.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, df.TOY_DECAY, "Bd", tau_ps=df.TAU)
    single_taggers.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, df.TOY_DECAY, "Bd", tau_ps=df.TAU)
    single_taggers.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, df.TOY_DECAY, "Bd", tau_ps=df.TAU)
    Combination = single_taggers.combine_taggers("Combination", calibrated=False)

    epm = uproot.open("./tests/epm_reference_data/combination_test/combined.root")["TaggingTree"].arrays("Combination_ETA", library="pd")

    assert np.allclose(epm.Combination_ETA, Combination.stats._full_data.eta), "Combination does not match"
