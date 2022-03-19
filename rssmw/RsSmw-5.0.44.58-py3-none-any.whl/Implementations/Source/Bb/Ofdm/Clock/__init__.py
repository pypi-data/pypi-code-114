from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	@property
	def synchronization(self):
		"""synchronization commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_synchronization'):
			from .Synchronization import Synchronization
			self._synchronization = Synchronization(self._core, self._cmd_group)
		return self._synchronization

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EuTraClockMode:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MODE \n
		Snippet: value: enums.EuTraClockMode = driver.source.bb.ofdm.clock.get_mode() \n
		Sets the type of externally supplied clock. \n
			:return: clock_mode: SAMPle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraClockMode)

	def set_mode(self, clock_mode: enums.EuTraClockMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MODE \n
		Snippet: driver.source.bb.ofdm.clock.set_mode(clock_mode = enums.EuTraClockMode.CUSTom) \n
		Sets the type of externally supplied clock. \n
			:param clock_mode: SAMPle
		"""
		param = Conversions.enum_scalar_to_str(clock_mode, enums.EuTraClockMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.ofdm.clock.get_multiplier() \n
		No command help available \n
			:return: clock_samp_mult: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, clock_samp_mult: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.ofdm.clock.set_multiplier(clock_samp_mult = 1) \n
		No command help available \n
			:param clock_samp_mult: No help available
		"""
		param = Conversions.decimal_value_to_str(clock_samp_mult)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceC:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceC = driver.source.bb.ofdm.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:return: clock_source: INTernal| ELCLock| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceC)

	def set_source(self, clock_source: enums.ClockSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:SOURce \n
		Snippet: driver.source.bb.ofdm.clock.set_source(clock_source = enums.ClockSourceC.ELCLock) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:param clock_source: INTernal| ELCLock| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(clock_source, enums.ClockSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CLOCk:SOURce {param}')

	def clone(self) -> 'Clock':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Clock(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
