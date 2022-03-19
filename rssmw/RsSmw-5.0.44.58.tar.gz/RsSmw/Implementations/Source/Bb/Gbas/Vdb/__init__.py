from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vdb:
	"""Vdb commands group definition. 134 total commands, 12 Subgroups, 1 group commands
	Repeated Capability: VdbTransmitter, default value after init: VdbTransmitter.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vdb", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_vdbTransmitter_get', 'repcap_vdbTransmitter_set', repcap.VdbTransmitter.Nr1)

	def repcap_vdbTransmitter_set(self, vdbTransmitter: repcap.VdbTransmitter) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to VdbTransmitter.Default
		Default value after init: VdbTransmitter.Nr1"""
		self._cmd_group.set_repcap_enum_value(vdbTransmitter)

	def repcap_vdbTransmitter_get(self) -> repcap.VdbTransmitter:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def append(self):
		"""append commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_append'):
			from .Append import Append
			self._append = Append(self._core, self._cmd_group)
		return self._append

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dlength(self):
		"""dlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlength'):
			from .Dlength import Dlength
			self._dlength = Dlength(self._core, self._cmd_group)
		return self._dlength

	@property
	def fnumber(self):
		"""fnumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fnumber'):
			from .Fnumber import Fnumber
			self._fnumber = Fnumber(self._core, self._cmd_group)
		return self._fnumber

	@property
	def gid(self):
		"""gid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gid'):
			from .Gid import Gid
			self._gid = Gid(self._core, self._cmd_group)
		return self._gid

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import Insert
			self._insert = Insert(self._core, self._cmd_group)
		return self._insert

	@property
	def mconfig(self):
		"""mconfig commands group. 54 Sub-classes, 0 commands."""
		if not hasattr(self, '_mconfig'):
			from .Mconfig import Mconfig
			self._mconfig = Mconfig(self._core, self._cmd_group)
		return self._mconfig

	@property
	def rid(self):
		"""rid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rid'):
			from .Rid import Rid
			self._rid = Rid(self._core, self._cmd_group)
		return self._rid

	@property
	def sch(self):
		"""sch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sch'):
			from .Sch import Sch
			self._sch = Sch(self._core, self._cmd_group)
		return self._sch

	@property
	def sgid(self):
		"""sgid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgid'):
			from .Sgid import Sgid
			self._sgid = Sgid(self._core, self._cmd_group)
		return self._sgid

	@property
	def ssid(self):
		"""ssid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssid'):
			from .Ssid import Ssid
			self._ssid = Ssid(self._core, self._cmd_group)
		return self._ssid

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def delete(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:DELete \n
		Snippet: driver.source.bb.gbas.vdb.delete(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Deletes the selected VDB. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:DELete')

	def delete_with_opc(self, vdbTransmitter=repcap.VdbTransmitter.Default, opc_timeout_ms: int = -1) -> None:
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:DELete \n
		Snippet: driver.source.bb.gbas.vdb.delete_with_opc(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Deletes the selected VDB. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'Vdb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Vdb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
