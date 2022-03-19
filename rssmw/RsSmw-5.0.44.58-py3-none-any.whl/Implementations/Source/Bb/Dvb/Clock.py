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
	def get_mode(self) -> enums.DvbClocMode:
		"""SCPI: [SOURce<HW>]:BB:DVB:CLOCk:MODE \n
		Snippet: value: enums.DvbClocMode = driver.source.bb.dvb.clock.get_mode() \n
		Sets the type of externally supplied clock. \n
			:return: mode: SAMP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DvbClocMode)

	def set_mode(self, mode: enums.DvbClocMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:CLOCk:MODE \n
		Snippet: driver.source.bb.dvb.clock.set_mode(mode = enums.DvbClocMode.MSAMp) \n
		Sets the type of externally supplied clock. \n
			:param mode: SAMP
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DvbClocMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.dvb.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.dvb.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceC:
		"""SCPI: [SOURce<HW>]:BB:DVB:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceC = driver.source.bb.dvb.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:return: source: INTernal| ELCLock| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceC)

	def set_source(self, source: enums.ClockSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:CLOCk:SOURce \n
		Snippet: driver.source.bb.dvb.clock.set_source(source = enums.ClockSourceC.ELCLock) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:param source: INTernal| ELCLock| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:CLOCk:SOURce {param}')
