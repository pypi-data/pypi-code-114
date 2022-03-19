from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlotState:
	"""SlotState commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: SlotNull, default value after init: SlotNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slotState", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_slotNull_get', 'repcap_slotNull_set', repcap.SlotNull.Nr0)

	def repcap_slotNull_set(self, slotNull: repcap.SlotNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SlotNull.Default
		Default value after init: SlotNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(slotNull)

	def repcap_slotNull_get(self) -> repcap.SlotNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:BCH:SLOTstate<CH0> \n
		Snippet: value: bool = driver.source.bb.tdscdma.down.cell.enh.bch.slotState.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Queries the state of the slots off cell 1 used to transmit the broadcast channels. Slot 0 is always on and all the other
		slots are always off. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SlotState')
			:return: slot_state: 1| ON| 0| OFF"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:BCH:SLOTstate{slotNull_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'SlotState':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SlotState(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
