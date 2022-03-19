from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Utilities import trim_str_response
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: str, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:SYNC:PATTern \n
		Snippet: driver.source.bb.tdscdma.down.cell.slot.channel.dpcch.sync.pattern.set(pattern = '1', cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the bit pattern for the sync shift. \n
			:param pattern: string The maximum pattern length is 64 bits.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(pattern)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:SYNC:PATTern {param}')

	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:SYNC:PATTern \n
		Snippet: value: str = driver.source.bb.tdscdma.down.cell.slot.channel.dpcch.sync.pattern.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the bit pattern for the sync shift. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: pattern: string The maximum pattern length is 64 bits."""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:SYNC:PATTern?')
		return trim_str_response(response)
