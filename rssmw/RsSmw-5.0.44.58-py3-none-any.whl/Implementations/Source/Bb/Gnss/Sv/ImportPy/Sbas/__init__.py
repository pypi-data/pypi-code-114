from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sbas:
	"""Sbas commands group definition. 12 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sbas", core, parent)

	@property
	def egnos(self):
		"""egnos commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_egnos'):
			from .Egnos import Egnos
			self._egnos = Egnos(self._core, self._cmd_group)
		return self._egnos

	@property
	def waas(self):
		"""waas commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_waas'):
			from .Waas import Waas
			self._waas = Waas(self._core, self._cmd_group)
		return self._waas

	def clone(self) -> 'Sbas':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sbas(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
