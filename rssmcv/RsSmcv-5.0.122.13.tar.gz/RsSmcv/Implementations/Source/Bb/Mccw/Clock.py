from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ClockModeUnits:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CLOCk:MODE \n
		Snippet: value: enums.ClockModeUnits = driver.source.bb.mccw.clock.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ClockModeUnits)

	def set_mode(self, mode: enums.ClockModeUnits) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CLOCk:MODE \n
		Snippet: driver.source.bb.mccw.clock.set_mode(mode = enums.ClockModeUnits.MSAMple) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ClockModeUnits)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.mccw.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.mccw.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceB:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceB = driver.source.bb.mccw.clock.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceB)

	def set_source(self, source: enums.ClockSourceB) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CLOCk:SOURce \n
		Snippet: driver.source.bb.mccw.clock.set_source(source = enums.ClockSourceB.AINTernal) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceB)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CLOCk:SOURce {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CLOCk \n
		Snippet: value: float = driver.source.bb.mccw.clock.get_value() \n
		No command help available \n
			:return: clock: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CLOCk?')
		return Conversions.str_to_float(response)
