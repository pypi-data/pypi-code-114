# Copyright 2022 Cognite AS
import numpy as np
import pandas as pd

from indsl.resample.auto_align import auto_align
from indsl.type_check import check_types


@check_types
def total_head(
    discharge_pressure: pd.Series, suction_pressure: pd.Series, den: float, align_timesteps: bool = False
) -> pd.Series:
    """Total head calculation

    Head is a measure of the potential of a liquid to reach a certain
    height. The head is essentially a unit of pressure. The total head
    is the difference in pressure of the discharge to the suction of
    the pump.

    Args:
        discharge_pressure (pandas.Series): Discharge pressure [Pa]
            Discharge pressure of a centrifugal pump.
        suction_pressure (pandas.Series): Suction pressure [Pa]
            Suction pressure of a centrifugal pump.
        den (float): Density of fluid [kg/m3]
            Specific gravity of the fluid.
        align_timesteps (bool): Auto-align
            Automatically align time stamp  of input time series. Default is False.

    Returns:
        pandas.Series: Total head [m]
            Difference in total discharge head and the total suction head.

    """
    # auto-align
    discharge_pressure, suction_pressure = auto_align([discharge_pressure, suction_pressure], align_timesteps)

    return (discharge_pressure - suction_pressure) / (den * 9.81)


@check_types
def percent_BEP_flowrate(pump_liquid_flowrate: pd.Series, BEP_flowrate: float) -> pd.Series:
    """Current flowrate % of BEP

    Centrifugal pumps operate optimally at a specific liquid flowrate (BEP).
    This function calculates the flowrate relative to BEP as a percentage.
    i.e. 100% means the current flowrate is at the BEP, 110% means the
    current flowrate is 10% above BEP.

    Args:
        pump_liquid_flowrate (pandas.Series): Pump liquid flowrate
            The current flowrate of the pump.
        BEP_flowrate (float): Best efficiency point
            The best efficiency flowrate point of the pump.

    Returns:
        pandas.Series:BEP to current flowrate [%]
            Percentage of current flowrate to BEP

    """

    return pump_liquid_flowrate / BEP_flowrate * 100


@check_types
def pump_hydraulic_power(
    pump_liquid_flowrate: pd.Series, total_head: pd.Series, den: float, align_timesteps: bool = False
) -> pd.Series:
    """Pump hydraulic horsepower

    Pump hydraulic horsepower is the amount of energy per unit time
    delivered to the liquid. Pump hydraulic horsepower can be calculated
    if the liquid flowrate, total head across the pump, and specific gravity
    of the fluid.

    Args:

        pump_liquid_flowrate (pandas.Series): Pump liquid flowrate [m3/s]
            The current flowrate of the pump.
        total_head (pandas.Series): Head across pump [m]
            Difference in pressure between discharge and suction of pump.
        den (float): Density of fluid [kg/m3]
            Specific gravity of the fluid.
        align_timesteps (bool): Auto-align
            Automatically align time stamp  of input time series. Default is False.

    Returns:
        pandas.Series: Hydraulic horsepower [W]
            Hydraulic horsepower of pump.

    """
    # auto-align
    pump_liquid_flowrate, total_head = auto_align([pump_liquid_flowrate, total_head], align_timesteps)

    return pump_liquid_flowrate * den * 9.81 * total_head


@check_types
def pump_shaft_power(
    pump_hydraulic_power: pd.Series,
    pump_liquid_flowrate: pd.Series,
    eff_parameter_1: float,
    eff_parameter_2: float,
    eff_intercept: float,
    align_timesteps: bool = False,
) -> pd.Series:
    """Pump shaft power

    Pump shaft power is the input power delivered by the shaft.
    Pump shaft power can be calculated by dividing the pump hydraulic hp
    by the pump efficiency. Pump efficiency is a function of liquid flowrate.
    The pump efficiency curve is assumed to be a 2nd order polynomial.
    Therefore the input parameters of the curve are coefficients
    to x^2 and x and the y intercept of the curve.

    Args:

        pump_hydraulic_power (pandas.Series): Hydraulic power [W]
            Hydraulic power of pump.
        pump_liquid_flowrate (pandas.Series): Pump liquid flowrate [m3/h]
            The current flowrate of the pump.
        eff_parameter_1 (float): x^2 coefficient [-]
            Coefficient to x^2.
        eff_parameter_2 (float): x coefficient [-]
            Coefficient to x.
        eff_intercept (float): y-intercept [-]
            Y-intercept of curve
        align_timesteps (bool): Auto-align
            Automatically align time stamp  of input time series. Default is False.

    Returns:
        pandas.Series: pump shaft power [W]
            Pump shaft power of pump.
    """
    # auto-align
    pump_liquid_flowrate, pump_hydraulic_power = auto_align(
        [pump_liquid_flowrate, pump_hydraulic_power], align_timesteps
    )

    p = (eff_parameter_1, eff_parameter_2, eff_intercept)
    eff = np.polyval(p, pump_liquid_flowrate) / 100

    return pump_hydraulic_power / eff
