from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Repetition:
	"""Repetition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("repetition", core, parent)

	def set(self, repetition: int, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:SYNC:REPetition \n
		Snippet: driver.source.bb.tdscdma.up.cell.slot.channel.dpcch.sync.repetition.set(repetition = 1, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the value for the sync shift repetition. \n
			:param repetition: integer Range: 1 to 8
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(repetition)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:SYNC:REPetition {param}')

	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:SYNC:REPetition \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.slot.channel.dpcch.sync.repetition.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the value for the sync shift repetition. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: repetition: integer Range: 1 to 8"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:SYNC:REPetition?')
		return Conversions.str_to_int(response)
