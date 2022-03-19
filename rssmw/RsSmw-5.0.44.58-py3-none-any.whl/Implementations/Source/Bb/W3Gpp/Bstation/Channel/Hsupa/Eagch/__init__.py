from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eagch:
	"""Eagch commands group definition. 6 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eagch", core, parent)

	@property
	def ifCoding(self):
		"""ifCoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ifCoding'):
			from .IfCoding import IfCoding
			self._ifCoding = IfCoding(self._core, self._cmd_group)
		return self._ifCoding

	@property
	def tti(self):
		"""tti commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tti'):
			from .Tti import Tti
			self._tti = Tti(self._core, self._cmd_group)
		return self._tti

	@property
	def ttiCount(self):
		"""ttiCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiCount'):
			from .TtiCount import TtiCount
			self._ttiCount = TtiCount(self._core, self._cmd_group)
		return self._ttiCount

	@property
	def ttiedch(self):
		"""ttiedch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiedch'):
			from .Ttiedch import Ttiedch
			self._ttiedch = Ttiedch(self._core, self._cmd_group)
		return self._ttiedch

	def clone(self) -> 'Eagch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eagch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
