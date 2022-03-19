from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 12 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def avahi(self):
		"""avahi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_avahi'):
			from .Avahi import Avahi
			self._avahi = Avahi(self._core, self._cmd_group)
		return self._avahi

	@property
	def ftp(self):
		"""ftp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ftp'):
			from .Ftp import Ftp
			self._ftp = Ftp(self._core, self._cmd_group)
		return self._ftp

	@property
	def http(self):
		"""http commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_http'):
			from .Http import Http
			self._http = Http(self._core, self._cmd_group)
		return self._http

	@property
	def raw(self):
		"""raw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_raw'):
			from .Raw import Raw
			self._raw = Raw(self._core, self._cmd_group)
		return self._raw

	@property
	def remSupport(self):
		"""remSupport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remSupport'):
			from .RemSupport import RemSupport
			self._remSupport = RemSupport(self._core, self._cmd_group)
		return self._remSupport

	@property
	def rpc(self):
		"""rpc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rpc'):
			from .Rpc import Rpc
			self._rpc = Rpc(self._core, self._cmd_group)
		return self._rpc

	@property
	def smb(self):
		"""smb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_smb'):
			from .Smb import Smb
			self._smb = Smb(self._core, self._cmd_group)
		return self._smb

	@property
	def soe(self):
		"""soe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_soe'):
			from .Soe import Soe
			self._soe = Soe(self._core, self._cmd_group)
		return self._soe

	@property
	def ssh(self):
		"""ssh commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssh'):
			from .Ssh import Ssh
			self._ssh = Ssh(self._core, self._cmd_group)
		return self._ssh

	@property
	def swUpdate(self):
		"""swUpdate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_swUpdate'):
			from .SwUpdate import SwUpdate
			self._swUpdate = SwUpdate(self._core, self._cmd_group)
		return self._swUpdate

	@property
	def vnc(self):
		"""vnc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_vnc'):
			from .Vnc import Vnc
			self._vnc = Vnc(self._core, self._cmd_group)
		return self._vnc

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
