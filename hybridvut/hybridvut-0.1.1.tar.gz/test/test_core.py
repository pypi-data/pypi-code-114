import os
import sys

import numpy as np
import pandas as pd
import pytest

TESTPATH = os.path.dirname(os.path.realpath("hybrid_VUT"))
sys.path.append(TESTPATH + "/hybridvut")

import hybridvut as hyb


@pytest.fixture()
def TestDataRAS():
    """This is to test the RAS function and basic class properties.

    RAS-Example is taken from Miller and Blair, p. 335
    """

    class TablesRAS:
        U_arr = np.array([[5, 0.5], [4, 3]]).astype(float)
        U = pd.DataFrame(data=U_arr, index=["com1", "com2"], columns=["ind1", "ind2"])

        r_U = np.array([[10], [2]]).astype(float)
        r_U = pd.DataFrame(data=r_U, index=["com1", "com2"], columns=["total"])["total"]

        c_U = np.array([[7], [5]]).astype(float)
        c_U = pd.DataFrame(data=c_U, index=["ind1", "ind2"], columns=["total"])["total"]

        yz = np.array([[0], [0]]).astype(float)
        yz = pd.DataFrame(data=yz, index=["com1", "com2"], columns=["total"])["total"]

        vz = np.array([[0], [0]]).astype(float)
        vz = pd.DataFrame(data=vz, index=["ind1", "ind2"], columns=["total"])["total"]

    return TablesRAS


