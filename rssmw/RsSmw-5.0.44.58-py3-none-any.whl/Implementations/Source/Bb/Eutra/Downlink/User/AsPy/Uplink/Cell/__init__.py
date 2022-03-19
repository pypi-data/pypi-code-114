from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 15 total commands, 6 Subgroups, 2 group commands
	Repeated Capability: CellNull, default value after init: CellNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cellNull_get', 'repcap_cellNull_set', repcap.CellNull.Nr0)

	def repcap_cellNull_set(self, cellNull: repcap.CellNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CellNull.Default
		Default value after init: CellNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(cellNull)

	def repcap_cellNull_get(self) -> repcap.CellNull:
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
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import Insert
			self._insert = Insert(self._core, self._cmd_group)
		return self._insert

	@property
	def selement(self):
		"""selement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_selement'):
			from .Selement import Selement
			self._selement = Selement(self._core, self._cmd_group)
		return self._selement

	@property
	def seqElem(self):
		"""seqElem commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_seqElem'):
			from .SeqElem import SeqElem
			self._seqElem = SeqElem(self._core, self._cmd_group)
		return self._seqElem

	@property
	def slength(self):
		"""slength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import Slength
			self._slength = Slength(self._core, self._cmd_group)
		return self._slength

	@property
	def vulTxPow(self):
		"""vulTxPow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vulTxPow'):
			from .VulTxPow import VulTxPow
			self._vulTxPow = VulTxPow(self._core, self._cmd_group)
		return self._vulTxPow

	def delete(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:UL:CELL<ST0>:DELete \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.uplink.cell.delete(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Deletes the selected table element. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:UL:CELL{cellNull_cmd_val}:DELete')

	def delete_with_opc(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, opc_timeout_ms: int = -1) -> None:
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:UL:CELL<ST0>:DELete \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.uplink.cell.delete_with_opc(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Deletes the selected table element. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:UL:CELL{cellNull_cmd_val}:DELete', opc_timeout_ms)

	def reset(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:UL:CELL<ST0>:RESet \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.uplink.cell.reset(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Resets the DCI table, i.e. removes all table elements. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:UL:CELL{cellNull_cmd_val}:RESet')

	def reset_with_opc(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, opc_timeout_ms: int = -1) -> None:
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:UL:CELL<ST0>:RESet \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.uplink.cell.reset_with_opc(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Resets the DCI table, i.e. removes all table elements. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:UL:CELL{cellNull_cmd_val}:RESet', opc_timeout_ms)

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
