from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alignment:
	"""Alignment commands group definition. 5 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alignment", core, parent)

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:[STATe] \n
		Snippet: value: bool = driver.source.efrontend.alignment.get_state() \n
		Activates correction of the IF signal for different IF signal frequencies. \n
			:return: cable_corr_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:ALIGnment:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, cable_corr_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:[STATe] \n
		Snippet: driver.source.efrontend.alignment.set_state(cable_corr_state = False) \n
		Activates correction of the IF signal for different IF signal frequencies. \n
			:param cable_corr_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(cable_corr_state)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:ALIGnment:STATe {param}')

	def clone(self) -> 'Alignment':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alignment(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
