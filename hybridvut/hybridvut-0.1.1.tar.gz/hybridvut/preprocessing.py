import re

import numpy as np
import pandas as pd
import pyam
from pyam.utils import get_variable_components as gvc


def VUT_messageix_from_IAMC(
    df_pyam,
    model,
    scenario,
    year,
    mapping_regions,
    variables_V,
    variables_U,
    flows_not_needed,
    harmonize_inds_coms=True,
):
    """Creates Make (V) and Use (U) matrices from IAMC data.

    This function converts the intertechnology flow of energy products
    of a Integrated Assessment Model into a Make and Use Framework of
    input-output analysis.

    Paramters
    ---------
    df_pyam : pyam.IamDataFrame
        Data to be used in IAMC format
    model : str
        IAMC model
    scenario : str
        IAMC scenario
    year : int
        IAMC year
    mapping_regions : dict
        {'region1': ['subreg_1', 'subreg_2'],}
        Aggregate subregions to one region.
    variables_V : dict (Better list!)
        {'V': ['variable_1', 'variable_2',]}
        Extract data from IAMC variables
    variables_U : dict (Better list!)
        {'U': ['variable_1', 'variable_2']}
        Extract data from IAMC variables
    flows_not_needed : list
         Remove not needed flows manually

    Returns
    -------
    V : pd.DataFrame
        Make matrix (industry x commodity)
    U : pd.DataFrame
        Use matrix (commodity x industry)
    """

    def _extract_data_for_V_or_U(df, variable, year, model, scenario):
        """Step 1: Extract data"""
        df = df.filter(model=model, scenario=scenario, variable=variable, year=year)
        return df

    def _create_mapping(df, flows_not_needed):
        """Step 2: Create mapping"""
        mapping = {}
        for var in df["variable"]:
            if gvc(var, 0) == "in":
                mapping[var] = (
                    gvc(var, [1, 2], join=True),
                    gvc(var, [3, 4], join=True),
                )
            if gvc(var, 0) == "out":
                mapping[var] = (
                    gvc(var, [3, 4], join=True),
                    gvc(var, [1, 2], join=True),
                )
        variables_not_needed = []
        for k in mapping.keys():
            for flow in flows_not_needed:
                if flow in k:
                    variables_not_needed.append(k)
        for var in variables_not_needed:
            del mapping[var]
        return mapping

    def _create_V_or_U_table(df, mapping, mapping_region):
        """Step 3: Create Make or use Table"""
        region = mapping_region
        X = pd.DataFrame.from_dict(
            mapping, orient="index", columns=["source", "target"]
        ).merge(df._data, how="left", left_index=True, right_on="variable")
        X.reset_index(inplace=True)
        X.drop(
            columns=["model", "scenario", "variable", "region", "unit", "year"],
            inplace=True,
        )
        X = X.pivot(index="source", columns="target", values="value").fillna(0)
        X = pd.concat({region: X}, names=["region"])
        X.columns = pd.MultiIndex.from_product([[region], X.columns])
        return X

    # Apply _functions to extract data, map variables and create preliminary dataframes
    d_V = {}
    d_U = {}

    for reg in mapping_regions:
        df = df_pyam.aggregate_region(
            df_pyam.variable, region=reg, subregions=mapping_regions[reg]
        )
        for tabV in variables_V:
            datV = _extract_data_for_V_or_U(
                df=df,
                variable=variables_V[tabV],
                year=year,
                model=model,
                scenario=scenario,
            )
            mapping = _create_mapping(datV, flows_not_needed)
            d_V[f"{tabV}_{reg}"] = _create_V_or_U_table(datV, mapping, reg)
        for tabU in variables_U:
            datU = _extract_data_for_V_or_U(
                df=df,
                variable=variables_U[tabU],
                year=year,
                model=model,
                scenario=scenario,
            )
            mapping = _create_mapping(datU, flows_not_needed)
            d_U[f"{tabU}_{reg}"] = _create_V_or_U_table(datU, mapping, reg)

    # Create Multi-Index for Dataframes V and U
    TECHS_V = pd.MultiIndex.from_arrays(([], []))
    COMMS_V = pd.MultiIndex.from_arrays(([], []))
    for v in d_V:
        TECHS_V = TECHS_V.append(d_V[v].index)
        COMMS_V = COMMS_V.append(d_V[v].columns)

    TECHS_U = pd.MultiIndex.from_arrays(([], []))
    COMMS_U = pd.MultiIndex.from_arrays(([], []))
    for u in d_U:
        TECHS_U = TECHS_U.append(d_U[u].columns)
        COMMS_U = COMMS_U.append(d_U[u].index)

    TECHS = TECHS_V.append(TECHS_U).unique()
    COMMS = COMMS_V.append(COMMS_U).unique()

    V = pd.DataFrame(data={}, index=TECHS, columns=COMMS)
    U = pd.DataFrame(data={}, index=COMMS, columns=TECHS)

    # Update empty V and U with the corresponding values
    for d in d_V:
        V.update(d_V[d])
    V.fillna(0, inplace=True)

    for d in d_U:
        U.update(d_U[d])
    U.fillna(0, inplace=True)

    # Sort columns and rows
    U.sort_index(axis=0, level=0, inplace=True)
    U.sort_index(axis=1, level=0, inplace=True)

    V.sort_index(axis=0, level=0, inplace=True)
    V.sort_index(axis=1, level=0, inplace=True)

    # Add global trade processes
    processes_exp_glo = [
        "oil_exp|M1",
        "LNG_exp|M1",
        "coal_exp|M1",
        "eth_exp|M1",
        "foil_exp|M1",
        "loil_exp|M1",
        "meth_exp|M1",
        "lh2_exp|M1",
        "elec_exp|M1",
    ]
    processes_exp_gas = [
        "gas_exp_afr|M1",
        "gas_exp_cpa|M1",
        "gas_exp_eeu|M1",
        "gas_exp_fsu|M1",
        "gas_exp_lam|M1",
        "gas_exp_mea|M1",
        "gas_exp_nam|M1",
        "gas_exp_nor|M1",
        "gas_exp_pao|M1",
        "gas_exp_pas|M1",
        "gas_exp_sas|M1",
        "gas_exp_weu|M1",
    ]
    processes_exp = processes_exp_glo + processes_exp_gas

    # Add trade commodities to U and V
    regions = [
        "AFR",
        "CPA",
        "EEU",
        "FSU",
        "LAM",
        "MEA",
        "NAM",
        "NOR",
        "PAO",
        "PAS",
        "SAS",
        "WEU",
    ]
    commodities_exp = [
        "export|crudeoil",
        "export|LNG",
        "export|coal",
        "export|ethanol",
        "export|fueloil",
        "export|lightoil",
        "export|methanol",
        "export|lh2",
        "export|electr",
        "piped-gas|gas_afr",
        "piped-gas|gas_cpa",
        "piped-gas|gas_eeu",
        "piped-gas|gas_fsu",
        "piped-gas|gas_lam",
        "piped-gas|gas_mea",
        "piped-gas|gas_nam",
        "piped-gas|gas_nor",
        "piped-gas|gas_pao",
        "piped-gas|gas_pas",
        "piped-gas|gas_sas",
        "piped-gas|gas_weu",
    ]

    commodities_imp = [
        "import|crudeoil",
        "import|LNG",
        "import|coal",
        "import|ethanol",
        "import|fueloil",
        "import|lightoil",
        "import|methanol",
        "import|lh2",
        "import|electr",
        "piped-gas|gas_afr",
        "piped-gas|gas_cpa",
        "piped-gas|gas_eeu",
        "piped-gas|gas_fsu",
        "piped-gas|gas_lam",
        "piped-gas|gas_mea",
        "piped-gas|gas_nam",
        "piped-gas|gas_nor",
        "piped-gas|gas_pao",
        "piped-gas|gas_pas",
        "piped-gas|gas_sas",
        "piped-gas|gas_weu",
    ]

    # Copy values to trade processes
    processes_imp = [
        "oil_imp|M1",
        "LNG_imp|M1",
        "coal_imp|M1",
        "eth_imp|M1",
        "foil_imp|M1",
        "loil_imp|M1",
        "meth_imp|M1",
        "lh2_imp|M1",
        "elec_imp|M1",
        "gas_imp|M1",
    ]

    for r in regions:
        for p in processes_exp:
            for c in commodities_exp:
                try:
                    val = V.at[(r, p), (r, c)]
                    U.at[(r, c), ("Trade", p)] = val
                except:
                    pass  # print(f'In V not both, process {p} and commodity {c}, for region {r}')
        for p1 in processes_imp:
            for c1 in commodities_imp:
                try:
                    val1 = U.at[(r, c1), (r, p1)]
                    if p1 == "gas_imp|M1":
                        r_low = r.lower()  # decapitalize region str
                        V.at[("Trade", f"gas_imp_{r_low}|M1"), (r, c1)] = val1
                    else:
                        V.at[("Trade", p1), (r, c1)] = val1
                except:
                    pass  # print(f' In U not both, process {p} and commodity {c}, for region {r}')

    # Rename processes in 'Trade' region
    # U
    a = U["Trade"].columns.str.replace("exp", "trade")
    index_trade = pd.MultiIndex.from_product(
        [["Trade"], a], names=["region", "industry"]
    )
    b = U.drop("Trade", axis=1, level=0).columns
    index_others = b.set_names(["region", "industry"])
    U.columns = index_others.append(index_trade)
    # V
    a = V.loc["Trade"].index.str.replace("imp", "trade")
    index_trade = pd.MultiIndex.from_product(
        [["Trade"], a], names=["region", "industry"]
    )
    b = V.drop("Trade", axis=0, level=0).index
    index_others = b.set_names(["region", "industry"])
    V.index = index_others.append(index_trade)

    V.columns.set_names(["region", "commodity"], inplace=True)
    U.index.set_names(["region", "commodity"], inplace=True)

    V.fillna(0, inplace=True)
    U.fillna(0, inplace=True)

    # Drop Trade columns from Use and trade rows from Make table which are empty
    for p in U.columns.get_level_values(level=1):
        try:
            total = U[("Trade"), (p)].sum()
            if total == 0.0:
                U.drop((("Trade"), (p)), axis=1, inplace=True)
            else:
                pass
        except:
            pass
    for p in V.index.get_level_values(level=1):
        try:
            total = V.loc[("Trade"), (p)].sum()
            if total == 0.0:
                V.drop((("Trade"), (p)), axis=0, inplace=True)
            else:
                pass
        except:
            pass

    # Sort columns and rows for Trade
    # U.sort_index(axis=0, level=0, inplace=True)
    # U.sort_index(axis=1, level=0, inplace=True)

    # V.sort_index(axis=0, level=0, inplace=True)
    # V.sort_index(axis=1, level=0, inplace=True)

    # Harmonize number of industries and commodities among countries
    if harmonize_inds_coms == True:
        reg = list(
            V.columns.append(U.columns).append(V.index).append(U.index).unique(level=0)
        )
        com = list(V.columns.append(U.index).unique(level=1))
        ind = list(V.index.append(U.columns).unique(level=1))

        new_com = pd.MultiIndex.from_product([reg, com], names=("region", "commodity"))
        new_ind = pd.MultiIndex.from_product([reg, ind], names=("region", "industry"))

        V = V.reindex(index=new_ind, columns=new_com, fill_value=0.0)
        U = U.reindex(index=new_com, columns=new_ind, fill_value=0.0)

    # Sort columns and rows for Trade
    U.sort_index(axis=0, level=0, inplace=True)
    U.sort_index(axis=1, level=0, inplace=True)

    V.sort_index(axis=0, level=0, inplace=True)
    V.sort_index(axis=1, level=0, inplace=True)
    return V, U


