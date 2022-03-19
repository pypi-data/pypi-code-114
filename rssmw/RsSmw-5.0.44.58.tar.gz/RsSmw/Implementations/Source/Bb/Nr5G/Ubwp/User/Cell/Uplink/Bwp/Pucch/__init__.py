from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pucch:
	"""Pucch commands group definition. 10 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	@property
	def adMrs(self):
		"""adMrs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adMrs'):
			from .AdMrs import AdMrs
			self._adMrs = AdMrs(self._core, self._cmd_group)
		return self._adMrs

	@property
	def bpsk(self):
		"""bpsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bpsk'):
			from .Bpsk import Bpsk
			self._bpsk = Bpsk(self._core, self._cmd_group)
		return self._bpsk

	@property
	def brind(self):
		"""brind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_brind'):
			from .Brind import Brind
			self._brind = Brind(self._core, self._cmd_group)
		return self._brind

	@property
	def cpext(self):
		"""cpext commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpext'):
			from .Cpext import Cpext
			self._cpext = Cpext(self._core, self._cmd_group)
		return self._cpext

	@property
	def hack(self):
		"""hack commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hack'):
			from .Hack import Hack
			self._hack = Hack(self._core, self._cmd_group)
		return self._hack

	@property
	def pdsharq(self):
		"""pdsharq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsharq'):
			from .Pdsharq import Pdsharq
			self._pdsharq = Pdsharq(self._core, self._cmd_group)
		return self._pdsharq

	@property
	def uitl(self):
		"""uitl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uitl'):
			from .Uitl import Uitl
			self._uitl = Uitl(self._core, self._cmd_group)
		return self._uitl

	@property
	def ur16(self):
		"""ur16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ur16'):
			from .Ur16 import Ur16
			self._ur16 = Ur16(self._core, self._cmd_group)
		return self._ur16

	def clone(self) -> 'Pucch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pucch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
