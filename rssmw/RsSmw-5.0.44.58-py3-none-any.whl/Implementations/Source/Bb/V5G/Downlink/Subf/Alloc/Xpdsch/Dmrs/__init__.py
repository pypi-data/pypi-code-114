from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dmrs:
	"""Dmrs commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrs", core, parent)

	@property
	def nid(self):
		"""nid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nid'):
			from .Nid import Nid
			self._nid = Nid(self._core, self._cmd_group)
		return self._nid

	@property
	def niddmrs(self):
		"""niddmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_niddmrs'):
			from .Niddmrs import Niddmrs
			self._niddmrs = Niddmrs(self._core, self._cmd_group)
		return self._niddmrs

	def clone(self) -> 'Dmrs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dmrs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
