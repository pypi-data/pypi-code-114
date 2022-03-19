from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cs:
	"""Cs commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cs", core, parent)

	@property
	def ap(self):
		"""ap commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ap'):
			from .Ap import Ap
			self._ap = Ap(self._core, self._cmd_group)
		return self._ap

	@property
	def csiAp(self):
		"""csiAp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csiAp'):
			from .CsiAp import CsiAp
			self._csiAp = CsiAp(self._core, self._cmd_group)
		return self._csiAp

	@property
	def xssap(self):
		"""xssap commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_xssap'):
			from .Xssap import Xssap
			self._xssap = Xssap(self._core, self._cmd_group)
		return self._xssap

	def clone(self) -> 'Cs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
