from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccount:
	"""Ccount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccount", core, parent)

	def set(self, ccount: int, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:EUCC:CCOunt \n
		Snippet: driver.source.bb.tdscdma.up.cell.slot.channel.dpcch.eucc.ccount.set(ccount = 1, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the number of the E-DCH Uplink Control Channels (E-UCCH) . \n
			:param ccount: integer Range: 0 to 8
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(ccount)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:EUCC:CCOunt {param}')

	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:EUCC:CCOunt \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.slot.channel.dpcch.eucc.ccount.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the number of the E-DCH Uplink Control Channels (E-UCCH) . \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: ccount: integer Range: 0 to 8"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:EUCC:CCOunt?')
		return Conversions.str_to_int(response)