@pytest.fixture()
def TestDataVUT():
    """This is an example of foreground and background VUTs.

    To test hybridization and other functions.
    """

    class TablesVUT:
        reg = ["reg1", "reg2"]
        com_b = ["a", "b", "c"]
        ind_b = ["A", "B"]
        com_f = ["a*", "b*"]
        ind_f = ["A*", "B*"]
        unit_com = ["EUR"]

        # Foreground system
        ix_f = pd.MultiIndex.from_product([reg, ind_f], names=["region", "industry"])
        co_f = pd.MultiIndex.from_product(
            [reg, com_f, unit_com], names=["region", "commodity", "unit"]
        )
        ext_f = pd.MultiIndex.from_arrays(
            [["CO2"], ["kg"]], names=["extension", "unit"]
        )

        V_for = pd.DataFrame(
            np.array(
                [[90, 0, 0, 0], [0, 50, 0, 0], [0, 0, 70, 0], [0, 0, 0, 70]]
            ).astype(float),
            index=ix_f,
            columns=co_f,
        )
        U_for = pd.DataFrame(
            np.array([[0, 0, 0, 5], [30, 0, 0, 0], [0, 0, 0, 0], [2, 0, 5, 0]]).astype(
                float
            ),
            index=co_f,
            columns=ix_f,
        )
        F_for = pd.DataFrame(
            np.array([[1000, 2000, 1200, 2100]]).astype(float),
            index=ext_f,
            columns=ix_f,
        )

        # Background system
        ix_b = pd.MultiIndex.from_product([reg, ind_b], names=["region", "industry"])
        co_b = pd.MultiIndex.from_product(
            [reg, com_b, unit_com], names=["region", "commodity", "unit"]
        )
        ext_b = pd.MultiIndex.from_arrays(
            [["carbon dioxide", "N2O"], ["kg", "g"]], names=["extension", "unit"]
        )
        ext_b_Q = pd.MultiIndex.from_arrays(
            [["value added", "CO2"], ["M.EUR", "t"]], names=["extension", "unit"]
        )
        imp_b_Q = pd.MultiIndex.from_arrays(
            [["impact_A", "impact_B"], ["kg CO2-eq.", "M.EUR"]],
            names=["impact", "unit"],
        )

        V_back = pd.DataFrame(
            np.array(
                [
                    [100, 0, 10, 0, 0, 0],
                    [0, 60, 0, 0, 0, 0],
                    [0, 0, 0, 80, 0, 10],
                    [0, 0, 0, 0, 70, 0],
                ]
            ).astype(float),
            index=ix_b,
            columns=co_b,
        )
        U_back = pd.DataFrame(
            np.array(
                [
                    [10, 10, 0, 5],
                    [30, 0, 0, 0],
                    [0, 5, 0, 0],
                    [0, 0, 0, 5],
                    [5, 0, 20, 0],
                    [0, 0, 0, 5],
                ]
            ).astype(float),
            index=co_b,
            columns=ix_b,
        )
        F_back = pd.DataFrame(
            np.array([[3000, 4000, 5000, 6000], [500, 500, 400, 600]]).astype(float),
            index=ext_b,
            columns=ix_b,
        )
        Q_back = pd.DataFrame(
            np.array([[0, 1000], [1, 10000]]).astype(float),
            index=imp_b_Q,
            columns=ext_b_Q,
        )

        # Concordance matrices
        H = pd.DataFrame(
            np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]).astype(
                float
            ),
            index=ix_b,
            columns=ix_f,
        )

        H1 = pd.DataFrame(
            np.array(
                [
                    [1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                ]
            ).astype(float),
            index=co_f,
            columns=co_b,
        )

        HF = pd.DataFrame(
            np.array([[1], [0]]).astype(float), index=ext_b, columns=ext_f
        )

        # Resulting total system
        V = pd.DataFrame(
            np.array(
                [
                    [90, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 50, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 70, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 70, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 10, 0, 10, 0, 0, 0],
                    [0, 0, 0, 0, 0, 10, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 10, 0, 10],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            ).astype(float),
            index=ix_f.append(ix_b),
            columns=co_f.append(co_b),
        )

        U = pd.DataFrame(
            np.array(
                [
                    [8.7025, 8.75, 0, 5, 0.2975, 0.25, 0, 0],
                    [30, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 4.375, 0, 0, 0, 0],
                    [4.9008, 0, 19.2593, 0, 0.0992, 0, 0.7407, 0],
                    [0.8182, 0.8333, 0, 0, 0.1818, 0.1667, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 4.1667, 0, 0, 0, 0.8333, 0, 0],
                    [0, 0, 0, 0.625, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 0, 0, 0],
                ]
            ).astype(float),
            index=co_f.append(co_b),
            columns=ix_f.append(ix_b),
        )

        U_message = pd.DataFrame(
            np.array(
                [
                    [10, 10, 0, 5, 0, 0, 0, 0],
                    [30, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 0, 0, 0],
                    [5, 0, 20, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 0, 0, 0],
                ]
            ).astype(float),
            index=co_f.append(co_b),
            columns=ix_f.append(ix_b),
        )

        F = pd.DataFrame(
            np.array(
                [
                    [1000, 2000, 1200, 2100, 0, 0, 0, 0],
                    [
                        1636.364,
                        1666.667,
                        2955.556,
                        3900.000,
                        363.636,
                        333.333,
                        844.444,
                        0,
                    ],
                    [409.091, 416.667, 311.111, 600.000, 90.909, 83.333, 88.889, 0],
                ]
            ).astype(float),
            index=ext_f.append(ext_b),
            columns=ix_f.append(ix_b),
        )

        F_message = pd.DataFrame(
            np.array(
                [
                    [1000, 2000, 1200, 2100, 0, 0, 0, 0],
                    [
                        2000,
                        2000,
                        3800,
                        3900.000,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [500, 500, 400, 600.000, 0, 0, 0, 0],
                ]
            ).astype(float),
            index=ext_f.append(ext_b),
            columns=ix_f.append(ix_b),
        )

        # Special cases:
        # with multiple extensions
        ext_f_multiple = pd.MultiIndex.from_arrays(
            [["CO2", "CH4"], ["kg", "t"]], names=["extension", "unit"]
        )
        F_for_multiple = pd.DataFrame(
            np.array([[20, 10, 10, 10], [2, 4, 4, 4]]).astype(float),
            index=ext_f_multiple,
            columns=ix_f,
        )
        F_multiple = pd.DataFrame(
            np.array(
                [
                    [20, 10, 10, 10, 0, 0, 0, 0],
                    [2, 4, 4, 4, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 30, 40, 40, 40],
                ]
            ).astype(float),
            index=ext_f_multiple.append(ext_b),
            columns=ix_f.append(ix_b),
        )

        # with avoiding negative values
        V_for_neg = pd.DataFrame(
            np.array(
                [[101, 0, 0, 0], [0, 50, 0, 0], [0, 0, 70, 0], [0, 0, 0, 70]]
            ).astype(float),
            index=ix_f,
            columns=co_f,
        )

        U_neg = pd.DataFrame(
            np.array(
                [
                    [9.9188, 9.722, 0, 5, 0.0812, 0.2778, 0, 0],
                    [30, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 4.375, 0, 0, 0, 0],
                    [4.9756, 0, 19.2593, 0, 0.0243, 0, 0.7407, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 4.1667, 0, 0, 0, 0.8333, 0, 0],
                    [0, 0, 0, 0.625, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 0, 0, 0],
                ]
            ).astype(float),
            index=co_f.append(co_b),
            columns=ix_f.append(ix_b),
        )

        # for testing harmonization
        ix_not_harmo = pd.MultiIndex.from_tuples(
            [("reg1", "ind1"), ("reg2", "ind1"), ("reg2", "ind2")],
            names=("region", "industry"),
        )

        co_not_harmo = pd.MultiIndex.from_tuples(
            [("reg1", "com1", "EUR"), ("reg1", "com2", "EUR"), ("reg2", "com1", "EUR")],
            names=("region", "commodity", "unit"),
        )

        V_not_harmo = pd.DataFrame(
            np.array([[0, 0, 0], [100, 0, 0], [0, 140, 0]]).astype(float),
            index=ix_not_harmo,
            columns=co_not_harmo,
        )

        U_not_harmo = pd.DataFrame(
            np.array([[0, 0, 0], [60, 0, 0], [20, 0, 50]]).astype(float),
            index=co_not_harmo,
            columns=ix_not_harmo,
        )

        F_not_harmo = pd.DataFrame(
            np.array([[20, 10, 10], [2, 4, 4]]).astype(float),
            index=ext_f_multiple,
            columns=ix_not_harmo,
        )

        # for testing calculation of Z, y, F_multipliers and footprints
        int_F = pd.Index(data=["emis_A", "emis_B"], name="extension")
        F_ind = pd.DataFrame(
            np.array([[2, 5, 30, 10, 3, 0, 0, 0], [8, 7, 0, 0, 8, 8, 77, 0]]),
            index=int_F,
            columns=ix_f.append(ix_b),
        )

        F_com = pd.DataFrame(
            np.array(
                [[23, 3, 3, 0, 6, 88, 9, 29, 0, 1], [3, 32, 5, 7, 87, 0, 2, 1, 0, 7]]
            ),
            index=int_F,
            columns=co_f.append(co_b),
        )

        imp_Q = pd.Index(data=["imp_1", "imp_2"], name="impact")
        Q_calc_F = pd.DataFrame(
            np.array([[10, 0], [1, 0.5]]), index=imp_Q, columns=int_F
        )

        footprint_consumption = pd.DataFrame(
            np.array([[10.4715905, 39.5284095], [31.6412976, 76.3587024]]),
            index=int_F,
            columns=ix_f.unique(0).append(ix_b.unique(0)).unique(0),
        )

        footprint_income = pd.DataFrame(
            np.array([[11.0575719, 38.9424281], [30.5740612, 77.4259388]]),
            index=int_F,
            columns=ix_f.unique(0).append(ix_b.unique(0)).unique(0),
        )

        footprint_production = pd.DataFrame(
            np.array([[10, 40], [31, 77]]),
            index=int_F,
            columns=ix_f.unique(0).append(ix_b.unique(0)).unique(),
        )

    return TablesVUT


#### Test RAS and basic class properties ####


def test_RAS_U(TestDataRAS):
    U_expected = pd.DataFrame(
        np.array([[6.5911, 3.4089], [0.4099, 1.5901]]).astype(float),
        index=["com1", "com2"],
        columns=["ind1", "ind2"],
    )
    vut = hyb.VUT(U=TestDataRAS.U)
    pd.testing.assert_frame_equal(
        U_expected,
        vut.RAS_U(
            q=TestDataRAS.r_U,
            x=TestDataRAS.c_U,
            y=TestDataRAS.yz,
            v=TestDataRAS.vz,
            n=5,
        ),
        check_exact=False,
        atol=1e-3,
    )


def test_RAS_U_no_U(TestDataRAS):
    U_expected = None
    vut = hyb.VUT()
    assert (
        vut.RAS_U(
            q=TestDataRAS.r_U,
            x=TestDataRAS.c_U,
            y=TestDataRAS.yz,
            v=TestDataRAS.vz,
            n=5,
        )
        == U_expected
    )


def test_RAS_U_including_y_v(TestDataRAS):
    U_expected = pd.DataFrame(
        np.array([[6.5911, 3.4089], [0.4099, 1.5901]]).astype(float),
        index=["com1", "com2"],
        columns=["ind1", "ind2"],
    )
    e_expected = TestDataRAS.yz.to_frame()
    v_expected = TestDataRAS.vz.to_frame()

    vut = hyb.VUT(U=TestDataRAS.U)
    U_test, e_test, v_test = vut.RAS_U(
        q=TestDataRAS.r_U,
        x=TestDataRAS.c_U,
        y=TestDataRAS.yz,
        v=TestDataRAS.vz,
        n=5,
        include_e_v=True,
    )
    pd.testing.assert_frame_equal(
        U_expected,
        U_test,
        check_exact=False,
        atol=1e-3,
    )
    pd.testing.assert_frame_equal(
        e_expected,
        e_test,
        check_exact=False,
        atol=1e-3,
    )
    pd.testing.assert_frame_equal(
        v_expected,
        v_test,
        check_exact=False,
        atol=1e-3,
    )


def test_hybridize_determine_V(TestDataVUT):
    V_expected = TestDataVUT.V
    foreground = hyb.VUT(V=TestDataVUT.V_for, U=TestDataVUT.U_for)
    background = hyb.VUT(V=TestDataVUT.V_back, U=TestDataVUT.U_back)
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )
    V_test, _, _, _ = HT.hybridize(H=TestDataVUT.H, H1=TestDataVUT.H1)
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=False, atol=1e-4)


def test_hybridize_determine_U(TestDataVUT):
    U_expected = TestDataVUT.U
    foreground = hyb.VUT(V=TestDataVUT.V_for, U=TestDataVUT.U_for)
    background = hyb.VUT(V=TestDataVUT.V_back, U=TestDataVUT.U_back)
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )

    _, U_test, _, _ = HT.hybridize(H=TestDataVUT.H, H1=TestDataVUT.H1)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=False, atol=1e-4)