def y_messageix_from_V_U(V, U):
    """Calculate final demand y based on V and U.

    In Messageix final demand is equivalent to amount of
    products with level -useful-.
    """
    y = pd.Series(data=0, index=U.index)
    df = V.sum(0) - U.sum(1)
    df = df[
        df.index.get_level_values(1).isin(
            [
                "useful|i_feed",
                "useful|i_spec",
                "useful|i_therm",
                "useful|non-comm",
                "useful|rc_spec",
                "useful|rc_therm",
                "useful|transport",
            ]
        )
    ]
    y.update(df)
    return y


def balance_check_messageix(V, U, y):
    """Check trade balance of products.

    All products those are made should be used.
    Also all exported products should be imported.
    """
    balance_check = V.sum(0) - U.sum(1) - y  # V'*e == U*e + y
    countries = balance_check.index.get_level_values(level=0).unique()
    for c in countries:
        if (
            balance_check.iloc[balance_check.index.get_level_values(0) == c]
            > 0.00000001
        ).any() or (
            balance_check.iloc[balance_check.index.get_level_values(0) == c]
            < -0.00000001
        ).any():
            print(f"WARNING: unbalanced trade in region: {c}")
    return balance_check


def q_messageix_from_V(V):
    """Calculate product output q from Make matrix V"""
    q = V.sum(axis=0)


