from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bstation:
	"""Bstation commands group definition. 57 total commands, 9 Subgroups, 1 group commands
	Repeated Capability: BaseStation, default value after init: BaseStation.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bstation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_baseStation_get', 'repcap_baseStation_set', repcap.BaseStation.Nr1)

	def repcap_baseStation_set(self, baseStation: repcap.BaseStation) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BaseStation.Default
		Default value after init: BaseStation.Nr1"""
		self._cmd_group.set_repcap_enum_value(baseStation)

	def repcap_baseStation_get(self) -> repcap.BaseStation:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def cgroup(self):
		"""cgroup commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cgroup'):
			from .Cgroup import Cgroup
			self._cgroup = Cgroup(self._core, self._cmd_group)
		return self._cgroup

	@property
	def dconflict(self):
		"""dconflict commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dconflict'):
			from .Dconflict import Dconflict
			self._dconflict = Dconflict(self._core, self._cmd_group)
		return self._dconflict

	@property
	def pdChannel(self):
		"""pdChannel commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdChannel'):
			from .PdChannel import PdChannel
			self._pdChannel = PdChannel(self._core, self._cmd_group)
		return self._pdChannel

	@property
	def pnOffset(self):
		"""pnOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnOffset'):
			from .PnOffset import PnOffset
			self._pnOffset = PnOffset(self._core, self._cmd_group)
		return self._pnOffset

	@property
	def qwSet(self):
		"""qwSet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qwSet'):
			from .QwSet import QwSet
			self._qwSet = QwSet(self._core, self._cmd_group)
		return self._qwSet

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def sync(self):
		"""sync commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def tdelay(self):
		"""tdelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdelay'):
			from .Tdelay import Tdelay
			self._tdelay = Tdelay(self._core, self._cmd_group)
		return self._tdelay

	@property
	def tdiversity(self):
		"""tdiversity commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdiversity'):
			from .Tdiversity import Tdiversity
			self._tdiversity = Tdiversity(self._core, self._cmd_group)
		return self._tdiversity

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:PRESet \n
		Snippet: driver.source.bb.c2K.bstation.preset() \n
		A standardized default for all the base stations (*RST values specified for the commands) . See 'Reset All Base Stations'
		for an overview. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:PRESet \n
		Snippet: driver.source.bb.c2K.bstation.preset_with_opc() \n
		A standardized default for all the base stations (*RST values specified for the commands) . See 'Reset All Base Stations'
		for an overview. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:C2K:BSTation:PRESet', opc_timeout_ms)

	def clone(self) -> 'Bstation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bstation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
