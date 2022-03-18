#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
def thermal_conductivity(temperature):

    """
    ========== DESCRIPTION ==========

    This function return the thermal conductivity of Copper-Beryllium

    ========== VALIDITY ==========

    <temperature> : [4.4 -> 298]

    ========== FROM ==========

    Internal report - contact valentin.sauvage@outlook.com 

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of the material
        [K]

    ========== OUTPUT ==========

    <thermal_conductivity>
        -- float --
        The thermal conductivity of Copper-Beryllium
        [W].[m]**(-1).[K]**(-1)

    ========== STATUS ==========

    Status : Checked

    """

    ################## CONDITIONS #############################################

    assert temperature <= 298 and temperature >= 4.4 ,'The function '\
        ' CuBe.thermal_conductivity is not defined for '\
            'T = '+str(temperature)+' K'

    ################## MODULES ################################################

    import numpy as np

    ################## INITIALISATION #########################################
    
    Coefficients = np.array([-0.8517934,2.22797618,-0.29595893,0.01743955])

    ################## FUNCTION ###############################################

    result = 0
    
    for i in range(len(Coefficients)):
        result = result + Coefficients[i]*np.log(temperature)**i
        
    return np.exp(result)