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

	def get_custom(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:CUSTom \n
		Snippet: value: int = driver.source.bb.v5G.clock.get_custom() \n
		No command help available \n
			:return: custom: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:CLOCk:CUSTom?')
		return Conversions.str_to_int(response)

	def set_custom(self, custom: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:CUSTom \n
		Snippet: driver.source.bb.v5G.clock.set_custom(custom = 1) \n
		No command help available \n
			:param custom: No help available
		"""
		param = Conversions.decimal_value_to_str(custom)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:CLOCk:CUSTom {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ClockMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:MODE \n
		Snippet: value: enums.ClockMode = driver.source.bb.v5G.clock.get_mode() \n
		Sets the type of externally supplied clock. \n
			:return: cloc_mode: SAMPle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ClockMode)

	def set_mode(self, cloc_mode: enums.ClockMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:MODE \n
		Snippet: driver.source.bb.v5G.clock.set_mode(cloc_mode = enums.ClockMode.SAMPle) \n
		Sets the type of externally supplied clock. \n
			:param cloc_mode: SAMPle
		"""
		param = Conversions.enum_scalar_to_str(cloc_mode, enums.ClockMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.v5G.clock.get_multiplier() \n
		No command help available \n
			:return: cloc_samp_mult: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, cloc_samp_mult: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.v5G.clock.set_multiplier(cloc_samp_mult = 1) \n
		No command help available \n
			:param cloc_samp_mult: No help available
		"""
		param = Conversions.decimal_value_to_str(cloc_samp_mult)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceC:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceC = driver.source.bb.v5G.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:return: cloc_source: INTernal| ELCLock| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceC)

	def set_source(self, cloc_source: enums.ClockSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:CLOCk:SOURce \n
		Snippet: driver.source.bb.v5G.clock.set_source(cloc_source = enums.ClockSourceC.ELCLock) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:param cloc_source: INTernal| ELCLock| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(cloc_source, enums.ClockSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:CLOCk:SOURce {param}')
