import pandas as pd
import numpy as np

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def calc_Z_y(self, tech_assumption="industry", requirements="com-by-com"):
    """This function calculates the transaction matrix Z and final demand y.

    This is done only based on the hybridized Make and Use Tables.
    TODO: Allow Commodity technology assumption!
    """
    if self.V is None or self.U is None:
        logger.warning(
            "No Z and y calculated. First determine hybridized Make matrix V and Use matrix U"
        )
        return
    else:
        x = self.V.sum(axis=1)
        q = self.V.sum(axis=0)
        x_diag = (
            pd.DataFrame(np.diag(1 / x), index=x.index, columns=x.index)
            .fillna(0)
            .replace(np.inf, 0)
        )
        q_diag = (
            pd.DataFrame(np.diag(1 / q), index=q.index, columns=q.index)
            .fillna(0)
            .replace(np.inf, 0)
        )
        C = self.V.transpose().dot(x_diag)
        D = self.V.dot(q_diag)
        if tech_assumption == "industry":
            if requirements == "com-by-com":
                Z = self.U.dot(C.transpose())
                y = q - Z.sum(axis=1)
                y = y.to_frame()
            elif requirements == "ind-by-ind":
                Z = D.dot(self.U)
                y = x - Z.sum(axis=1)
                y = y.to_frame()

    return Z, y


