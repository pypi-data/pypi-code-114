import os
import sys
import uproot
import lhcb_ftcalib as ft


def generate_reference_data(N):
    if not os.path.exists("tests/epm_reference_data"):
        os.mkdir("tests/epm_reference_data")

    FILE = uproot.recreate("tests/epm_reference_data/reference.root")

    poly1_MISTAG = ft.PolynomialCalibration(2, ft.link.mistag)
    params_poly1 = [[0, 1, 0, 1],
                    [0.01, 1.3, 0.01, 1],
                    [0.01, 0.95, 0.01, 1.1]]

    FILE["BU_POLY1_MISTAG"] = ft.toydata.generate(N,
                                                  poly1_MISTAG,
                                                  params=params_poly1,
                                                  osc=False,
                                                  DM=0, DG=0, Aprod=0,
                                                  tagger_types = ["OSMuon", "OSKaon", "SSPion"],
                                                  tag_effs = [0.99, 0.9, 0.8])
    FILE["BD_POLY1_MISTAG"] = ft.toydata.generate(N,
                                                  poly1_MISTAG,
                                                  params=params_poly1,
                                                  osc=True,
                                                  DM=0.51, DG=0, Aprod=0,  # DM_EPM = 0.51
                                                  tagger_types = ["OSMuon", "OSKaon", "SSPion"],
                                                  tag_effs = [0.99, 0.9, 0.8])
    FILE["BS_POLY1_MISTAG"] = ft.toydata.generate(N,
                                                  poly1_MISTAG,
                                                  params=params_poly1,
                                                  osc=True,
                                                  DM=17.761, DG=0.0913, Aprod=0,
                                                  tagger_types = ["OSMuon", "OSKaon", "SSPion"],
                                                  tag_effs = [0.99, 0.9, 0.8])

if __name__ == "__main__":
    generate_reference_data(int(sys.argv[1]))
