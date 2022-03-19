from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Couple:
	"""Couple commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("couple", core, parent)

	@property
	def logNormal(self):
		"""logNormal commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_logNormal'):
			from .LogNormal import LogNormal
			self._logNormal = LogNormal(self._core, self._cmd_group)
		return self._logNormal

	def get_speed(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:COUPle:SPEed \n
		Snippet: value: bool = driver.source.fsimulator.couple.get_speed() \n
		(available in 'System Configuration > Mode > Standard') Couples the setting for the speed for the paths of both faders. \n
			:return: speed: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:COUPle:SPEed?')
		return Conversions.str_to_bool(response)

	def set_speed(self, speed: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:COUPle:SPEed \n
		Snippet: driver.source.fsimulator.couple.set_speed(speed = False) \n
		(available in 'System Configuration > Mode > Standard') Couples the setting for the speed for the paths of both faders. \n
			:param speed: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(speed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:COUPle:SPEed {param}')

	def clone(self) -> 'Couple':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Couple(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
