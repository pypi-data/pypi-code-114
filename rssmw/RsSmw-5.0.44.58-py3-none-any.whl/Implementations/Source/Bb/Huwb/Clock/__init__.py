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
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.HrpUwbClocMode:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CLOCk:MODE \n
		Snippet: value: enums.HrpUwbClocMode = driver.source.bb.huwb.clock.get_mode() \n
		Sets the type of externally supplied clock. \n
			:return: mode: SAMPle| MSAMple| CSAMple
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbClocMode)

	def set_mode(self, mode: enums.HrpUwbClocMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CLOCk:MODE \n
		Snippet: driver.source.bb.huwb.clock.set_mode(mode = enums.HrpUwbClocMode.CSAMple) \n
		Sets the type of externally supplied clock. \n
			:param mode: SAMPle| MSAMple| CSAMple
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HrpUwbClocMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.huwb.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.huwb.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceB:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceB = driver.source.bb.huwb.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:return: source: INTernal| ELCLock| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceB)

	def set_source(self, source: enums.ClockSourceB) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CLOCk:SOURce \n
		Snippet: driver.source.bb.huwb.clock.set_source(source = enums.ClockSourceB.AINTernal) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference
			- ELCLock: External local clock
			- EXTernal = ELCLock: Setting only Provided for backward compatibility with other Rohde & Schwarz signal generators \n
			:param source: INTernal| ELCLock| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceB)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:CLOCk:SOURce {param}')

	def clone(self) -> 'Clock':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Clock(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
