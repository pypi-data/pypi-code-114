from enum import Enum


class Entries(Enum):
    ActualAnalaogInput1 = 167772417
    ActualAnalaogInput2 = 167772673
    ActualAnalaogInput3 = 167772929
    ActualAnalaogInput4 = 167773185

    ActualBatteryVoltage = 33556226
    ActualBatteryCharge = 33556229
    ActualBatteryCurrent = 33556228
    ActualBatteryCurrentDir = 33556230
    ActualBatteryChargeCycles = 33556228
    ActualBatteryTemperature = 33556227

    ActualGridOutputPower = 67109120
    ActualGridFreq = 67110400
    ActualGridCosPhi = 67110656
    ActualGridLimitation = 67110144
    ActualGridVoltageL1 = 67109378
    ActualGridCurrentL1 = 67109377
    ActualGridPowerL1 = 67109379
    ActualGridVoltageL2 = 67109634
    ActualGridCurrentL2 = 67109633
    ActualGridPowerL2 = 67109635
    ActualGridVoltageL3 = 67109890
    ActualGridCurrentL3 = 67109889
    ActualGridPowerL3 = 67109891

    ActualHomeConsumptionSolar = 83886336
    ActualHomeConsumptionBat = 83886592
    ActualHomeConsumptionGrid = 83886848
    ActualHomeConsumptionL1 = 83887106
    ActualHomeConsumptionL2 = 83887362
    ActualHomeConsumptionL3 = 83887618

    ActualGeneratorDc1Voltage = 33555202
    ActualGeneratorDc1Current = 33555201
    ActualGeneratorDc1Power = 33555203
    ActualGeneratorDc2Voltage = 33555458
    ActualGeneratorDc2Current = 33555457
    ActualGeneratorDc2Power = 33555459
    ActualGeneratorDc3Voltage = 33555714
    ActualGeneratorDc3Current = 33555713
    ActualGeneratorDc3Power = 33555715

    ActualS0InPulseCnt = 184549632
    ActualS0InLoginterval = 150995968

    HomeDcPowerPV = 33556736
    HomeAcPower = 67109120
    HomeOwnConsumption = 83888128
    HomeBatStateOfCharge = 33556229
    HomeOperatingStatus = 16780032

    InverterName = 16777984
    InverterMake = 16780544

    VersionUI = 16779267
    VersionFW = 16779265
    VersionHW = 16779266
    VersionPAR = 16779268
    SerialNumber = 16777728
    ArticleNumber = 16777472
    CountrySettingsName = 16779522
    CountrySettingsVersion = 16779521

    StatisticsDayYield = 251658754
    StatisticsDayHomeConsumption = 251659010
    StatisticsDayOwnConsumption = 251659266
    StatisticsDayOwnConsRate = 251659278
    StatisticsDayAutonomyDegree = 251659279

    StatisticsYearYield = 251658753
    StatisticsYearOperatingTime = 251658496
    StatisticsYearHomeConsumption = 251659009
    StatisticsYearOwnConsumption = 251659265
    StatisticsYearOwnConsRate = 251659280
    StatisticsYearAutonomyDegree = 251659281
