from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oload:
	"""Oload commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oload", core, parent)

	@property
	def hold(self):
		"""hold commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hold'):
			from .Hold import Hold
			self._hold = Hold(self._core, self._cmd_group)
		return self._hold

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BBIN:OLOad:STATe \n
		Snippet: value: bool = driver.source.bbin.oload.get_state() \n
		Queries the current overflow state. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:OLOad:STATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Oload':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Oload(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
