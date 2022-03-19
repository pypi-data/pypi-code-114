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
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:CUSTom \n
		Snippet: value: int = driver.source.bb.eutra.clock.get_custom() \n
		Specifies the sample clock for clock type Custom (BB:EUTRa:CLOCk:MODE CUSTom) in the case of an external clock source.
		Note: Custom External Clock source in baseband B is only supported if baseband A is configured with EUTRA/LTE too.
		Furthermore the same settings for clock source and clock mode have to be set in baseband A and B. The user needs to take
		care of the correct settings. \n
			:return: custom: integer Range: 25000 to 40E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:CUSTom?')
		return Conversions.str_to_int(response)

	def set_custom(self, custom: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:CUSTom \n
		Snippet: driver.source.bb.eutra.clock.set_custom(custom = 1) \n
		Specifies the sample clock for clock type Custom (BB:EUTRa:CLOCk:MODE CUSTom) in the case of an external clock source.
		Note: Custom External Clock source in baseband B is only supported if baseband A is configured with EUTRA/LTE too.
		Furthermore the same settings for clock source and clock mode have to be set in baseband A and B. The user needs to take
		care of the correct settings. \n
			:param custom: integer Range: 25000 to 40E6
		"""
		param = Conversions.decimal_value_to_str(custom)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:CUSTom {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ClockMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MODE \n
		Snippet: value: enums.ClockMode = driver.source.bb.eutra.clock.get_mode() \n
		Sets the type of externally supplied clock. \n
			:return: mode: SAMPle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ClockMode)

	def set_mode(self, mode: enums.ClockMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MODE \n
		Snippet: driver.source.bb.eutra.clock.set_mode(mode = enums.ClockMode.SAMPle) \n
		Sets the type of externally supplied clock. \n
			:param mode: SAMPle
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ClockMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.eutra.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.eutra.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceC:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceC = driver.source.bb.eutra.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:return: source: INTernal| ELCLock| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceC)

	def set_source(self, source: enums.ClockSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:SOURce \n
		Snippet: driver.source.bb.eutra.clock.set_source(source = enums.ClockSourceC.ELCLock) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:param source: INTernal| ELCLock| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:SOURce {param}')
