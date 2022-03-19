from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mac:
	"""Mac commands group definition. 35 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mac", core, parent)

	@property
	def bssid(self):
		"""bssid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bssid'):
			from .Bssid import Bssid
			self._bssid = Bssid(self._core, self._cmd_group)
		return self._bssid

	@property
	def fcontrol(self):
		"""fcontrol commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcontrol'):
			from .Fcontrol import Fcontrol
			self._fcontrol = Fcontrol(self._core, self._cmd_group)
		return self._fcontrol

	@property
	def htControl(self):
		"""htControl commands group. 11 Sub-classes, 1 commands."""
		if not hasattr(self, '_htControl'):
			from .HtControl import HtControl
			self._htControl = HtControl(self._core, self._cmd_group)
		return self._htControl

	@property
	def sa(self):
		"""sa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sa'):
			from .Sa import Sa
			self._sa = Sa(self._core, self._cmd_group)
		return self._sa

	@property
	def vhtControl(self):
		"""vhtControl commands group. 12 Sub-classes, 1 commands."""
		if not hasattr(self, '_vhtControl'):
			from .VhtControl import VhtControl
			self._vhtControl = VhtControl(self._core, self._cmd_group)
		return self._vhtControl

	def clone(self) -> 'Mac':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mac(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