def x_messageix_from_V(V):
    """Calculate industry output x from Make matrix V"""
    x = V.sum(axis=1)


def p_messageix_from_PRICE_COMMODITY(df, year, multiindex=None):
    """Determines the price vector p from message result.

    Parameters
    ----------
    df: pd.DataFrame
        PRICE_COMMODITY variable of messageix result
    year: int
    multiindex: pd.MultiIndex
        Specifies the index to merge on (to drop not needed commodities)
    Returns
    -------
    p: pd.DataFrame
        Price vector for message commodities
    """
    p = pd.DataFrame({})
    df = df[df["year"] == year]
    p["region"] = df["node"].str.replace("R11_", "")
    p["commodity"] = df[["level", "commodity"]].apply(lambda x: "|".join(x), axis=1)
    p["value"] = df["lvl"]
    p.set_index(["region", "commodity"], inplace=True)
    if multiindex is not None:
        p1 = pd.DataFrame(data={}, index=multiindex)
        p = p1.merge(p, left_index=True, right_index=True, how="left")
        # Use prices of secondary/final commodities for import/export commodities.
        # this is necessary, since no prices for import/export is given by PRICE_COMMODITY
        for reg, com in p.index:
            if "export" in com:
                try:
                    p.loc[(reg, com), "value"] = p.at[
                        (reg, com.replace("export", "final")), "value"
                    ]
                except KeyError:
                    try:
                        p.loc[(reg, com), "value"] = p.at[
                            (reg, com.replace("export", "primary")), "value"
                        ]
                    except KeyError:  # check why this part seems to have no effect!
                        try:
                            p.loc[(reg, com), "value"] = p.at[
                                (reg, com.replace("export", "primary")), "value"
                            ]
                        except KeyError:
                            pass

            elif "import" in com:
                try:
                    p.loc[(reg, com), "value"] = p.at[
                        (reg, com.replace("import", "secondary")), "value"
                    ]
                except KeyError:
                    try:
                        p.loc[(reg, com), "value"] = p.at[
                            (reg, com.replace("import", "primary")), "value"
                        ]
                    except KeyError:
                        pass

            elif "piped-gas" in com:
                try:
                    p.loc[(reg, com), "value"] = p.at[
                        (reg, com.replace(com, "primary|gas")), "value"
                    ]
                except KeyError:
                    try:
                        p.loc[(reg, com), "value"] = p.at[
                            (reg, com.replace(com, "secondary|gas")), "value"
                        ]
                    except KeyError:
                        pass
    # All other commodities are not specified for a region by PRICE_COMMODITY,
    # and can be set to 0
    p.fillna(0, inplace=True)
    return p


