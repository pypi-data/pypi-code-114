from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ClockModeUnits:
		"""SCPI: [SOURce<HW>]:BB:DAB:CLOCk:MODE \n
		Snippet: value: enums.ClockModeUnits = driver.source.bb.dab.clock.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ClockModeUnits)

	def set_mode(self, mode: enums.ClockModeUnits) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:CLOCk:MODE \n
		Snippet: driver.source.bb.dab.clock.set_mode(mode = enums.ClockModeUnits.MSAMple) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ClockModeUnits)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DAB:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.dab.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.dab.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.SourceInt:
		"""SCPI: [SOURce<HW>]:BB:DAB:CLOCk:SOURce \n
		Snippet: value: enums.SourceInt = driver.source.bb.dab.clock.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)

	def set_source(self, source: enums.SourceInt) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:CLOCk:SOURce \n
		Snippet: driver.source.bb.dab.clock.set_source(source = enums.SourceInt.EXTernal) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceInt)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:CLOCk:SOURce {param}')