def test_hybridize_determine_U_with_Vback_negative(TestDataVUT):
    U_expected = TestDataVUT.U_neg
    foreground = hyb.VUT(V=TestDataVUT.V_for_neg, U=TestDataVUT.U_for)
    background = hyb.VUT(V=TestDataVUT.V_back, U=TestDataVUT.U_back)
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )

    _, U_test, _, _ = HT.hybridize(H=TestDataVUT.H, H1=TestDataVUT.H1)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=False, atol=1e-3)


def test_hybridize_determine_F(TestDataVUT):
    F_expected = TestDataVUT.F
    foreground = hyb.VUT(V=TestDataVUT.V_for, U=TestDataVUT.U_for, F=TestDataVUT.F_for)
    background = hyb.VUT(
        V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back
    )
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )

    _, _, F_test, _ = HT.hybridize(
        HF=TestDataVUT.HF, H=TestDataVUT.H, H1=TestDataVUT.H1
    )
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=False, atol=1e-3)


def test_hybridize_determine_F_message(TestDataVUT):
    F_expected = TestDataVUT.F_message
    foreground = hyb.VUT(V=TestDataVUT.V_for, U=TestDataVUT.U_for, F=TestDataVUT.F_for)
    background = hyb.VUT(
        V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back
    )
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )

    _, _, F_test, _ = HT.hybridize(
        HF=TestDataVUT.HF, H=TestDataVUT.H, H1=TestDataVUT.H1, message_exiobase=True
    )
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=False, atol=1e-3)


def test_hybridize_determine_U_message(TestDataVUT):
    U_expected = TestDataVUT.U_message
    foreground = hyb.VUT(V=TestDataVUT.V_for, U=TestDataVUT.U_for)
    background = hyb.VUT(V=TestDataVUT.V_back, U=TestDataVUT.U_back)
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )

    _, U_test, _, _ = HT.hybridize(
        H=TestDataVUT.H, H1=TestDataVUT.H1, message_exiobase=True
    )
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=False, atol=1e-4)


def test_hybridize_determine_U_message_check_neg(TestDataVUT):
    U_expected = TestDataVUT.U_message
    foreground = hyb.VUT(V=TestDataVUT.V_for, U=TestDataVUT.U_for)
    background = hyb.VUT(V=TestDataVUT.V_back, U=TestDataVUT.U_back)
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )

    _, U_test, _, _ = HT.hybridize(
        H=TestDataVUT.H,
        H1=TestDataVUT.H1,
        message_exiobase=True,
        check_negative_U=True,
    )
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=False, atol=1e-4)


def test_hybridize_determine_Q_back_given(TestDataVUT):
    ext_f_Q = pd.MultiIndex.from_arrays(
        [["carbon dioxide"], ["kg"]], names=["extension", "unit"]
    )
    HF_Q = pd.DataFrame(
        np.array([[0], [1]]).astype(float), index=TestDataVUT.ext_b_Q, columns=ext_f_Q
    )
    Q_back = pd.DataFrame(
        np.array([[0, 1], [1 / 1000000, 10]]).astype(float),
        index=TestDataVUT.imp_b_Q,
        columns=TestDataVUT.ext_b_Q,
    )

    Q_expected = pd.DataFrame(
        np.array([[1, 0, 1], [10, 1 / 1000000, 10]]).astype(float),
        index=TestDataVUT.imp_b_Q,
        columns=ext_f_Q.append(TestDataVUT.ext_b_Q),
    )

    foreground = hyb.VUT()
    background = hyb.VUT(Q=Q_back)
    HT = hyb.HybridTables(
        foreground=foreground,
        background=background,
    )

    _, _, _, Q_test = HT.hybridize(HF=HF_Q)

    pd.testing.assert_frame_equal(Q_expected, Q_test)


def test_aggregate_region_for(TestDataVUT):
    mapping_reg = {"New": ["reg1", "reg2"]}

    ix_f_agg = pd.MultiIndex.from_product(
        [["New"], TestDataVUT.ind_f], names=["region", "industry"]
    )
    co_f_agg = pd.MultiIndex.from_arrays(
        [["New", "New"], TestDataVUT.com_f, ["EUR", "EUR"]],
        names=["region", "commodity", "unit"],
    )

    V_expected = pd.DataFrame(
        np.array([[160, 0], [0, 120]]).astype(float),
        index=ix_f_agg,
        columns=co_f_agg,
    )
    U_expected = pd.DataFrame(
        np.array([[0, 5], [37, 0]]).astype(float), index=co_f_agg, columns=ix_f_agg
    )
    F_expected = pd.DataFrame(
        np.array([[30, 20], [6, 8]]).astype(float),
        index=TestDataVUT.ext_f_multiple,
        columns=ix_f_agg,
    )

    foreground = hyb.VUT(
        V=TestDataVUT.V_for, U=TestDataVUT.U_for, F=TestDataVUT.F_for_multiple
    )
    HT = hyb.HybridTables(foreground=foreground)

    V_test, U_test, F_test = HT.foreground.aggregate(mapping_reg=mapping_reg)
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=True)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=True)
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=True)


