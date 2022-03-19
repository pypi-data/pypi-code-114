from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PulsTrigMode:
		"""SCPI: [SOURce<HW>]:PULM:TRIGger:MODE \n
		Snippet: value: enums.PulsTrigMode = driver.source.pulm.trigger.get_mode() \n
		Selects a trigger mode - auto, external, external single or external gated - for generating the modulation signal. \n
			:return: mode: AUTO| EXTernal| EGATe| ESINgle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:TRIGger:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PulsTrigMode)

	def set_mode(self, mode: enums.PulsTrigMode) -> None:
		"""SCPI: [SOURce<HW>]:PULM:TRIGger:MODE \n
		Snippet: driver.source.pulm.trigger.set_mode(mode = enums.PulsTrigMode.AUTO) \n
		Selects a trigger mode - auto, external, external single or external gated - for generating the modulation signal. \n
			:param mode: AUTO| EXTernal| EGATe| ESINgle
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PulsTrigMode)
		self._core.io.write(f'SOURce<HwInstance>:PULM:TRIGger:MODE {param}')

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