def calc_F_mult(
    self,
    tech_assumption="industry",
    raw_factors="per-ind",
    multipliers="per-com",
    impacts=False,
    contribution=None,
):
    """This function calculates the Factor multipliers for the hybridized system.

    The equations are used from Lenzen and Rueda-Cantuche (2012):
    'A note on the use of supply-use tables in impact analyses'
    TODO: Implement 'commodity' and 'mixed' tech_assumptions for Factor matrix.
    """
    if self.V is None or self.U is None or self.F is None:
        logger.warning(
            "No multipliers calculated. First determine hybridized matrices V, U and F"
        )
        return
    else:
        x = self.V.sum(axis=1)
        q = self.V.sum(axis=0)
        x_diag = (
            pd.DataFrame(np.diag(1 / x), index=x.index, columns=x.index)
            .fillna(0)
            .replace(np.inf, 0)
        )
        q_diag = (
            pd.DataFrame(np.diag(1 / q), index=q.index, columns=q.index)
            .fillna(0)
            .replace(np.inf, 0)
        )
        B = self.U.dot(x_diag)
        D = self.V.dot(q_diag)
        if tech_assumption == "industry":
            # for interventions per industry:
            if raw_factors == "per-ind":
                F = self.F.dot(x_diag)
                I = pd.DataFrame(
                    np.identity(self.U.shape[1]),
                    index=self.U.columns,
                    columns=self.U.columns,
                )
                L = pd.DataFrame(
                    np.linalg.inv((I - D.dot(B)).values),
                    index=self.U.columns,
                    columns=self.U.columns,
                )
                if multipliers == "per-com":
                    if contribution is not None:
                        # extract strings from list
                        def _give_str(x):
                            for i in x:
                                return i

                        # Filter F and LD according to strings in contribution
                        f = F.loc[
                            F.index.get_level_values(0).str.contains(
                                _give_str(contribution["category"])
                            )
                        ]
                        ld = L.dot(D).transpose()
                        ld = ld[
                            np.in1d(
                                ld.index.get_level_values(1), contribution["com_or_ind"]
                            )
                        ]
                        # determine new indices
                        ix = pd.MultiIndex.from_product(
                            [f.index.tolist(), ld.index.tolist()],
                            names=["intervention", "per commodity"],
                        )
                        co = f.columns.copy()
                        # Repeat values in accordance to selected filters
                        F_repeated = pd.DataFrame(
                            np.repeat(f.values, len(ld.index), axis=0),
                            index=ix,
                            columns=co,
                        )
                        LD_repeated = pd.DataFrame(
                            np.matlib.repmat(ld.values, len(f.index), 1),
                            index=ix,
                            columns=co,
                        )

                        F_mult = F_repeated.multiply(LD_repeated)
                    else:
                        F_mult = F.dot(L).dot(D)
                elif multipliers == "per-ind":
                    if contribution is not None:
                        # extract strings from list
                        def _give_str(x):
                            for i in x:
                                return i

                        # Filter F and L according to strings in contribution
                        f = F.loc[
                            F.index.get_level_values(0).str.contains(
                                _give_str(contribution["category"])
                            )
                        ]
                        l = L.transpose()
                        l = l[
                            np.in1d(
                                l.index.get_level_values(1), contribution["com_or_ind"]
                            )
                        ]
                        # determine new indices
                        ix = pd.MultiIndex.from_product(
                            [f.index.tolist(), l.index.tolist()],
                            names=["intervention", "per industry"],
                        )
                        co = f.columns.copy()
                        # Repeat values in accordance to selected filters
                        F_repeated = pd.DataFrame(
                            np.repeat(f.values, len(l.index), axis=0),
                            index=ix,
                            columns=co,
                        )
                        L_repeated = pd.DataFrame(
                            np.matlib.repmat(l.values, len(f.index), 1),
                            index=ix,
                            columns=co,
                        )
                        F_mult = F_repeated.multiply(L_repeated)
                    else:
                        F_mult = F.dot(L)
            # for interventions per commodity:
            elif raw_factors == "per-com":
                F = self.F.dot(q_diag)
                I = pd.DataFrame(
                    np.identity(self.U.shape[0]),
                    index=self.U.index,
                    columns=self.U.index,
                )
                L = pd.DataFrame(
                    np.linalg.inv((I - B.dot(D)).values),
                    index=self.U.index,
                    columns=self.U.index,
                )
                if multipliers == "per-ind":
                    F_mult = F.dot(L).dot(B)
                elif multipliers == "per-com":
                    F_mult = F.dot(L)
            # to determine impact- instead of intervention-multipliers:
            if impacts is True:
                try:
                    if contribution is not None:
                        # Filter Q according to selected interventions
                        q_filtered = self.Q.filter(
                            items=F_mult.index.get_level_values(0).unique()
                        )
                        # Repeat rows and columns according to selected commodities/industries and Diagonalize characterization factors
                        q_repeated = np.kron(
                            q_filtered, np.eye(len(F_mult.index.levels[1]))
                        )
                        # Create Q_repeated
                        ix_q = pd.MultiIndex.from_product(
                            [
                                self.Q.index.tolist(),
                                F_mult.index.get_level_values(1).unique(),
                            ],
                            names=["impact", "per commodity (or industry)"],
                        )
                        Q_repeated = pd.DataFrame(
                            q_repeated, index=ix_q, columns=F_mult.index
                        )
                        F_mult = Q_repeated.dot(F_mult)
                    else:
                        F_mult = self.Q.dot(F_mult)
                except AttributeError:
                    logger.warning(
                        "Only intervention-multipliers are calculated. To calculate impact-multipliers, define Q matrix!"
                    )
            return F_mult
        return
    return


