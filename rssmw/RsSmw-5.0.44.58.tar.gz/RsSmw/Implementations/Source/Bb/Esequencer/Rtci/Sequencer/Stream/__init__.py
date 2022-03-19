from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stream:
	"""Stream commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stream", core, parent)

	@property
	def buffilled(self):
		"""buffilled commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_buffilled'):
			from .Buffilled import Buffilled
			self._buffilled = Buffilled(self._core, self._cmd_group)
		return self._buffilled

	@property
	def bufRemain(self):
		"""bufRemain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bufRemain'):
			from .BufRemain import BufRemain
			self._bufRemain = BufRemain(self._core, self._cmd_group)
		return self._bufRemain

	@property
	def drop(self):
		"""drop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_drop'):
			from .Drop import Drop
			self._drop = Drop(self._core, self._cmd_group)
		return self._drop

	@property
	def exec(self):
		"""exec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exec'):
			from .Exec import Exec
			self._exec = Exec(self._core, self._cmd_group)
		return self._exec

	@property
	def pdwDropping(self):
		"""pdwDropping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdwDropping'):
			from .PdwDropping import PdwDropping
			self._pdwDropping = PdwDropping(self._core, self._cmd_group)
		return self._pdwDropping

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import Restart
			self._restart = Restart(self._core, self._cmd_group)
		return self._restart

	@property
	def stime(self):
		"""stime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stime'):
			from .Stime import Stime
			self._stime = Stime(self._core, self._cmd_group)
		return self._stime

	@property
	def stReset(self):
		"""stReset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stReset'):
			from .StReset import StReset
			self._stReset = StReset(self._core, self._cmd_group)
		return self._stReset

	@property
	def wrdRead(self):
		"""wrdRead commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wrdRead'):
			from .WrdRead import WrdRead
			self._wrdRead = WrdRead(self._core, self._cmd_group)
		return self._wrdRead

	@property
	def wrdWrite(self):
		"""wrdWrite commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wrdWrite'):
			from .WrdWrite import WrdWrite
			self._wrdWrite = WrdWrite(self._core, self._cmd_group)
		return self._wrdWrite

	def clone(self) -> 'Stream':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stream(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