def F_messageix_from_IAMC(
    df, model, scenario, year, variables, mapping_regions, multiindex=None
):
    """Creates Environmental extension matrix F for messageix.

    Parameters
    ----------
    df: pyam.IamDataFrame
        Message model results in IAMC format.
    model: str
        Message model name
    scenario: str
        Message scenario name
    year: int
        Model year
    variables: list of str
        e.g. ['emis|CH4|*', 'emis|CO2|*']
        Variable names to consider.
    mapping_regions: dict
        e.g. {'AUT':'R11_AUT', ...}
        To rename regions.
    multiindex: pd.MultiIndex
        If not None, the F matrix is merged on the multiindex.
    Returns
    -------
    F: pd.DataFrame
        Environmental extension matrix F of message model
    """
    filt = df.filter(model=model, scenario=scenario, year=year, variable=variables).data

    interventions = []
    industries = []
    values = []
    regions = []

    # Rename regions
    for row in filt.itertuples():
        for reg_new, reg_old in mapping_regions.items():
            filt.region = filt.region.replace(reg_old, reg_new)

    # Create intermediate lists
    for row in filt.itertuples():
        regions.append(row.region)
        interventions.append(gvc(row.variable, [0, 1], join=True))
        industries.append(gvc(row.variable, [2, 3], join=True))
        values.append(row.value)

    d = {
        "region": regions,
        "industry": industries,
        "intervention": interventions,
        "value": values,
    }

    F = pd.DataFrame(d)
    F = F.pivot(index="intervention", columns=["region", "industry"], values="value")
    F.fillna(0, inplace=True)
    if multiindex is not None:
        F1 = pd.DataFrame(data={}, index=multiindex)
        F = F1.merge(F.transpose(), left_index=True, right_index=True, how="left")
        F.fillna(0, inplace=True)
        F = F.transpose()
    return F