def test_aggregate_region_com_back(TestDataVUT):
    mapping_reg = {"New": ["reg1", "reg2"]}
    mapping_com = {"aa": ["a", "c"], "bb": ["b"]}

    ix_b_agg = pd.MultiIndex.from_product(
        [["New"], TestDataVUT.ind_b], names=["region", "industry"]
    )
    co_b_agg = pd.MultiIndex.from_arrays(
        [["New", "New"], ["aa", "bb"], ["EUR", "EUR"]],
        names=["region", "commodity", "unit"],
    )

    V_expected = pd.DataFrame(
        np.array([[200, 0], [0, 130]]).astype(float),
        index=ix_b_agg,
        columns=co_b_agg,
    )
    U_expected = pd.DataFrame(
        np.array([[10, 30], [55, 0]]).astype(float), index=co_b_agg, columns=ix_b_agg
    )
    F_expected = pd.DataFrame(
        np.array([[8000, 10000], [900, 1100]]).astype(float),
        index=TestDataVUT.ext_b,
        columns=ix_b_agg,
    )

    background = hyb.VUT(
        V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back
    )
    HT = hyb.HybridTables(background=background)

    V_test, U_test, F_test = HT.background.aggregate(
        mapping_reg=mapping_reg, mapping_com=mapping_com
    )
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=True)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=True)
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=True)


def test_aggregate_com_back(TestDataVUT):
    mapping_com = {"aa": ["a", "c"], "bb": ["b"]}

    co_b_agg = pd.MultiIndex.from_arrays(
        [
            ["reg1", "reg1", "reg2", "reg2"],
            ["aa", "bb", "aa", "bb"],
            ["EUR", "EUR", "EUR", "EUR"],
        ],
        names=["region", "commodity", "unit"],
    )

    V_expected = pd.DataFrame(
        np.array([[110, 0, 0, 0], [0, 60, 0, 0], [0, 0, 90, 0], [0, 0, 0, 70]]).astype(
            float
        ),
        index=TestDataVUT.ix_b,
        columns=co_b_agg,
    )
    U_expected = pd.DataFrame(
        np.array([[10, 15, 0, 5], [30, 0, 0, 0], [0, 0, 0, 10], [5, 0, 20, 0]]).astype(
            float
        ),
        index=co_b_agg,
        columns=TestDataVUT.ix_b,
    )
    F_expected = TestDataVUT.F_back.copy()

    background = hyb.VUT(
        V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back
    )
    HT = hyb.HybridTables(background=background)

    V_test, U_test, F_test = HT.background.aggregate(mapping_com=mapping_com)
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=True)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=True)
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=True)


def test_aggregate_ind_back(TestDataVUT):
    mapping_ind = {"neu": ["A", "B"]}

    ix_b_agg = pd.MultiIndex.from_arrays(
        [
            ["reg1", "reg2"],
            ["neu", "neu"],
        ],
        names=["region", "industry"],
    )

    V_expected = pd.DataFrame(
        np.array([[100, 60, 10, 0, 0, 0], [0, 0, 0, 80, 70, 10]]).astype(float),
        index=ix_b_agg,
        columns=TestDataVUT.co_b,
    )
    U_expected = pd.DataFrame(
        np.array([[20, 5], [30, 0], [5, 0], [0, 5], [5, 20], [0, 5]]).astype(float),
        index=TestDataVUT.co_b,
        columns=ix_b_agg,
    )
    F_expected = pd.DataFrame(
        np.array([[7000, 11000], [1000, 1000]]).astype(float),
        index=TestDataVUT.ext_b,
        columns=ix_b_agg,
    )

    background = hyb.VUT(
        V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back
    )
    HT = hyb.HybridTables(background=background)

    V_test, U_test, F_test = HT.background.aggregate(mapping_ind=mapping_ind)
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=True)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=True)
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=True)


def test_aggregate_reg_com_ind_back(TestDataVUT):
    mapping_ind = {"neu": ["A", "B"]}
    mapping_com = {"aa": ["a", "c"], "bb": ["b"]}
    mapping_reg = {"New": ["reg1", "reg2"]}

    ix_b_agg = pd.MultiIndex.from_arrays(
        [
            ["New"],
            ["neu"],
        ],
        names=["region", "industry"],
    )
    co_b_agg = pd.MultiIndex.from_arrays(
        [
            ["New", "New"],
            ["aa", "bb"],
            ["EUR", "EUR"],
        ],
        names=["region", "commodity", "unit"],
    )
    V_expected = pd.DataFrame(
        np.array([[200, 130]]).astype(float),
        index=ix_b_agg,
        columns=co_b_agg,
    )
    U_expected = pd.DataFrame(
        np.array([[40], [55]]).astype(float),
        index=co_b_agg,
        columns=ix_b_agg,
    )
    F_expected = pd.DataFrame(
        np.array([[18000], [2000]]).astype(float),
        index=TestDataVUT.ext_b,
        columns=ix_b_agg,
    )

    background = hyb.VUT(
        V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back
    )
    HT = hyb.HybridTables(background=background)

    V_test, U_test, F_test = HT.background.aggregate(
        mapping_reg=mapping_reg, mapping_com=mapping_com, mapping_ind=mapping_ind
    )
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=True)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=True)
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=True)


def test_monetize_forground(TestDataVUT):
    V_expected = pd.DataFrame(
        np.array(
            [[900, 0, 0, 0], [0, 100, 0, 0], [0, 0, 140, 0], [0, 0, 0, 700]]
        ).astype(float),
        index=TestDataVUT.ix_f,
        columns=TestDataVUT.co_f,
    )

    U_expected = pd.DataFrame(
        np.array([[0, 0, 0, 50], [60, 0, 0, 0], [0, 0, 0, 0], [20, 0, 50, 0]]).astype(
            float
        ),
        index=TestDataVUT.co_f,
        columns=TestDataVUT.ix_f,
    )

    p = pd.DataFrame(
        np.array([[10], [2], [2], [10]]).astype(float),
        index=TestDataVUT.co_f,
        columns=["value"],
    )

    foreground = hyb.VUT(V=TestDataVUT.V_for, U=TestDataVUT.U_for)

    V_test, U_test = foreground.monetize(price_vector=p)
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=True)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=True)


