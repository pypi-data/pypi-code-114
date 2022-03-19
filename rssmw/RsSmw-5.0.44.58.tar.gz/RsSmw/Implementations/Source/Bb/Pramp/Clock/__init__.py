from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	@property
	def synchronization(self):
		"""synchronization commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronization'):
			from .Synchronization import Synchronization
			self._synchronization = Synchronization(self._core, self._cmd_group)
		return self._synchronization

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PowerRampClocMode:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:CLOCk:MODE \n
		Snippet: value: enums.PowerRampClocMode = driver.source.bb.pramp.clock.get_mode() \n
		Sets the type of externally supplied clock. \n
			:return: mode: SAMPle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowerRampClocMode)

	def set_mode(self, mode: enums.PowerRampClocMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:CLOCk:MODE \n
		Snippet: driver.source.bb.pramp.clock.set_mode(mode = enums.PowerRampClocMode.MULTisample) \n
		Sets the type of externally supplied clock. \n
			:param mode: SAMPle
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PowerRampClocMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.pramp.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.pramp.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceC:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceC = driver.source.bb.pramp.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:return: source: INTernal| ELCLock| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceC)

	def set_source(self, source: enums.ClockSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:CLOCk:SOURce \n
		Snippet: driver.source.bb.pramp.clock.set_source(source = enums.ClockSourceC.ELCLock) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:param source: INTernal| ELCLock| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:CLOCk:SOURce {param}')

	def clone(self) -> 'Clock':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Clock(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
