from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mstation:
	"""Mstation commands group definition. 27 total commands, 8 Subgroups, 1 group commands
	Repeated Capability: MobileStation, default value after init: MobileStation.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mstation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_mobileStation_get', 'repcap_mobileStation_set', repcap.MobileStation.Nr1)

	def repcap_mobileStation_set(self, mobileStation: repcap.MobileStation) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MobileStation.Default
		Default value after init: MobileStation.Nr1"""
		self._cmd_group.set_repcap_enum_value(mobileStation)

	def repcap_mobileStation_get(self) -> repcap.MobileStation:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def additional(self):
		"""additional commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_additional'):
			from .Additional import Additional
			self._additional = Additional(self._core, self._cmd_group)
		return self._additional

	@property
	def ccoding(self):
		"""ccoding commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def channel(self):
		"""channel commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def lcMask(self):
		"""lcMask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lcMask'):
			from .LcMask import LcMask
			self._lcMask = LcMask(self._core, self._cmd_group)
		return self._lcMask

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def rconfiguration(self):
		"""rconfiguration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rconfiguration'):
			from .Rconfiguration import Rconfiguration
			self._rconfiguration = Rconfiguration(self._core, self._cmd_group)
		return self._rconfiguration

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tpc(self):
		"""tpc commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import Tpc
			self._tpc = Tpc(self._core, self._cmd_group)
		return self._tpc

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation:PRESet \n
		Snippet: driver.source.bb.c2K.mstation.preset() \n
		A standardized default for all the mobile stations (*RST values specified for the commands) . See 'Reset All Mobile
		Stations' for an overview. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation:PRESet \n
		Snippet: driver.source.bb.c2K.mstation.preset_with_opc() \n
		A standardized default for all the mobile stations (*RST values specified for the commands) . See 'Reset All Mobile
		Stations' for an overview. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:C2K:MSTation:PRESet', opc_timeout_ms)

	def clone(self) -> 'Mstation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mstation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
