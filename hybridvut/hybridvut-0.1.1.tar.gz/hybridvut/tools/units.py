from iam_units import registry

import pandas as pd
import numpy as np

# use short names in registry
registry.Unit.default_format = "~P"


def convert_unit(vut, current, to, matrix, factor=None):
    """This function converts the current unit to another.

    The core of this function is strongly related to the convert_unit()
    function of the pyam package ;-)
    """

    if matrix == "V":
        df = vut.V.copy()
    if matrix == "U":
        df = vut.U.copy()
    if matrix == "F":
        df = vut.F.copy()
    if matrix == "Q":
        df = vut.Q.copy()
    if matrix == "F_Y":
        df = vut.F_Y.copy()

    # transpose if necessary
    if matrix in ["V", "Q"]:
        df1 = df.transpose()
    else:
        df1 = df.copy()

    # find, convert and replace values
    where = df1.index.get_loc_level(current, "unit")[0]

    if factor:
        df1.loc[where] *= factor
    else:
        # Values of Q are impact/intervention (hence, pint units need workaround)
        if matrix in ["Q"]:
            qty = [df1.loc[where].values, "1/" + current]
            res = registry.Quantity(*qty).to("1/" + to)
        else:
            qty = [df1.loc[where].values, current]
            res = registry.Quantity(*qty).to(to)
        df1.loc[where] = res.magnitude

    # replace the old unit index by new unit
    if matrix in ["F", "Q", "F_Y"]:
        df1.index = df1.index.set_levels(
            df1.index.levels[1].str.replace(rf"^{current}$", to),
            level="unit",
            verify_integrity=False,
        )
    else:
        df1.index = df1.index.set_levels(
            df1.index.levels[2].str.replace(rf"^{current}$", to), level="unit"
        )

    # transpose if necessary
    if matrix in ["V", "Q"]:
        df1 = df1.transpose()

    # set .self
    if matrix == "V":
        vut.V = df1
    if matrix == "U":
        vut.U = df1
    if matrix == "F":
        vut.F = df1
    if matrix == "Q":
        vut.Q = df1
    if matrix == "F_Y":
        vut.F_Y = df1

    return df1


def demonetize_F_mult(F_mult, price_vector):
    """This function converts F_mult from monetary to physical units.

    Currently only for F_mult_com (extensions per commodity).
    Currently only for F_mult with same monetary units.
    Currently only if price_vector has same monetary unit as in F_mult.

    Parameters
    ----------
    F_mult : pd.DataFrame
        Multiplier matrix with extensions per (monetary) unit of commodities
        df must have index.names = ["intervention", "unit"]
        df must have columns.names = ["region", "commodity", "unit"]
    price_vector : pd.DataFrame
        Price vector with price per physical unit of commodities
        df must have index.names = ["region", "commodity", "unit"]
    Returns
    -------
    F_mult_phys : pd.DataFrame
        Multiplier matrix with extensions per (physical) unit of commodities
    """

    reg = F_mult.columns.get_level_values(0)
    com = F_mult.columns.get_level_values(1)
    ix = F_mult.index.copy()

    Q_ = registry.Quantity

    # change the numerator with the dominator
    # (necessary since the units for the values in F_mult are row_unit/column_unit)
    old_unit = price_vector.index.levels[2][0]
    new_unit = old_unit.split("/")[1] + "/" + old_unit.split("/")[0]

    # create pint arrays for dealing with units during calculation
    F_mult_pint = Q_(F_mult.values, F_mult.columns.levels[2][0])
    p_pint = Q_(price_vector.values, new_unit)

    ones = np.ones((F_mult.shape[0], 1))

    # calclation of physical values
    F_mult_pint_phys = np.multiply(F_mult_pint, np.dot(ones, np.transpose(p_pint)))

    # creare new column index
    new_units = []
    for i in range(len(reg)):
        new_units.append(str(F_mult_pint_phys.units))
    co = pd.MultiIndex.from_arrays(
        [reg, com, new_units], names=["region", "commodity", "unit"]
    )

    # create new dataframe
    F_mult_phys = pd.DataFrame(F_mult_pint_phys.magnitude, index=ix, columns=co)

    return F_mult_phys
