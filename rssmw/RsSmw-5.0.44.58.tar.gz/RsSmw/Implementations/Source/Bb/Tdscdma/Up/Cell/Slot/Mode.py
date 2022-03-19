from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.TdscdmaSlotModeUp, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:MODE \n
		Snippet: driver.source.bb.tdscdma.up.cell.slot.mode.set(mode = enums.TdscdmaSlotModeUp.DEDicated, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the mode in which the slot is to work. \n
			:param mode: DEDicated| PRACh DEDicated The instrument generates a signal with a dedicated physical control channel (DPCCH) and up to six dedicated physical data channels (DPDCH) . The signal is used for voice and data transmission. PRACh The instrument generates a single physical random access channel (PRACH) . This channel is needed to set up the connection between the mobile station and the base station.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TdscdmaSlotModeUp)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> enums.TdscdmaSlotModeUp:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:MODE \n
		Snippet: value: enums.TdscdmaSlotModeUp = driver.source.bb.tdscdma.up.cell.slot.mode.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the mode in which the slot is to work. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: mode: DEDicated| PRACh DEDicated The instrument generates a signal with a dedicated physical control channel (DPCCH) and up to six dedicated physical data channels (DPDCH) . The signal is used for voice and data transmission. PRACh The instrument generates a single physical random access channel (PRACH) . This channel is needed to set up the connection between the mobile station and the base station."""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaSlotModeUp)