def test_harmonize_inds_coms_in_regions(TestDataVUT):
    ix_harmo = pd.MultiIndex.from_tuples(
        [("reg1", "ind1"), ("reg1", "ind2"), ("reg2", "ind1"), ("reg2", "ind2")],
        names=("region", "industry"),
    )

    co_harmo = pd.MultiIndex.from_tuples(
        [
            ("reg1", "com1", "EUR"),
            ("reg1", "com2", "EUR"),
            ("reg2", "com1", "EUR"),
            ("reg2", "com2", "EUR"),
        ],
        names=("region", "commodity", "unit"),
    )

    V_expected = pd.DataFrame(
        np.array([[0, 0, 0, 0], [0, 0, 0, 0], [100, 0, 0, 0], [0, 140, 0, 0]]).astype(
            float
        ),
        index=ix_harmo,
        columns=co_harmo,
    )

    U_expected = pd.DataFrame(
        np.array([[0, 0, 0, 0], [60, 0, 0, 0], [20, 0, 0, 50], [0, 0, 0, 0]]).astype(
            float
        ),
        index=co_harmo,
        columns=ix_harmo,
    )

    F_expected = pd.DataFrame(
        np.array([[20, 0, 10, 10], [2, 0, 4, 4]]).astype(float),
        index=TestDataVUT.ext_f_multiple,
        columns=ix_harmo,
    )

    foreground = hyb.VUT(
        V=TestDataVUT.V_not_harmo, U=TestDataVUT.U_not_harmo, F=TestDataVUT.F_not_harmo
    )

    V_test, U_test, F_test = foreground.harmonize_inds_coms_in_regions()
    pd.testing.assert_frame_equal(V_expected, V_test, check_exact=True)
    pd.testing.assert_frame_equal(U_expected, U_test, check_exact=True)
    pd.testing.assert_frame_equal(F_expected, F_test, check_exact=True)


def test_calc_Z_y_industry_comxcom(TestDataVUT):
    Z_I_cxc = pd.DataFrame(
        np.array(
            [
                [8.7024793, 8.75, 0, 5, 0.1487603, 0.25, 0.1487603, 0, 0, 0],
                [30, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4.375, 0, 0, 0, 0, 0, 0],
                [
                    4.9008264,
                    0,
                    19.259259,
                    0,
                    0.0495868,
                    0,
                    0.0495868,
                    0.3703704,
                    0,
                    0.3703704,
                ],
                [
                    0.8181818,
                    0.8333333,
                    0,
                    0,
                    0.0909091,
                    0.1666667,
                    0.0909091,
                    0,
                    0,
                    0,
                ],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 4.1666667, 0, 0, 0, 0.8333333, 0, 0, 0, 0],
                [0, 0, 0, 0.625, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
            ]
        ),
        index=TestDataVUT.co_f.append(TestDataVUT.co_b),
        columns=TestDataVUT.co_f.append(TestDataVUT.co_b),
    )

    y_I_c = pd.DataFrame(
        np.array([[67], [20], [65.625], [45], [8], [10], [5], [9.375], [0], [5]]),
        index=TestDataVUT.co_f.append(TestDataVUT.co_b),
    )

    total = hyb.VUT(V=TestDataVUT.V, U=TestDataVUT.U)

    Z_test, y_test = total.calc_Z_y(
        tech_assumption="industry", requirements="com-by-com"
    )
    pd.testing.assert_frame_equal(Z_I_cxc, Z_test, check_exact=False, atol=1e-2)
    pd.testing.assert_frame_equal(y_I_c, y_test, check_exact=False, atol=1e-2)