#####  Helper functions for Exiabase data  ####


def exiobase_from_csv(path):
    """Reads Exiobase3.7 data from csv file.

    Applies some restructuring to create a pd.DataFrame in the required format.
    Returns Use Table (com x ind) and Supply Table (com x ind) -> V=S.transpose()
    """
    X = pd.read_csv(path, sep="|", low_memory=False)
    X = pd.DataFrame.from_records(X)
    ix = pd.MultiIndex.from_frame(X.iloc[2:, :3], names=["region", "commodity", "unit"])
    co1 = pd.MultiIndex.from_frame(
        X.iloc[:2, 3:].transpose(), names=["industry", "unit"]
    )
    X.drop(axis=0, index=[0, 1], inplace=True)
    X.drop(axis=1, columns=["Unnamed: 0", "Unnamed: 1", "Unnamed: 2"], inplace=True)
    co2 = list(X.columns.get_level_values(0))
    # Delete numbers from in region levels
    def remove(L):
        patt = "[^A-Za-z]"
        L = [re.sub(patt, "", c) for c in L]
        return L

    co2 = remove(co2)
    co = pd.MultiIndex.from_arrays(
        [list(co1.get_level_values(0)), list(co1.get_level_values(1)), co2],
        names=["industry", "unit", "region"],
    )
    X.index = ix
    X.columns = co
    X = X.reorder_levels(["region", "industry", "unit"], axis=1)
    X = X.droplevel("unit", axis=0)  # Remove unit EUR
    X = X.droplevel("unit", axis=1)  # Remove unit EUR
    return X


def exiobase_to_excel(X, path):
    """Writes Exiobase3.7 data to excel file.

    Parameters
    ----------
    X : pd.DataFrame
    path : string
    """
    writer = pd.ExcelWriter(path, engine="xlsxwriter")
    X.to_excel(writer)
    writer.book.use_zip64()
    writer.save()


