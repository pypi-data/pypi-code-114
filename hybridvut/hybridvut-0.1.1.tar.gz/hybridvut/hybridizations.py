import numpy as np
import pandas as pd
import numpy.matlib
import logging
import numpy.linalg

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# main function
def hybridize(
    self,
    H=None,
    H1=None,
    HF=None,
    message_exiobase=False,
    check_negative_U=False,
    delete_trade_in_reg=None,
    RAS=False,
):
    """Hybridize the foreground and background sytems.

    V and U are determined based on V_back, U_back, V_for and U_for.
    The hybridization procedure assumes that the background system
    fully represents the world economy.
    TODO: Replace hard-coding when setting emissions of Exiobase to zero.
    """
    if self.foreground.V is not None and self.background.V is not None:
        e_for = self.foreground.V.sum(axis=0) - self.foreground.U.sum(axis=1)
        e_back = self.background.V.sum(axis=0) - self.background.U.sum(axis=1)
    if H is not None and H1 is not None:
        x_for = self.foreground.V.sum(axis=1)
        q_for = self.foreground.V.sum(axis=0)
        q_back = self.background.V.sum(axis=0)

        # Transform 1s of Concordance matrices into weighting factors
        # if multiple assignments
        if H is not None and H1 is not None and self.background.V is not None:
            # multiple foreground industries in background industry
            _A1 = H.dot(x_for).to_frame().to_numpy()
            _x1 = self.foreground.V.sum(1).to_frame().to_numpy()
            _x1_repeated = pd.DataFrame(
                np.matlib.repmat(_x1.transpose(), H.shape[0], 1),
                index=H.index.copy(),
                columns=H.columns.copy(),
            )
            _B1 = H.multiply(_x1_repeated)
            _A1_repeated = pd.DataFrame(
                np.matlib.repmat(_A1, 1, H.shape[1]),
                index=H.index.copy(),
                columns=H.columns.copy(),
            )
            H = _B1 / _A1_repeated
            H.replace(np.inf, 0, inplace=True)
            H.fillna(0, inplace=True)
            # multiple foreground commodities in background commodity
            _A1 = q_for.transpose().dot(H1).to_frame().to_numpy().transpose()
            _q1 = self.foreground.V.sum(0).to_frame().to_numpy()
            _q1_repeated = pd.DataFrame(
                np.matlib.repmat(_q1, 1, H1.shape[1]),
                index=H1.index.copy(),
                columns=H1.columns.copy(),
            )
            _B1 = H1.multiply(_q1_repeated)
            _A1_repeated = pd.DataFrame(
                np.matlib.repmat(_A1, H1.shape[0], 1),
                index=H1.index.copy(),
                columns=H1.columns.copy(),
            )
            H1 = _B1 / _A1_repeated
            H1.replace(np.inf, 0, inplace=True)
            H1.fillna(0, inplace=True)

            # Delete all entries in H, H1 for those no production occured
            ind_i = x_for.where(x_for == 0).dropna()
            for i in ind_i.index:
                H.loc[:, i] = 0

            col_i = q_for.where(q_for == 0).dropna()
            for c in col_i.index:
                H1.loc[c, :] = 0

        # If message_exiobase is True, remove 'final|...' commodities and aggregated industries (trp, rc, fs, i, nc) from message
        if message_exiobase is True:
            coms_del = "useful"
            techs_del = [
                "biomass_i",
                "coal_i",
                "elec_i",
                "eth_i",
                "foil_i",
                "gas_i",
                "heat_i",
                "hp_el_i",
                "hp_gas_i",
                "loil_i",
                "meth_i",
                "solar_i",
                "coal_trp",
                "elec_trp",
                "eth_fc_trp",
                "eth_ic_trp",
                "foil_trp",
                "gas_trp",
                "loil_trp",
                "meth_fc_trp",
                "meth_ic_trp",
                "biomass_rc",
                "coal_rc",
                "elec_rc",
                "eth_rc",
                "foil_rc",
                "gas_rc",
                "heat_rc",
                "hp_el_rc",
                "hp_gas_rc",
                "loil_rc",
                "meth_rc",
                "solar_rc",
                "coal_fs",
                "foil_fs",
                "gas_fs",
                "loil_fs",
                "methanol_fs",
                "biomass_nc",
            ]
            self.foreground.U.loc[
                (
                    slice(None),
                    self.foreground.U.index.get_level_values(1).str.contains(coms_del),
                ),
                :,
            ] = 0.0
            self.foreground.V.loc[
                :,
                (
                    slice(None),
                    self.foreground.V.columns.get_level_values(1).str.contains(
                        coms_del
                    ),
                ),
            ] = 0.0
            self.foreground.U.loc[
                :,
                (
                    slice(None),
                    self.foreground.U.columns.get_level_values(1).str.contains(
                        "|".join(techs_del)
                    ),
                ),
            ] = 0.0
            self.foreground.V.loc[
                (
                    slice(None),
                    self.foreground.V.index.get_level_values(1).str.contains(
                        "|".join(techs_del)
                    ),
                ),
                :,
            ] = 0.0

        # Adjust U_back
        U_back_adj = self.background.U - H1.transpose().dot(self.foreground.U).dot(
            H.transpose()
        )

        # if message_exiobase True, determine q_for and q_back based on U and e
        if message_exiobase is True:
            com_for = self.foreground.V.columns
            com_back = self.background.V.columns
            ind_for = self.foreground.V.index
            ind_back = self.background.V.index

            # scale e
            _e = pd.Series(1, index=com_back)
            _t1_for = (
                pd.DataFrame(np.diag(q_for), index=com_for, columns=com_for)
                .dot(H1)
                .dot(_e)
            )
            _t1_back = H1.dot(
                pd.DataFrame(np.diag(q_back), index=com_back, columns=com_back)
            ).dot(_e)
            t1 = _t1_for.div(_t1_for + _t1_back)
            t1.fillna(0, inplace=True)

            e_for = t1.multiply(H1.dot(e_back))
            e_back_adj = e_back.dot(H1.transpose()).dot(e_for)

            # determine q based on U and e
            q_for_new = self.foreground.U.sum(1) + e_for
            q_back_new = U_back_adj.sum(1) + e_back_adj

            # scale V
            _Ones_for = pd.DataFrame(1, index=ind_for, columns=com_for)
            _Ones_back = pd.DataFrame(1, index=ind_back, columns=com_back)
            _q_ratio_for = q_for_new.div(q_for)
            _q_ratio_for.fillna(0, inplace=True)
            _q_ratio_back = q_back_new.div(q_back)
            _q_ratio_back.fillna(0, inplace=True)
            self.foreground.V = self.foreground.V.multiply(
                _Ones_for.dot(
                    pd.DataFrame(np.diag(_q_ratio_for), index=com_for, columns=com_for)
                )
            )
            self.background.V = self.background.V.multiply(
                _Ones_back.dot(
                    pd.DataFrame(
                        np.diag(_q_ratio_back), index=com_back, columns=com_back
                    )
                )
            )

            q_for = q_for_new.copy()
            q_back_adj = q_back_new.copy()
            # determine x based on V
            x_for = self.foreground.V.sum(1)
            x_back_adj = self.background.V.sum(1)

        # Calculate q and x based on V
        V_back_adj = self.background.V - H.dot(self.foreground.V).dot(H1)
        V_back_adj[V_back_adj < 0] = 0  # set negative values to zero

        if (
            message_exiobase is True
        ):  # Set associated background commodities to zero (is covered by foreground)
            _, com_back_i = np.where(H1 > 0)
            com_i = []
            for c in com_back_i:
                com_i.append(H1.columns[c])
            for c in com_i:
                V_back_adj.loc[:, c] = 0
            # Set associated background industries to zero
            ind_back_i, _ = np.where(H > 0)
            ind_i = []
            for i in ind_back_i:
                ind_i.append(H.index[i])
            for i in ind_i:
                V_back_adj.loc[i, :] = 0

        x_back_adj = V_back_adj.sum(axis=1)
        q_back_adj = V_back_adj.sum(axis=0)

        # Define Theta (T) and Theta* (T1)
        com_back = self.background.V.columns
        ind_back = self.background.V.index
        com_for = self.foreground.V.columns
        ind_for = self.foreground.V.index
        _E = pd.DataFrame(1, index=com_back, columns=ind_back)
        _T_for = _E.dot(H).dot(
            pd.DataFrame(np.diag(x_for), index=ind_for, columns=ind_for)
        )
        _T_back = _E.dot(
            pd.DataFrame(np.diag(x_back_adj), index=ind_back, columns=ind_back)
        ).dot(H)
        T = _T_for.div(_T_for + _T_back)
        T.fillna(0, inplace=True)

        _T1_for = (
            pd.DataFrame(np.diag(q_for), index=com_for, columns=com_for).dot(H1).dot(_E)
        )
        _T1_back = H1.dot(
            pd.DataFrame(np.diag(q_back_adj), index=com_back, columns=com_back)
        ).dot(_E)
        T1 = _T1_for.div(_T1_for + _T1_back)
        T1.fillna(0, inplace=True)

        # Calculate C_u and adjust U_back
        C_u = T.multiply(U_back_adj.dot(H))
        U_back_adj1 = U_back_adj - (C_u.dot(H.transpose()))

        # Calculate C_d and adjust U_back a second time
        C_d = T1.multiply(H1.dot(U_back_adj1))
        U_back_adj2 = U_back_adj1 - (H1.transpose()).dot(C_d)

        # Correct C_u, C_d, and U_for
        corect_term1 = C_u.multiply(H1.transpose().dot(T1).dot(H))
        corect_term2 = C_d.multiply(H1.dot(T).dot(H.transpose()))

        C_u_adj = C_u - corect_term1
        C_d_adj = C_d - corect_term2
        U_for_adj = self.foreground.U + H1.dot(corect_term1) + corect_term2.dot(H)

        # Delete all commodities that are covered by foreground system
        if message_exiobase is True:
            _, com_back_i = np.where(H1 > 0)
            com_i = []
            for c in com_back_i:
                com_i.append(H1.columns[c])
            for c in com_i:
                U_back_adj2.loc[c, :] = 0
                C_u_adj.loc[c, :] = 0
            # Set associated background industries to zero
            ind_back_i, _ = np.where(H > 0)
            ind_i = []
            for i in ind_back_i:
                ind_i.append(H.index[i])
            for i in ind_i:
                # not for all transport
                if i[1] not in [
                    "Transport via railways",
                    "Other land transport",
                    "Sea and coastal water transport",
                    "Inland water transport",
                ]:
                    U_back_adj2.loc[:, i] = 0
                    C_d_adj.loc[:, i] = 0

        # Create V and U of the hybridized system
        V = pd.DataFrame(
            {}, index=ind_for.append(ind_back), columns=com_for.append(com_back)
        )
        V.update(V_back_adj)
        V.update(self.foreground.V.copy())
        V.fillna(0, inplace=True)

        U = pd.DataFrame(
            {}, index=com_for.append(com_back), columns=ind_for.append(ind_back)
        )
        U.update(U_back_adj2)
        U.update(U_for_adj)
        U.update(C_d_adj)
        U.update(C_u_adj)
        U.fillna(0, inplace=True)
    else:
        V = None
        U = None
        logger.warning(
            "V and U will not be hybridized - concordance matrices H and H1 are not defined"
        )

    # Adjust Extension matrix
    if HF is not None and H is not None:
        F_back = self.background.F.copy()
        # Scale CO2, N2O and CH4 in background system
        if message_exiobase is not False and F_back.size > 1000:  # includes dummy check
            CO2_new = self.foreground.F.loc["emis|CO2"].sum(1).sum()
            CH4_new = self.foreground.F.loc["emis|CH4"].sum(1).sum()
            N2O_new = self.foreground.F.loc["emis|N2O"].sum(1).sum()

            CO2_old = F_back.loc["CO2 - combustion - air"].sum(1).sum()
            CH4_categories = [
                "CH4 - combustion - air",
                "CH4 - non combustion - Extraction/production of (natural) gas - air",
                "CH4 - non combustion - Extraction/production of crude oil - air",
                "CH4 - non combustion - Mining of antracite - air",
                "CH4 - non combustion - Mining of bituminous coal - air",
                "CH4 - non combustion - Mining of coking coal - air",
                "CH4 - non combustion - Mining of lignite (brown coal) - air",
                "CH4 - non combustion - Mining of sub-bituminous coal - air",
                "CH4 - non combustion - Oil refinery - air",
            ]
            CH4_old = F_back[F_back.index.isin(CH4_categories, level=0)].sum(1).sum()
            N2O_old = F_back.loc["N2O - combustion - air"].sum(1).sum()

            F_back_CO2_new = F_back.loc["CO2 - combustion - air"].apply(
                lambda x: np.multiply(x, (CO2_new / CO2_old))
            )
            F_back_CO2_new.index = pd.MultiIndex.from_arrays(
                [
                    ["CO2 - combustion - air"],
                    [F_back.loc["CO2 - combustion - air"].index[0]],
                ],
                names=("intervention", "unit"),
            )
            F_back.update(F_back_CO2_new)
            F_back[F_back.index.isin(CH4_categories, level=0)] = F_back[
                F_back.index.isin(CH4_categories, level=0)
            ] * (CH4_new / CH4_old)
            F_back_NO2_new = F_back.loc["N2O - combustion - air"].apply(
                lambda x: np.multiply(x, (N2O_new / N2O_old))
            )
            F_back_NO2_new.index = pd.MultiIndex.from_arrays(
                [
                    ["N2O - combustion - air"],
                    [F_back.loc["N2O - combustion - air"].index[0]],
                ],
                names=("intervention", "unit"),
            )
            F_back.update(F_back_NO2_new)

        # Adjust F_back first time
        F_back_adj = F_back - HF.dot(self.foreground.F).dot(H.transpose())

        # Define Theta** (T2) and Theta*** (T3)
        ext_for = self.foreground.F.index
        ext_back = self.background.F.index
        ind_for = self.foreground.V.index
        ind_back = self.background.V.index
        k_for = self.foreground.F.sum(axis=1)
        k_back = self.background.F.sum(axis=1)
        x_for = self.foreground.V.sum(axis=1)
        if H1 is None:
            x_back_adj = self.background.V.sum(axis=1)

        _E1 = pd.DataFrame(1, index=ext_back, columns=ind_back)
        _T2_for = _E1.dot(H).dot(
            pd.DataFrame(np.diag(x_for), index=ind_for, columns=ind_for)
        )
        _T2_back = _E1.dot(
            pd.DataFrame(np.diag(x_back_adj), index=ind_back, columns=ind_back)
        ).dot(H)
        T2 = _T2_for.div(_T2_for + _T2_back)
        T2.fillna(0, inplace=True)

        # There might be additional steps to finalize the hybridization for F.
        # This would be fully equivalent to the hybridization of U.
        # However, since the interpretation of F_d is difficult (does it make sense
        # to allocate emissions based on the ratios of total emissions k_for, k_back?
        # -> guess NO).
        # _T3_for = (
        #    pd.DataFrame(np.diag(k_for), index=ext_for, columns=ext_for)
        #    .dot(HF.transpose())
        #    .dot(_E1)
        # )
        # _T3_back = (
        #    HF.transpose()
        #    .dot(pd.DataFrame(np.diag(k_back), index=ext_back, columns=ext_back))
        #    .dot(_E1)
        # )
        # T3 = _T3_for.div(_T3_for + _T3_back)
        # T3.fillna(0, inplace=True)

        # Determine F_u and adjuest F_back second time
        F_u = T2.multiply(F_back_adj.dot(H))
        F_back_adj1 = F_back_adj - F_u.dot(H.transpose())

        # Determine F_d and adjust F_back third time
        # F_d = T3.multiply(HF.transpose().dot(F_back_adj1))
        # F_back_adj2 = F_back_adj1 - HF.dot(F_d)

        # Correct F_u, F_d and F_for
        # correct_termA = F_u.multiply(HF.dot(T3).dot(H))
        # correct_termB = F_d.multiply(HF.transpose().dot(T2).dot(H.transpose()))

        # F_u_adj = F_u - correct_termA
        # F_d_adj = F_d - correct_termB
        # F_for_adj = (
        #    self.F_for + HF.transpose().dot(correct_termA) + correct_termB.dot(H)
        # )

        # Put everything together
        F = pd.DataFrame(
            {}, index=ext_for.append(ext_back), columns=ind_for.append(ind_back)
        )
        # F.update(F_back_adj2)
        # F.update(F_for_adj)
        # F.update(F_u_adj)
        # F.update(F_d_adj)
        F.update(self.foreground.F.copy())
        F.update(F_back_adj1)
        F.update(F_u)
        F.fillna(0, inplace=True)

        # Set energy related emissions in background to zero
        if HF is not None and H is not None:
            if (
                message_exiobase is not False and F_back.size > 1000
            ):  # includes dummy check
                # Set associated background industries to zero
                ind_back_i, _ = np.where(H > 0)
                ind_i = []
                for i in ind_back_i:
                    ind_i.append(H.index[i])
                for i in ind_i:
                    # not for all transport
                    if i[1] not in [
                        "Transport via railways",
                        "Other land transport",
                        "Sea and coastal water transport",
                        "Inland water transport",
                    ]:
                        F.loc[:, i] = 0
    else:
        F = None
        logger.warning(
            "Factor matrix will not be hybridized - concordance matrices HF and H are not defined"
        )

    self.total.V = V
    self.total.U = U
    self.total.F = F

    # Delete traded commodities between regions
    if delete_trade_in_reg is not None:
        logger.info("Deletion of trade in Matrix U is carried out.")
        y = self.total.V.sum(axis=0) - self.total.U.sum(
            axis=1
        )  # demand based on standard algorithm
        v = self.total.V.sum(axis=1) - self.total.U.sum(
            axis=0
        )  # value added based on standard alg.
        for key, value in delete_trade_in_reg.items():
            for i in value:
                U.at[key, i] = 0
        self.total.U = U

    # Delete negative values in U AND Use the value added from F for v
    if message_exiobase is True:
        logger.info("Hybridization is carried out for message_exiobase")
        # Use q and x from V
        q = self.total.V.sum(axis=0)
        x = self.total.V.sum(axis=1)
        # Delete negative values in U
        U = self.total.U.copy()
        U[U < 0] = 0
        self.total.U = U
        # Calc preliminary v
        v = x - self.total.U.sum(axis=0)
        # Use value added from F
        value_added = [
            "Taxes less subsidies on products purchased: Total",
            "Other net taxes on production",
            "Compensation of employees; wages, salaries, & employers' social contributions: Low-skilled",
            "Compensation of employees; wages, salaries, & employers' social contributions: Medium-skilled",
            "Compensation of employees; wages, salaries, & employers' social contributions: High-skilled",
            "Operating surplus: Consumption of fixed capital",
            "Operating surplus: Rents on land",
            "Operating surplus: Royalties on resources",
            "Operating surplus: Remaining net operating surplus",
        ]
        try:
            # Use value added from F
            v_new = self.total.F.loc[value_added].sum(axis=0)
            # Connect transport background commodities to foreground technologies
            mapping_region = []
            for region_back in H.index.get_level_values(0).unique():
                for region_for in H.columns.get_level_values(0).unique():
                    if H.loc[region_back, region_for].sum().sum() > 0:
                        mapping_region.append((region_back, region_for))
            U = self.total.U.copy()
            for com in U.index:
                for ind in U.columns:
                    if (
                        ind[1]
                        in [
                            "biomass_t_d|M1",
                            "coal_t_d|M1",
                            "loil_t_d|M1",
                            "meth_t_d|M1",
                            "lh2_t_d|M1",
                        ]
                        and com[1]
                        in [
                            "Railway transportation services",
                            "Other land transportation services",
                        ]
                        and (com[0], ind[0]) in mapping_region
                    ):
                        U.at[com, ind] = 0.15 * x.loc[ind]
                    if (
                        ind[1] in ["eth_t_d|M1", "foil_t_d|M1", "h2_t_d|M1"]
                        and com[1]
                        in [
                            "Other land transportation services",
                            "Transportation services via pipelines",
                        ]
                        and (com[0], ind[0]) in mapping_region
                    ):
                        U.at[com, ind] = 0.15 * x.loc[ind]
                    if (
                        ind[1] in ["gas_t_d_ch4_t_d|M1", "gas_t_d|M1"]
                        and com[1]
                        in ["Distribution services of gaseous fuels through mains"]
                        and (com[0], ind[0]) in mapping_region
                    ):
                        U.at[com, ind] = 0.3 * x.loc[ind]
            self.total.U = U
            # Use new final demand but set negative values to zero
            e = q - self.total.U.sum(1)
            # e[e < 0] = 0
            # Check total sums equality of e and v
            if e.sum() != v_new.sum():
                scaling_e = v_new.sum() / e.sum()
                e = scaling_e * e
            # Calculate new x; adjust V; and q
            x_new = self.total.U.sum(axis=0) + v_new
            scaling_V = x_new / x
            scaling_V.fillna(0, inplace=True)
            V = self.total.V.copy()
            V = V.multiply(scaling_V.to_numpy(), axis=0)
            V.fillna(0, inplace=True)
            q_new = self.total.V.sum(axis=0)
            # RAS U
            if RAS == True:
                U, _, _ = self.total.RAS_U(
                    q=q_new, x=x_new, y=e, v=v_new, n=10000, include_e_v=True
                )  # y=e, y=np.append(e_for.values, e_back_adj.values)

        except AttributeError:
            logger.warning(
                "v vector has not been changed. Check Exiobase version! Value added categories must be the same as in v3.8.1!"
            )
        except KeyError:
            logger.warning(
                "v vector has not been changed. Factor matrix F has not been found!"
            )
        self.total.U = U
        self.total.V = V

    # Check for negative values
    if check_negative_U is True:
        logger.info("Checking for negative values in Matrix U is carried out")
        y = self.total.V.sum(axis=0) - self.total.U.sum(
            axis=1
        )  # demand based on standard algorithm
        v = self.total.V.sum(axis=1) - self.total.U.sum(
            axis=0
        )  # value added based on standard alg.
        U[U < 0] = 0  # set negative values to zero
        diff = (self.total.U - U).values
        if not np.all((diff == 0)):  # Do RAS only if negative values were included
            self.total.U = U
            U = self.total.RAS_U(
                q=V.sum(axis=0),
                x=V.sum(axis=1),  # production based on standard alg.
                y=y,
                v=v,
                n=1000,
            )
            self.total.U = U
            logger.info("Matrix U has been Rased due to negative values.")

    # Create matrix Q
    if self.foreground.Q is None and self.background.Q is not None:
        Q_back = self.background.Q.copy()
        Q_for = Q_back.dot(HF)
        Q = Q_for.merge(Q_back, left_index=True, right_index=True)
    elif self.background.Q is None and self.foreground.Q is not None:
        Q_for = self.foreground.Q.copy()
        Q_back = Q_for.dot(HF.transpose())
        Q = Q_for.merge(Q_back, left_index=True, right_index=True)
    else:
        Q = None
    self.total.Q = Q

    return (
        V,
        U,
        F,
        Q,
        #        H,
        #        H1,
    )  # T, T1, C_d_adj, C_u_adj, U_for_adj, U_back_adj2 #only for detailed testing
