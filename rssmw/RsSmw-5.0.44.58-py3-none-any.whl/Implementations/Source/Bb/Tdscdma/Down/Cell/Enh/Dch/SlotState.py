from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlotState:
	"""SlotState commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Slot, default value after init: Slot.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slotState", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_slot_get', 'repcap_slot_set', repcap.Slot.Nr1)

	def repcap_slot_set(self, slot: repcap.Slot) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Slot.Default
		Default value after init: Slot.Nr1"""
		self._cmd_group.set_repcap_enum_value(slot)

	def repcap_slot_get(self) -> repcap.Slot:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, slot_state: bool, cell=repcap.Cell.Default, slot=repcap.Slot.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:SLOTstate<CH> \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.slotState.set(slot_state = False, cell = repcap.Cell.Default, slot = repcap.Slot.Default) \n
		Queries the state of the slots off cell 1 used to transmit the transport channel. \n
			:param slot_state: 1| ON| 0| OFF
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SlotState')
		"""
		param = Conversions.bool_to_str(slot_state)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:SLOTstate{slot_cmd_val} {param}')

	def get(self, cell=repcap.Cell.Default, slot=repcap.Slot.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:SLOTstate<CH> \n
		Snippet: value: bool = driver.source.bb.tdscdma.down.cell.enh.dch.slotState.get(cell = repcap.Cell.Default, slot = repcap.Slot.Default) \n
		Queries the state of the slots off cell 1 used to transmit the transport channel. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SlotState')
			:return: slot_state: 1| ON| 0| OFF"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:SLOTstate{slot_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'SlotState':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SlotState(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
