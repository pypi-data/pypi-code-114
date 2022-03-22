import pandas as pd
import numpy as np

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def aggregate(self, mapping_reg=None, mapping_com=None, mapping_ind=None):
    """Aggregate regions of the specified system and according to regional mapping."""

    # Create regional aggregation matrix S_reg
    if mapping_reg is not None:
        S_reg = pd.DataFrame(
            0.0,
            index=mapping_reg.keys(),
            columns=sorted(set(v for val in mapping_reg.values() for v in val)),
        )
        for k, v in mapping_reg.items():
            S_reg.at[k, v] = 1.0
    else:
        reg = self.V.columns.unique(level=0)
        S_reg = pd.DataFrame(np.identity(len(reg)), index=reg, columns=reg)

    # Create total aggregation matrix S_C (commodties)
    if mapping_com is not None:
        S_com = pd.DataFrame(
            0.0,
            index=mapping_com.keys(),
            columns=sorted(set(v for val in mapping_com.values() for v in val)),
        )
        for k, v in mapping_com.items():
            S_com.at[k, v] = 1.0
    else:
        com = self.V.columns.unique(level=1)
        S_com = pd.DataFrame(np.identity(len(com)), index=com, columns=com)

    # Create total aggregation matrix S_I (industries)
    if mapping_ind is not None:
        S_ind = pd.DataFrame(
            0.0,
            index=mapping_ind.keys(),
            columns=sorted(set(v for val in mapping_ind.values() for v in val)),
        )
        for k, v in mapping_ind.items():
            S_ind.at[k, v] = 1.0
    else:
        ind = self.V.index.unique(level=1)
        S_ind = pd.DataFrame(np.identity(len(ind)), index=ind, columns=ind)

    unit = self.V.columns.unique(level=2)  # presumes consistent units in V+U

    C_c = pd.MultiIndex.from_product(
        [S_reg.index.tolist(), S_com.index.tolist(), unit],
        names=["region", "commodity", "unit"],
    )
    C_i = pd.MultiIndex.from_product(
        [S_reg.columns.tolist(), S_com.columns.tolist(), unit],
        names=["region", "commodity", "unit"],
    )
    I_i = pd.MultiIndex.from_product(
        [S_reg.index.tolist(), S_ind.index.tolist()], names=["region", "industry"]
    )
    I_c = pd.MultiIndex.from_product(
        [S_reg.columns.tolist(), S_ind.columns.tolist()],
        names=["region", "industry"],
    )
    S_C = pd.DataFrame(np.kron(S_reg, S_com), index=C_c, columns=C_i)
    S_I = pd.DataFrame(np.kron(S_reg, S_ind), index=I_i, columns=I_c)

    V = S_I.dot(self.V).dot(S_C.transpose())
    U = S_C.dot(self.U).dot(S_I.transpose())
    if self.F is not None:
        F = self.F.dot(S_I.transpose())
    else:
        F = None

    if self.F_Y is not None:
        cat = self.F_Y.columns.unique(level=1)
        S_cat = pd.DataFrame(np.identity(len(cat)), index=cat, columns=cat)
        I_cat = pd.MultiIndex.from_product(
            [S_reg.columns.tolist(), S_cat.columns.tolist()],
            names=["region", "demand category"],
        )
        I_i = pd.MultiIndex.from_product(
            [S_reg.index.tolist(), S_cat.index.tolist()],
            names=["region", "demand category"],
        )
        S_CAT = pd.DataFrame(np.kron(S_reg, S_cat), index=I_i, columns=I_cat)
        F_Y = self.F_Y.dot(S_CAT.transpose())
        self.F_Y = F_Y

    self.V = V
    self.U = U
    self.F = F

    if self.F_Y is None:
        return V, U, F
    else:
        return V, U, F, F_Y


def monetize(self, price_vector):
    """Monetize the Make and Use tables of a system.

    Currently only for dataframes without unit index.
    """

    V = self.V
    U = self.U

    ones_ind = pd.DataFrame(np.ones((V.shape[0], 1)), index=V.index, columns=["value"])
    U_mon = U.multiply(price_vector.dot(ones_ind.transpose()))
    V_mon = V.multiply(ones_ind.dot(price_vector.transpose()))

    self.V = V_mon
    self.U = U_mon

    return V_mon, U_mon


def harmonize_inds_coms_in_regions(self):
    """Harmonize the number of commodities and industries among regions."""
    # Check number of commodities and industries
    # (examplary on V, since equvilance is assumed)
    shape_i = self.V.index.levshape
    shape_c = self.V.columns.levshape
    if shape_i[1] / shape_i[0] == 0 or shape_c[1] / shape_c[0] == 0:
        logger.info(
            "No harmonization necessary - indsutries and commodities in all regions identical"
        )
        return
    else:
        reg = list(self.U.columns.append(self.V.index).unique(level=0))
        com = list(self.V.columns.append(self.U.index).unique(level=1))
        ind = list(self.V.index.append(self.U.columns).unique(level=1))
        unit_c = list(self.U.index.unique(level=2))

        new_com = pd.MultiIndex.from_product(
            [reg, com, unit_c], names=("region", "commodity", "unit")
        )
        new_ind = pd.MultiIndex.from_product([reg, ind], names=("region", "industry"))

        V = self.V.reindex(index=new_ind, columns=new_com, fill_value=0.0)
        U = self.U.reindex(index=new_com, columns=new_ind, fill_value=0.0)
        F = self.F.reindex(columns=new_ind, fill_value=0.0)
        self.V = V
        self.U = U
        self.F = F
        return V, U, F
    return