def test_calc_Z_y_industry_indxind(TestDataVUT):
    Z_I_ixi = pd.DataFrame(
        np.array(
            [
                [8.7024793, 8.75, 0, 5, 0.2975207, 0.25, 0, 0],
                [30, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4.375, 0, 0, 0, 0],
                [4.9008264, 0, 19.259259, 0, 0.0991736, 0, 0.7407407, 0],
                [0.8181818, 5, 0, 0, 0.1818182, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 5.625, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
        index=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
        columns=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )

    y_I_i = pd.DataFrame(
        np.array([[67], [20], [65.625], [45], [13], [10], [14.375], [0]]),
        index=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )
    total = hyb.VUT(V=TestDataVUT.V, U=TestDataVUT.U)

    Z_test, y_test = total.calc_Z_y(
        tech_assumption="industry", requirements="ind-by-ind"
    )
    pd.testing.assert_frame_equal(Z_I_ixi, Z_test, check_exact=False, atol=1e-2)
    pd.testing.assert_frame_equal(y_I_i, y_test, check_exact=False, atol=1e-2)


def test_calc_F_mult_per_com_and_ind_based_on_F_ind(TestDataVUT):
    F_mult_c = pd.DataFrame(
        np.array(
            [
                [0.09, 0.13, 0.48, 0.18, 0.15, 0.02, 0.15, 0.01, 0, 0.01],
                [0.20, 0.22, 0.09, 0.33, 0.41, 0.85, 0.41, 3.86, 0, 3.86],
            ]
        ),
        index=TestDataVUT.int_F,
        columns=TestDataVUT.co_f.append(TestDataVUT.co_b),
    )
    F_mult_i = pd.DataFrame(
        np.array(
            [
                [0.09, 0.13, 0.48, 0.18, 0.15, 0.02, 0.01, 0],
                [0.20, 0.22, 0.09, 0.33, 0.41, 0.85, 3.86, 0],
            ]
        ),
        index=TestDataVUT.int_F,
        columns=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )
    total = hyb.VUT(V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_ind)

    F_mult_c_test = total.calc_F_mult(
        tech_assumption="industry", raw_factors="per-ind", multipliers="per-com"
    )
    F_mult_i_test = total.calc_F_mult(
        tech_assumption="industry", raw_factors="per-ind", multipliers="per-ind"
    )
    pd.testing.assert_frame_equal(F_mult_c, F_mult_c_test, check_exact=False, atol=1e-2)
    pd.testing.assert_frame_equal(F_mult_i, F_mult_i_test, check_exact=False, atol=1e-2)


def test_calc_F_mult_per_com_and_ind_based_on_F_com(TestDataVUT):
    F_mult_c_expected = pd.DataFrame(
        np.array(
            [
                [0.37, 0.21, 0.06, 0.06, 0.61, 8.90, 0.91, 2.90, 0, 0.10],
                [0.47, 0.89, 0.12, 0.19, 8.79, 0.18, 0.29, 0.11, 0, 0.71],
            ]
        ),
        index=TestDataVUT.int_F,
        columns=TestDataVUT.co_f.append(TestDataVUT.co_b),
    )
    F_mult_i_expected = pd.DataFrame(
        np.array(
            [
                [0.12, 0.15, 0.02, 0.06, 0.01, 0.10, 0.00, 0],
                [0.43, 0.25, 0.05, 0.09, 0.09, 0.18, 0.01, 0],
            ]
        ),
        index=TestDataVUT.int_F,
        columns=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )
    total = hyb.VUT(V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_com)

    F_mult_c_test = total.calc_F_mult(
        tech_assumption="industry", raw_factors="per-com", multipliers="per-com"
    )
    F_mult_i_test = total.calc_F_mult(
        tech_assumption="industry", raw_factors="per-com", multipliers="per-ind"
    )
    pd.testing.assert_frame_equal(
        F_mult_c_expected, F_mult_c_test, check_exact=False, atol=1e-2
    )
    pd.testing.assert_frame_equal(
        F_mult_i_expected, F_mult_i_test, check_exact=False, atol=1e-2
    )


def test_calc_Q_mult_per_com_and_ind_based_on_F_ind(TestDataVUT):
    Q_mult_c_expected = pd.DataFrame(
        np.array(
            [
                [0.85, 1.3, 4.78, 1.79, 1.54, 0.17, 1.54, 0.07, 0, 0.07],
                [0.19, 0.24, 0.52, 0.35, 0.36, 0.44, 0.36, 1.94, 0, 1.94],
            ]
        ),
        index=TestDataVUT.imp_Q,
        columns=TestDataVUT.co_f.append(TestDataVUT.co_b),
    )
    Q_mult_i_expected = pd.DataFrame(
        np.array(
            [
                [0.85, 1.3, 4.78, 1.79, 1.54, 0.17, 0.07, 0],
                [0.19, 0.24, 0.52, 0.34, 0.36, 0.44, 1.94, 0],
            ]
        ),
        index=TestDataVUT.imp_Q,
        columns=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )
    total = hyb.VUT(
        V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_ind, Q=TestDataVUT.Q_calc_F
    )

    Q_mult_c_test = total.calc_F_mult(
        tech_assumption="industry",
        raw_factors="per-ind",
        multipliers="per-com",
        impacts=True,
    )
    Q_mult_i_test = total.calc_F_mult(
        tech_assumption="industry",
        raw_factors="per-ind",
        multipliers="per-ind",
        impacts=True,
    )
    pd.testing.assert_frame_equal(
        Q_mult_c_expected, Q_mult_c_test, check_exact=False, atol=1e-2
    )
    pd.testing.assert_frame_equal(
        Q_mult_i_expected, Q_mult_i_test, check_exact=False, atol=1e-2
    )


def test_calc_Q_mult_contr_per_com_based_on_F_ind(TestDataVUT):
    imp_Q_cont = pd.MultiIndex.from_product(
        [
            TestDataVUT.imp_Q.tolist(),
            TestDataVUT.co_f.append(TestDataVUT.co_b).tolist(),
        ],
        names=["impact", "per commodity (or industry)"],
    )
    Q_mult_contr_per_com = pd.DataFrame(
        np.array(
            [
                [
                    0.264439936,
                    0.396659904,
                    0.017783188,
                    0.094843671,
                    0.076420715,
                    0,
                    0,
                    0,
                ],
                [
                    0.046683626,
                    1.070025439,
                    0.003276204,
                    0.017473085,
                    0.164867286,
                    0,
                    0,
                    0,
                ],
                [
                    0.005303843,
                    0.007955765,
                    4.361284307,
                    0.403040112,
                    0.001532762,
                    0,
                    0,
                    0,
                ],
                [
                    0.01927743,
                    0.028916146,
                    0.274667961,
                    1.464895792,
                    0.005571001,
                    0,
                    0,
                    0,
                ],
                [
                    0.004066375,
                    0.006099562,
                    0.001641456,
                    0.008754429,
                    1.514936613,
                    0,
                    0,
                    0,
                ],
                [
                    0.007017636,
                    0.010526454,
                    0.000608725,
                    0.003246535,
                    0.153404179,
                    0,
                    0,
                    0,
                ],
                [
                    0.004066375,
                    0.006099562,
                    0.001641456,
                    0.008754429,
                    1.514936613,
                    0,
                    0,
                    0,
                ],
                [
                    0.000713979,
                    0.001070968,
                    0.010172887,
                    0.0542554,
                    0.000206333,
                    0,
                    0,
                    0,
                ],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [
                    0.000713979,
                    0.001070968,
                    0.010172887,
                    0.0542554,
                    0.000206333,
                    0,
                    0,
                    0,
                ],
                [
                    0.079331981,
                    0.067432184,
                    0.001778319,
                    0.009484367,
                    0.0178315,
                    0,
                    0.010269791,
                    0,
                ],
                [
                    0.014005088,
                    0.181904325,
                    0.00032762,
                    0.001747309,
                    0.038469034,
                    0,
                    0.001892008,
                    0,
                ],
                [
                    0.001591153,
                    0.00135248,
                    0.436128431,
                    0.040304011,
                    0.000357644,
                    0,
                    0.043641687,
                    0,
                ],
                [
                    0.005783229,
                    0.004915745,
                    0.027466796,
                    0.146489579,
                    0.0012999,
                    0,
                    0.158620748,
                    0,
                ],
                [
                    0.001219912,
                    0.001036926,
                    0.000164146,
                    0.000875443,
                    0.35348521,
                    0,
                    0.000947941,
                    0,
                ],
                [
                    0.002105291,
                    0.001789497,
                    6.08725e-05,
                    0.000324653,
                    0.035794308,
                    0.4,
                    0.000351539,
                    0,
                ],
                [
                    0.001219912,
                    0.001036926,
                    0.000164146,
                    0.000875443,
                    0.35348521,
                    0,
                    0.000947941,
                    0,
                ],
                [
                    0.000214194,
                    0.000182065,
                    0.001017289,
                    0.00542554,
                    4.81444e-05,
                    0,
                    1.930874843,
                    0,
                ],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [
                    0.000214194,
                    0.000182065,
                    0.001017289,
                    0.00542554,
                    4.81444e-05,
                    0,
                    1.930874843,
                    0,
                ],
            ]
        ),
        index=imp_Q_cont,
        columns=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )
    total = hyb.VUT(
        V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_ind, Q=TestDataVUT.Q_calc_F
    )

    Q_mult_contr_test = total.calc_F_mult(
        tech_assumption="industry",
        raw_factors="per-ind",
        multipliers="per-com",
        impacts=True,
        contribution={"category": [""], "com_or_ind": ["a*", "b*", "a", "b", "c"]},
    )
    pd.testing.assert_frame_equal(
        Q_mult_contr_per_com,
        Q_mult_contr_test,
        check_exact=False,
        atol=1e-4,
    )


def test_calc_Q_mult_contr_per_com_based_on_F_ind_COM_CHOICE(TestDataVUT):
    com_b_choice = ["b", "c"]
    reg = ["reg1", "reg2"]
    unit_com = ["EUR"]
    co_b = pd.MultiIndex.from_product(
        [reg, com_b_choice, unit_com], names=["region", "commodity", "unit"]
    )

    imp_Q_cont = pd.MultiIndex.from_product(
        [
            TestDataVUT.imp_Q.tolist(),
            TestDataVUT.co_f.append(co_b).tolist(),
        ],
        names=["impact", "per commodity (or industry)"],
    )
    Q_mult_contr_per_com_CHOICE = pd.DataFrame(
        np.array(
            [
                [
                    0.264439936,
                    0.396659904,
                    0.017783188,
                    0.094843671,
                    0.076420715,
                    0,
                    0,
                    0,
                ],
                [
                    0.046683626,
                    1.070025439,
                    0.003276204,
                    0.017473085,
                    0.164867286,
                    0,
                    0,
                    0,
                ],
                [
                    0.005303843,
                    0.007955765,
                    4.361284307,
                    0.403040112,
                    0.001532762,
                    0,
                    0,
                    0,
                ],
                [
                    0.01927743,
                    0.028916146,
                    0.274667961,
                    1.464895792,
                    0.005571001,
                    0,
                    0,
                    0,
                ],
                [
                    0.007017636,
                    0.010526454,
                    0.000608725,
                    0.003246535,
                    0.153404179,
                    0,
                    0,
                    0,
                ],
                [
                    0.004066375,
                    0.006099562,
                    0.001641456,
                    0.008754429,
                    1.514936613,
                    0,
                    0,
                    0,
                ],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [
                    0.000713979,
                    0.001070968,
                    0.010172887,
                    0.0542554,
                    0.000206333,
                    0,
                    0,
                    0,
                ],
                [
                    0.079331981,
                    0.067432184,
                    0.001778319,
                    0.009484367,
                    0.0178315,
                    0,
                    0.010269791,
                    0,
                ],
                [
                    0.014005088,
                    0.181904325,
                    0.00032762,
                    0.001747309,
                    0.038469034,
                    0,
                    0.001892008,
                    0,
                ],
                [
                    0.001591153,
                    0.00135248,
                    0.436128431,
                    0.040304011,
                    0.000357644,
                    0,
                    0.043641687,
                    0,
                ],
                [
                    0.005783229,
                    0.004915745,
                    0.027466796,
                    0.146489579,
                    0.0012999,
                    0,
                    0.158620748,
                    0,
                ],
                [
                    0.002105291,
                    0.001789497,
                    6.08725e-05,
                    0.000324653,
                    0.035794308,
                    0.4,
                    0.000351539,
                    0,
                ],
                [
                    0.001219912,
                    0.001036926,
                    0.000164146,
                    0.000875443,
                    0.35348521,
                    0,
                    0.000947941,
                    0,
                ],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [
                    0.000214194,
                    0.000182065,
                    0.001017289,
                    0.00542554,
                    4.81444e-05,
                    0,
                    1.930874843,
                    0,
                ],
            ]
        ),
        index=imp_Q_cont,
        columns=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )
    total = hyb.VUT(
        V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_ind, Q=TestDataVUT.Q_calc_F
    )

    Q_mult_contr_test = total.calc_F_mult(
        tech_assumption="industry",
        raw_factors="per-ind",
        multipliers="per-com",
        impacts=True,
        contribution={"category": [""], "com_or_ind": ["a*", "b*", "b", "c"]},
    )
    pd.testing.assert_frame_equal(
        Q_mult_contr_per_com_CHOICE,
        Q_mult_contr_test,
        check_exact=False,
        atol=1e-4,
    )


def test_convert_unit_back(TestDataVUT):
    unit_com_new = ["thousand EUR"]
    co_b_new = pd.MultiIndex.from_product(
        [TestDataVUT.reg, TestDataVUT.com_b, unit_com_new],
        names=["region", "commodity", "unit"],
    )
    ext_b_new = pd.MultiIndex.from_arrays(
        [["carbon dioxide", "N2O"], ["t", "g"]], names=["extension", "unit"]
    )
    ext_f_new = pd.MultiIndex.from_arrays(
        [["CO2", "CH4"], ["t", "t"]], names=["extension", "unit"]
    )

    V_back_expected = pd.DataFrame(
        np.array(
            [
                [0.100, 0, 0.010, 0, 0, 0],
                [0, 0.060, 0, 0, 0, 0],
                [0, 0, 0, 0.080, 0, 0.010],
                [0, 0, 0, 0, 0.070, 0],
            ]
        ).astype(float),
        index=TestDataVUT.ix_b,
        columns=co_b_new,
    )

    U_back_expected = pd.DataFrame(
        np.array(
            [
                [0.010, 0.010, 0, 0.005],
                [0.030, 0, 0, 0],
                [0, 0.005, 0, 0],
                [0, 0, 0, 0.005],
                [0.005, 0, 0.020, 0],
                [0, 0, 0, 0.005],
            ]
        ).astype(float),
        index=co_b_new,
        columns=TestDataVUT.ix_b,
    )

    F_back_expected = pd.DataFrame(
        np.array([[3, 4, 5, 6], [500, 500, 400, 600]]).astype(float),
        index=ext_b_new,
        columns=TestDataVUT.ix_b,
    )
    back = hyb.VUT(V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back)

    V_back_test = back.convert_unit(current="EUR", to="thousand EUR", matrix="V")
    U_back_test = back.convert_unit(current="EUR", to="thousand EUR", matrix="U")
    F_back_test = back.convert_unit(current="kg", to="t", matrix="F")
    pd.testing.assert_frame_equal(V_back_expected, V_back_test, check_exact=True)
    pd.testing.assert_frame_equal(U_back_expected, U_back_test, check_exact=True)
    pd.testing.assert_frame_equal(
        F_back_expected, F_back_test, check_exact=False, atol=1e-4
    )


def test_convert_unit_F_not_unique_units(TestDataVUT):
    ext_b_new = pd.MultiIndex.from_arrays(
        [["carbon dioxide", "N2O"], ["t", "g"]], names=["extension", "unit"]
    )
    ext_f_new = pd.MultiIndex.from_arrays(
        [["CO2", "CH4"], ["t", "t"]], names=["extension", "unit"]
    )
    F_multiple_expected = pd.DataFrame(
        np.array(
            [
                [0.020, 0.010, 0.010, 0.010, 0, 0, 0, 0],
                [2, 4, 4, 4, 0, 0, 0, 0],
                [0, 0, 0, 0, 0.001, 0, 0, 0],
                [0, 0, 0, 0, 30, 40, 40, 40],
            ]
        ).astype(float),
        index=ext_f_new.append(ext_b_new),
        columns=TestDataVUT.ix_f.append(TestDataVUT.ix_b),
    )
    total = hyb.VUT(F=TestDataVUT.F_multiple)

    F_test = total.convert_unit(current="kg", to="t", matrix="F")
    pd.testing.assert_frame_equal(
        F_multiple_expected, F_test, check_exact=False, atol=1e-4
    )


def test_convert_unit_back_with_factor(TestDataVUT):
    unit_com_new = ["thousand EUR"]
    co_b_new = pd.MultiIndex.from_product(
        [TestDataVUT.reg, TestDataVUT.com_b, unit_com_new],
        names=["region", "commodity", "unit"],
    )
    ext_b_new = pd.MultiIndex.from_arrays(
        [["carbon dioxide", "N2O"], ["t", "g"]], names=["extension", "unit"]
    )
    ext_f_new = pd.MultiIndex.from_arrays(
        [["CO2", "CH4"], ["t", "t"]], names=["extension", "unit"]
    )

    V_back_expected = pd.DataFrame(
        np.array(
            [
                [0.100, 0, 0.010, 0, 0, 0],
                [0, 0.060, 0, 0, 0, 0],
                [0, 0, 0, 0.080, 0, 0.010],
                [0, 0, 0, 0, 0.070, 0],
            ]
        ).astype(float),
        index=TestDataVUT.ix_b,
        columns=co_b_new,
    )

    U_back_expected = pd.DataFrame(
        np.array(
            [
                [0.010, 0.010, 0, 0.005],
                [0.030, 0, 0, 0],
                [0, 0.005, 0, 0],
                [0, 0, 0, 0.005],
                [0.005, 0, 0.020, 0],
                [0, 0, 0, 0.005],
            ]
        ).astype(float),
        index=co_b_new,
        columns=TestDataVUT.ix_b,
    )

    F_back_expected = pd.DataFrame(
        np.array([[3, 4, 5, 6], [500, 500, 400, 600]]).astype(float),
        index=ext_b_new,
        columns=TestDataVUT.ix_b,
    )
    back = hyb.VUT(V=TestDataVUT.V_back, U=TestDataVUT.U_back, F=TestDataVUT.F_back)

    V_back_test = back.convert_unit(
        current="EUR", to="thousand EUR", matrix="V", factor=1 / 1000
    )
    U_back_test = back.convert_unit(
        current="EUR", to="thousand EUR", matrix="U", factor=1 / 1000
    )
    F_back_test = back.convert_unit(current="kg", to="t", matrix="F", factor=1 / 1000)
    pd.testing.assert_frame_equal(V_back_expected, V_back_test, check_exact=True)
    pd.testing.assert_frame_equal(U_back_expected, U_back_test, check_exact=True)
    pd.testing.assert_frame_equal(
        F_back_expected, F_back_test, check_exact=False, atol=1e-4
    )


def test_convert_unit_Q(TestDataVUT):
    imp_b_Q = pd.MultiIndex.from_arrays(
        [["impact_A", "impact_B"], ["kg CO2-eq.", "M.EUR"]],
        names=["impact", "unit"],
    )
    ext_b_Q_new = pd.MultiIndex.from_arrays(
        [["value added", "CO2"], ["EUR", "kg"]], names=["extension", "unit"]
    )
    Q_back_expected = pd.DataFrame(
        np.array([[0, 1], [1 / 1000000, 10]]).astype(float),
        index=imp_b_Q,
        columns=ext_b_Q_new,
    )
    back = hyb.VUT(Q=TestDataVUT.Q_back, U=TestDataVUT.U)

    back.Q = back.convert_unit(
        current="M.EUR", to="EUR", matrix="Q", factor=1 / 1000000
    )
    Q_back_test = back.convert_unit(current="t", to="kg", matrix="Q")

    pd.testing.assert_frame_equal(Q_back_expected, Q_back_test, check_exact=True)


from hybridvut.tools.units import demonetize_F_mult


def test_demonetize_F_mult(TestDataVUT):
    F_mult_c = pd.DataFrame(
        np.array(
            [
                [0.09, 0.13, 0.48, 0.18, 0.15, 0.02, 0.15, 0.01, 0, 0.01],
                [0.20, 0.22, 0.09, 0.33, 0.41, 0.85, 0.41, 3.86, 0, 3.86],
            ]
        ),
        index=TestDataVUT.int_F,
        columns=TestDataVUT.co_f.append(TestDataVUT.co_b),
    )

    F_mult_c_expected = pd.DataFrame(
        np.array(
            [
                [0.9, 0.26, 0.96, 1.8, 0.30, 0.2, 0.15, 0.01, 0, 0.01],
                [2.0, 0.44, 0.18, 3.3, 0.82, 8.5, 0.41, 3.86, 0, 3.86],
            ]
        ),
        index=TestDataVUT.int_F,
        columns=pd.MultiIndex.from_arrays(
            [
                [
                    "reg1",
                    "reg1",
                    "reg2",
                    "reg2",
                    "reg1",
                    "reg1",
                    "reg1",
                    "reg2",
                    "reg2",
                    "reg2",
                ],
                ["a*", "b*", "a*", "b*", "a", "b", "c", "a", "b", "c"],
                [
                    "kWh",
                    "kWh",
                    "kWh",
                    "kWh",
                    "kWh",
                    "kWh",
                    "kWh",
                    "kWh",
                    "kWh",
                    "kWh",
                ],
            ],
            names=["region", "commodity", "unit"],
        ),
    )
    price_vector = pd.DataFrame(
        np.array([[10], [2], [2], [10], [2], [10], [1], [1], [2], [1]]).astype(float),
        index=pd.MultiIndex.from_arrays(
            [
                [
                    "reg1",
                    "reg1",
                    "reg2",
                    "reg2",
                    "reg1",
                    "reg1",
                    "reg1",
                    "reg2",
                    "reg2",
                    "reg2",
                ],
                ["a*", "b*", "a*", "b*", "a", "b", "c", "a", "b", "c"],
                [
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                    "EUR/kWh",
                ],
            ],
            names=["region", "commodity", "unit"],
        ),
        columns=["value"],
    )

    F_mult_test = demonetize_F_mult(F_mult_c, price_vector)
    pd.testing.assert_frame_equal(F_mult_c_expected, F_mult_test)


def test_calc_footprint_consumption(TestDataVUT):
    total = hyb.VUT(V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_ind)

    footprint_test = total.calc_footprint(
        responsibility="consumption",
        raw_factors="per-ind",
    )
    pd.testing.assert_frame_equal(
        TestDataVUT.footprint_consumption,
        footprint_test,
        check_exact=False,
        atol=1e-4,
    )


def test_calc_footprint_income(TestDataVUT):
    total = hyb.VUT(V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_ind)

    footprint_test = total.calc_footprint(
        responsibility="income",
        raw_factors="per-ind",
    )
    pd.testing.assert_frame_equal(
        TestDataVUT.footprint_income,
        footprint_test,
        check_exact=False,
        atol=1e-4,
    )


def test_calc_footprint_production(TestDataVUT):
    total = hyb.VUT(V=TestDataVUT.V, U=TestDataVUT.U, F=TestDataVUT.F_ind)

    footprint_test = total.calc_footprint(
        responsibility="production",
        raw_factors="per-ind",
    )
    pd.testing.assert_frame_equal(
        TestDataVUT.footprint_production,
        footprint_test,
        check_exact=False,
        atol=1e-4,
    )
