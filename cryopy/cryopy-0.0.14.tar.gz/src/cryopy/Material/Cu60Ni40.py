#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%%
def ThermalConductivity(Temperature):

    """
    ========== DESCRIPTION ==========

    This function return the thermal conductivity of Cu60Ni40
    
    ========== Validity ==========

    4K < Temperature < 1000K

    ========== FROM ==========
    
    C. Y. Ho, M. W. Ackerman, K. Y. Wu, S. G. Oh, et T. N. Havill, « Thermal conductivity of ten selected binary alloy systems », Journal of Physical and Chemical Reference Data, vol. 7, no 3, p. 959‑1178, juill. 1978, doi: 10.1063/1.555583.


    ========== INPUT ==========

    [Temperature]
        The temperature of the material in [K]

    ========== OUTPUT ==========

    [ThermalConductivity]
        The thermal conductivity in [W].[m]**(-1).[K]**(-1)

    ========== STATUS ==========

    Status : Checked

    """

    ################## MODULES ###############################################

    import numpy as np
    from numpy.polynomial.chebyshev import chebval


    ################## CONDITIONS ############################################

    if Temperature <= 4 and Temperature >= 1000:

        return chebval(Temperature,[-2.30898228e+00,  6.85983394e-01, -4.39606667e-03,  1.55003291e-05, -3.26232016e-08,  4.32251401e-11, -3.68136398e-14,  2.00747488e-17, -6.76447346e-21,  1.28140575e-24, -1.04288668e-28])

        ################## SINON NAN #########################################

    else:
        print('Warning: The thermal conductivity of Cu60Ni40 is not defined for T = '+str(Temperature)+' K')
        return np.nan

