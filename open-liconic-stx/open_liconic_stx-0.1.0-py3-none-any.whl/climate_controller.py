from stx.memory_map import MemoryMap


class ClimateController:
    __memory_map: MemoryMap

    def __init__(self, memory_map: MemoryMap) -> None:
        self.__memory_map = memory_map

    @property
    def current_temperature(self) -> float:
        """The current temperature in °C"""
        return self.__memory_map.data[982] / 10

    @property
    def target_temperature(self) -> float:
        """The target temperature in °C (can be set)"""
        return self.__memory_map.data[890] / 10

    @target_temperature.setter
    def target_temperature(self, target_temperature: float) -> None:
        self.__memory_map.data[890] = int(target_temperature * 10)

    @property
    def current_humidity(self) -> float:
        """The current humidity in % RH"""
        return self.__memory_map.data[983] / 10

    @property
    def target_humidity(self) -> float:
        """The target humidity in % RH (can be set)"""
        return self.__memory_map.data[893] / 10

    @target_humidity.setter
    def target_humidity(self, target_humidity: float) -> None:
        self.__memory_map.data[893] = int(target_humidity * 10)

    @property
    def current_co2(self) -> float:
        """The current CO2 level in % vol."""
        return self.__memory_map.data[984] / 100

    @property
    def target_co2(self) -> float:
        """The current CO2 level in % vol. (can be set)"""
        return self.__memory_map.data[894] / 100

    @target_co2.setter
    def target_co2(self, target_co2: float) -> None:
        self.__memory_map.data[894] = int(target_co2 * 100)

    @property
    def current_gas_1(self) -> float:
        """The current gas level of gas port 1 in % vol. (N2 or O2)"""
        return self.__memory_map.data[985] / 100

    @property
    def target_gas_1(self) -> float:
        """The target gas level of gas port 1 in % vol. (N2 or O2, can be set)"""
        return self.__memory_map.data[895] / 100

    @target_gas_1.setter
    def target_gas_1(self, target_n2: float) -> None:
        self.__memory_map.data[895] = int(target_n2 * 100)

    @property
    def current_gas_2(self) -> float:
        """The current gas level of gas port 2 in % vol. (N2 or O2)"""
        return self.__memory_map.data[986] / 100

    @property
    def target_gas_2(self) -> float:
        """The target gas level of gas port 2 in % vol. (N2 or O2, can be set)"""
        return self.__memory_map.data[896] / 100

    @target_gas_2.setter
    def target_gas_2(self, target_n2: float) -> None:
        self.__memory_map.data[896] = int(target_n2 * 100)

    def reset_water_low_alarm(self) -> None:
        """Reset the "water low" alarm"""
        self.__memory_map.bits[1505] = False

    def reset_co2_timeout_error(self) -> None:
        """Reset the CO2 timeout error"""
        self.__memory_map.bits[1504] = False
