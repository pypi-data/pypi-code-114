from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BfConfiguration:
	"""BfConfiguration commands group definition. 27 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bfConfiguration", core, parent)

	@property
	def binterval(self):
		"""binterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_binterval'):
			from .Binterval import Binterval
			self._binterval = Binterval(self._core, self._cmd_group)
		return self._binterval

	@property
	def capability(self):
		"""capability commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_capability'):
			from .Capability import Capability
			self._capability = Capability(self._core, self._cmd_group)
		return self._capability

	@property
	def dcChannel(self):
		"""dcChannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcChannel'):
			from .DcChannel import DcChannel
			self._dcChannel = DcChannel(self._core, self._cmd_group)
		return self._dcChannel

	@property
	def erp(self):
		"""erp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_erp'):
			from .Erp import Erp
			self._erp = Erp(self._core, self._cmd_group)
		return self._erp

	@property
	def htCapability(self):
		"""htCapability commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_htCapability'):
			from .HtCapability import HtCapability
			self._htCapability = HtCapability(self._core, self._cmd_group)
		return self._htCapability

	@property
	def iaWindow(self):
		"""iaWindow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iaWindow'):
			from .IaWindow import IaWindow
			self._iaWindow = IaWindow(self._core, self._cmd_group)
		return self._iaWindow

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def ssid(self):
		"""ssid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssid'):
			from .Ssid import Ssid
			self._ssid = Ssid(self._core, self._cmd_group)
		return self._ssid

	@property
	def tstamp(self):
		"""tstamp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import Tstamp
			self._tstamp = Tstamp(self._core, self._cmd_group)
		return self._tstamp

	def clone(self) -> 'BfConfiguration':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BfConfiguration(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