def exiobase_Q_from_txt(path_Q, path_unit):
    """Reads Exiobase characterization matrix from txt file.

    Matrix Q allocates impacts to the intervention.
    Parameters
    ----------
    path_Q : str
        path for characterization matrix
    path_unit : str
        path for units of the interventions
    """
    X = pd.read_csv(path_Q, sep="\t", index_col=[0], header=[0])
    units = pd.read_csv(path_unit, "\t")

    ix_int = pd.MultiIndex.from_frame(units, names=["intervention", "unit"])

    impacts = []
    units = []
    for i in X.columns:
        string = i.split("|")
        try:
            impact = string[0] + "|" + string[2] + "|" + string[3]
        except IndexError:
            impact = string[0] + "|" + string[2]
        unit = string[1]
        impacts.append(impact)
        units.append(unit)
    ix_imp = pd.MultiIndex.from_arrays([impacts, units], names=["impact", "unit"])

    Q = X.transpose()
    Q.index = ix_imp
    Q.columns = ix_int
    return Q


##### General helper functions


def make_H_matrix(focus, mapping, items_for, items_back):
    """Makes the concordance matrix H as pd.DataFrame.

    The binary matrix identifies which item of the foreground system
    does belong to the corresponding item of the background system.
    1, if concordance; else 0.
    Note, currently it is only possible to do a 1:1 concordance.
    Parameters
    ----------
    focus : str
        Focus of the concordance matrix.
        'ind' for industry
        'com' for commodity
        'reg' for region
        'int' for intervention
    mapping : dict
        Specifies the concordance between items.
        {'item1_for': 'item1_back', ...}
    items_for : list or pd.Index
        Items of the foreground system.
    items_back : list or pd.Index
        Items of the background system.

    Returns
    -------
    H : pd.DataFrame
        Concordance matrix.
    """
    if focus == "reg":
        H = pd.DataFrame(data=0.0, index=items_back, columns=items_for)
        H.index.names = ["region"]
        H.columns.names = ["region"]
        for i_for, i_back in mapping.items():
            H.at[i_back, i_for] = 1.0
    elif focus == "ind":
        H = pd.DataFrame(data=0.0, index=items_back, columns=items_for)
        H.index.names = ["industry"]
        H.columns.names = ["industry"]
        for i_for, i_back in mapping.items():
            H.at[i_back, i_for] = 1.0
    elif focus == "com":
        H = pd.DataFrame(data=0.0, index=items_for, columns=items_back)
        H.index.names = ["commodity"]
        H.columns.names = ["commodity"]
        for i_for, i_back in mapping.items():
            H.at[i_for, i_back] = 1.0
    elif focus == "int":
        H = pd.DataFrame(data=0.0, index=items_back, columns=items_for)
        H.index.names = ["intervention"]
        H.columns.names = ["intervention"]
        for i_for, i_back in mapping.items():
            H.at[i_back, i_for] = 1.0
    else:
        print(f"Focus {focus} is not supported.")
    return H


