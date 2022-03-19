from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Am:
	"""Am commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("am", core, parent)

	def get_depth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:DEPTh \n
		Snippet: value: float = driver.source.bb.general.am.get_depth() \n
		Sets the depth of the modulation signal in percent. The depth is limited by the maximum peak envelope power (PEP) . \n
			:return: am_depth: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:AM:DEPTh?')
		return Conversions.str_to_float(response)

	def set_depth(self, am_depth: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:DEPTh \n
		Snippet: driver.source.bb.general.am.set_depth(am_depth = 1.0) \n
		Sets the depth of the modulation signal in percent. The depth is limited by the maximum peak envelope power (PEP) . \n
			:param am_depth: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(am_depth)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:AM:DEPTh {param}')

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:FREQuency \n
		Snippet: value: float = driver.source.bb.general.am.get_frequency() \n
		Sets the frequency of the modulation signal. \n
			:return: am_freq: float Range: 0.1 to 100E3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:AM:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, am_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:FREQuency \n
		Snippet: driver.source.bb.general.am.set_frequency(am_freq = 1.0) \n
		Sets the frequency of the modulation signal. \n
			:param am_freq: float Range: 0.1 to 100E3
		"""
		param = Conversions.decimal_value_to_str(am_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:AM:FREQuency {param}')

	def get_period(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:PERiod \n
		Snippet: value: float = driver.source.bb.general.am.get_period() \n
		Queries the period of the modulation signal. \n
			:return: am_per: float Range: 100E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:AM:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, am_per: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:PERiod \n
		Snippet: driver.source.bb.general.am.set_period(am_per = 1.0) \n
		Queries the period of the modulation signal. \n
			:param am_per: float Range: 100E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(am_per)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:AM:PERiod {param}')

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.BasebandModShape:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:SHAPe \n
		Snippet: value: enums.BasebandModShape = driver.source.bb.general.am.get_shape() \n
		Queries the shape of the modulation signal. \n
			:return: am_shape: SINE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:AM:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.BasebandModShape)

	def set_shape(self, am_shape: enums.BasebandModShape) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:SHAPe \n
		Snippet: driver.source.bb.general.am.set_shape(am_shape = enums.BasebandModShape.SINE) \n
		Queries the shape of the modulation signal. \n
			:param am_shape: SINE
		"""
		param = Conversions.enum_scalar_to_str(am_shape, enums.BasebandModShape)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:AM:SHAPe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:[STATe] \n
		Snippet: value: bool = driver.source.bb.general.am.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: am_mod_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:AM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, am_mod_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:AM:[STATe] \n
		Snippet: driver.source.bb.general.am.set_state(am_mod_state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param am_mod_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(am_mod_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:AM:STATe {param}')
