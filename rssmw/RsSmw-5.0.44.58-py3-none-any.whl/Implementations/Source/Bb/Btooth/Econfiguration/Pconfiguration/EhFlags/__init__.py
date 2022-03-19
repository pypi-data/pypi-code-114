from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EhFlags:
	"""EhFlags commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ehFlags", core, parent)

	@property
	def aaddress(self):
		"""aaddress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_aaddress'):
			from .Aaddress import Aaddress
			self._aaddress = Aaddress(self._core, self._cmd_group)
		return self._aaddress

	@property
	def adInfo(self):
		"""adInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adInfo'):
			from .AdInfo import AdInfo
			self._adInfo = AdInfo(self._core, self._cmd_group)
		return self._adInfo

	@property
	def aptr(self):
		"""aptr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aptr'):
			from .Aptr import Aptr
			self._aptr = Aptr(self._core, self._cmd_group)
		return self._aptr

	@property
	def cinfo(self):
		"""cinfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cinfo'):
			from .Cinfo import Cinfo
			self._cinfo = Cinfo(self._core, self._cmd_group)
		return self._cinfo

	@property
	def sinfo(self):
		"""sinfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sinfo'):
			from .Sinfo import Sinfo
			self._sinfo = Sinfo(self._core, self._cmd_group)
		return self._sinfo

	@property
	def taddress(self):
		"""taddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taddress'):
			from .Taddress import Taddress
			self._taddress = Taddress(self._core, self._cmd_group)
		return self._taddress

	@property
	def tpower(self):
		"""tpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpower'):
			from .Tpower import Tpower
			self._tpower = Tpower(self._core, self._cmd_group)
		return self._tpower

	def clone(self) -> 'EhFlags':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EhFlags(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