# for price vector from messsage
def p_messageix(df, year, multiindex=None, unit=None):
    """Determines the price vector p from message result.

    TODO: This function is not used currently. Maybe later.

    Parameters
    ----------
    df: pd.DataFrame
        PRICE_COMMODITY variable of messageix result
    year: int
    multiindex: pd.MultiIndex
        Specifies the index to merge on (to drop not needed commodities)
    unit: str
        Unit of the prices
        e.g.: "USD/kWa"

    Returns
    -------
    p: pd.DataFrame
        Price vector for message commodities
    """
    p = pd.DataFrame({})
    df = df[df["year"] == year]
    p["region"] = df["node"].str.replace("R11_", "")
    p["commodity"] = df[["level", "commodity"]].apply(lambda x: "|".join(x), axis=1)
    p["value"] = df["lvl"]
    if unit is not None:
        p["unit"] = unit
        p.set_index(["region", "commodity", "unit"], inplace=True)
    else:
        p.set_index(["region", "commodity"], inplace=True)
    if multiindex is not None:
        p1 = pd.DataFrame(data={}, index=multiindex)
        p = p1.merge(p, left_index=True, right_index=True, how="left")
        # Use prices of secondary/final commodities for import/export commodities.
        # this is necessary, since no prices for import/export is given by PRICE_COMMODITY
        for reg, com, uni in p.index:
            if "export" in com:
                try:
                    p.loc[(reg, com, uni), "value"] = p.at[
                        (reg, com.replace("export", "final"), uni), "value"
                    ]
                except KeyError:
                    try:
                        p.loc[(reg, com, uni), "value"] = p.at[
                            (reg, com.replace("export", "primary"), uni), "value"
                        ]
                    except KeyError:  # check why this part seems to have no effect!
                        try:
                            p.loc[(reg, com, uni), "value"] = p.at[
                                (reg, com.replace("export", "primary"), uni), "value"
                            ]
                        except KeyError:
                            pass

            elif "import" in com:
                try:
                    p.loc[(reg, com, uni), "value"] = p.at[
                        (reg, com.replace("import", "secondary"), uni), "value"
                    ]
                except KeyError:
                    try:
                        p.loc[(reg, com, uni), "value"] = p.at[
                            (reg, com.replace("import", "primary"), uni), "value"
                        ]
                    except KeyError:
                        pass

            elif "piped-gas" in com:
                try:
                    p.loc[(reg, com, uni), "value"] = p.at[
                        (reg, com.replace(com, "primary|gas"), uni), "value"
                    ]
                except KeyError:
                    try:
                        p.loc[(reg, com, uni), "value"] = p.at[
                            (reg, com.replace(com, "secondary|gas"), uni), "value"
                        ]
                    except KeyError:
                        pass
    # All other commodities are not specified for a region by PRICE_COMMODITY,
    # and can be set to 0
    p.fillna(0, inplace=True)
    return p


def aggregate_reg_com_in_p(p, V, mapping_reg, mapping_com=None):
    """Aggregates the regions in the price vector without units.

    Parameters
    ----------
    p : pd.DataFrame
        Price vector without units.
    mapping_reg : dict
        Mapping of regions to aggregate.
        {"new_reg1": ["old_reg1", "old_reg2"], "new_reg2: ...}
    mapping_com : dict
        Mapping of commodities to aggregate.
        {"new_com1": ["old_com1", "old_com2"], "new_com2: ...}
    V : pd.DataFrame
        Make matrix of a certain system.
    Returns
    -------
    p_agg : pd.DataFrame
        Aggregated price vector

    """

    # Determine produced amount of commodities
    q = V.sum(axis=0)

    # Create regional aggregation matrix S_reg
    S_reg = pd.DataFrame(
        0.0,
        index=mapping_reg.keys(),
        columns=sorted(set(v for val in mapping_reg.values() for v in val)),
    )
    for k, v in mapping_reg.items():
        S_reg.at[k, v] = 1.0

    # Create total aggregation matrix S_C
    if mapping_com is not None:
        S_com = pd.DataFrame(
            0.0,
            index=mapping_com.keys(),
            columns=sorted(set(v for val in mapping_com.values() for v in val)),
        )
        for k, v in mapping_com.items():
            S_com.at[k, v] = 1.0 / len(v)  # creates average price
    else:
        com = p.index.unique(level=1)
        # unit = p.index.unique(level=2)
        S_com = pd.DataFrame(np.identity(len(com)), index=com, columns=com)

    C_c = pd.MultiIndex.from_product(
        [S_reg.index.tolist(), S_com.index.tolist()],  # , unit],
        names=["region", "commodity"],  # "unit"],
    )
    C_i = pd.MultiIndex.from_product(
        [S_reg.columns.tolist(), S_com.columns.tolist()],  # , unit],
        names=["region", "commodity"],  # "unit"],
    )

    S_C = pd.DataFrame(np.kron(S_reg, S_com), index=C_c, columns=C_i)

    # Consider production ratios when aggregating commodity prices
    q_agg = S_C.dot(q)
    q_agg_repeated = S_C.transpose().dot(q_agg)
    q_ratios = q.divide(q_agg_repeated)
    q_ratios = q_ratios.to_frame(name="value")
    q_ratios.fillna(0, inplace=True)

    p_agg = S_C.dot(p.multiply(q_ratios))

    return p_agg
