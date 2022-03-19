from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Am:
	"""Am commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("am", core, parent)

	@property
	def bband(self):
		"""bband commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bband'):
			from .Bband import Bband
			self._bband = Bband(self._core, self._cmd_group)
		return self._bband

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	def get_sensitivity(self) -> float:
		"""SCPI: [SOURce<HW>]:AM:SENSitivity \n
		Snippet: value: float = driver.source.am.get_sensitivity() \n
		No command help available \n
			:return: sensitivity: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AM:SENSitivity?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Am':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Am(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
