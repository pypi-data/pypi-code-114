from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plp:
	"""Plp commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plp", core, parent)

	@property
	def nidPlp(self):
		"""nidPlp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nidPlp'):
			from .NidPlp import NidPlp
			self._nidPlp = NidPlp(self._core, self._cmd_group)
		return self._nidPlp

	@property
	def nplp(self):
		"""nplp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nplp'):
			from .Nplp import Nplp
			self._nplp = Nplp(self._core, self._cmd_group)
		return self._nplp

	def clone(self) -> 'Plp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Plp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