def calc_footprint(
    self,
    responsibility="consumption",
    raw_factors="per-ind",
    multipliers="per-ind",
    sum_over_sectors=True,
):
    """Calculates footprints of countries depending on responsibility perspective."""

    if self.V is None or self.U is None or self.F is None:
        logger.warning("No footprints calculated. First determine matrices V, U and F")
        return
    else:
        x = self.V.sum(axis=1)
        q = self.V.sum(axis=0)
        x_diag = (
            pd.DataFrame(np.diag(1 / x), index=x.index, columns=x.index)
            .fillna(0)
            .replace(np.inf, 0)
        )
        q_diag = (
            pd.DataFrame(np.diag(1 / q), index=q.index, columns=q.index)
            .fillna(0)
            .replace(np.inf, 0)
        )
        B = self.U.dot(x_diag)
        D = self.V.dot(q_diag)
    if raw_factors == "per-ind":
        if responsibility == "consumption":
            if multipliers == "per-ind":
                I = pd.DataFrame(
                    np.identity(self.U.shape[1]),
                    index=self.U.columns,
                    columns=self.U.columns,
                )
                L = pd.DataFrame(
                    np.linalg.inv((I - D.dot(B)).values),
                    index=self.U.columns,
                    columns=self.U.columns,
                )
                y = (I - D.dot(B)).dot(x)
                y_diag = (
                    pd.DataFrame(np.diag(y), index=y.index, columns=y.index)
                    .fillna(0)
                    .replace(np.inf, 0)
                )
                if sum_over_sectors == True:
                    footprint = self.F.dot(x_diag).dot(L).dot(y_diag)
                else:
                    y_rep = pd.DataFrame(
                        np.tile(y.values, (self.F.shape[0], 1)),
                        index=self.F.index,
                        columns=y.index,
                    )
                    footprint = self.F.dot(x_diag).dot(L).multiply(y_rep)
            if multipliers == "per-com":
                I = pd.DataFrame(
                    np.identity(self.U.shape[0]),
                    index=self.U.index,
                    columns=self.U.index,
                )
                L = pd.DataFrame(
                    np.linalg.inv((I - B.dot(D)).values),
                    index=self.U.index,
                    columns=self.U.index,
                )
                y = (I - B.dot(D)).dot(q)
                y_diag = (
                    pd.DataFrame(np.diag(y), index=y.index, columns=y.index)
                    .fillna(0)
                    .replace(np.inf, 0)
                )
                if sum_over_sectors == True:
                    footprint = self.F.dot(x_diag).dot(D).dot(L).dot(y_diag)
                else:
                    y_rep = pd.DataFrame(
                        np.tile(y.values, (self.F.shape[0], 1)),
                        index=self.F.index,
                        columns=y.index,
                    )
                    footprint = self.F.dot(x_diag).dot(D).dot(L).multiply(y_rep)

        elif responsibility == "income":
            v = self.V.sum(axis=1) - self.U.sum(axis=0)
            I = pd.DataFrame(
                np.identity(self.U.shape[1]),
                index=self.U.columns,
                columns=self.U.columns,
            )
            G = pd.DataFrame(
                np.linalg.inv((I - x_diag.dot(D.dot(self.U))).values),
                index=self.U.columns,
                columns=self.U.columns,
            )
            v_diag = (
                pd.DataFrame(np.diag(v), index=v.index, columns=v.index)
                .fillna(0)
                .replace(np.inf, 0)
            )
            if sum_over_sectors == True:
                footprint = (
                    v_diag.dot(G).dot(x_diag.dot(self.F.transpose())).transpose()
                )
            else:
                v_rep = pd.DataFrame(
                    np.tile(v.values, (self.F.shape[0], 1)).transpose(),
                    index=v.index,
                    columns=self.F.index,
                )
                footprint = v_rep.multiply(
                    G.dot(x_diag.dot(self.F.transpose()))
                ).transpose()
        elif responsibility == "production":
            footprint = self.F.copy()

        if sum_over_sectors == True:
            footprint = footprint.sum(level=0, axis=1)

    elif raw_factors == "per-com":
        raise NotImplementedError("To be done")

    if self.F_Y is not None:
        if sum_over_sectors == True:
            footprint_Y = self.F_Y.sum(level=1, axis=1)
            footprint = footprint + footprint_Y
        else:
            if multipliers == "per-com":
                _F_Y = self.F_Y.transpose()
                _F_Y["unit"] = self.U.index.get_level_values(2)[0]
                _F_Y.set_index("unit", append=True, inplace=True)
                _F_Y.reorder_levels(["region", "demand category", "unit"])
                footprint = footprint.transpose().append(_F_Y).transpose()
            else:
                footprint = (
                    footprint.transpose().append(self.F_Y.transpose()).transpose()
                )

    return footprint
