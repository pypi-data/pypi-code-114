from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_loss(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:POWer:LOSS \n
		Snippet: value: float = driver.source.regenerator.radar.power.get_loss() \n
		Additional loss to compensate for system or cable loss. \n
			:return: power_loss: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:POWer:LOSS?')
		return Conversions.str_to_float(response)

	def set_loss(self, power_loss: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:POWer:LOSS \n
		Snippet: driver.source.regenerator.radar.power.set_loss(power_loss = 1.0) \n
		Additional loss to compensate for system or cable loss. \n
			:param power_loss: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(power_loss)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:POWer:LOSS {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.RegRadarPowSett:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:POWer:MODE \n
		Snippet: value: enums.RegRadarPowSett = driver.source.regenerator.radar.power.get_mode() \n
		Sets how the radar receive power is calculated. \n
			:return: mode: REQuation| MANual
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.RegRadarPowSett)

	def set_mode(self, mode: enums.RegRadarPowSett) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:POWer:MODE \n
		Snippet: driver.source.regenerator.radar.power.set_mode(mode = enums.RegRadarPowSett.MANual) \n
		Sets how the radar receive power is calculated. \n
			:param mode: REQuation| MANual
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RegRadarPowSett)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:POWer:MODE {param}')

	def get_tx(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:POWer:TX \n
		Snippet: value: float = driver.source.regenerator.radar.power.get_tx() \n
		Sets the radar transmit power PTx. \n
			:return: power: float Range: -50 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:POWer:TX?')
		return Conversions.str_to_float(response)

	def set_tx(self, power: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:POWer:TX \n
		Snippet: driver.source.regenerator.radar.power.set_tx(power = 1.0) \n
		Sets the radar transmit power PTx. \n
			:param power: float Range: -50 to 100
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:POWer:TX {param}')
