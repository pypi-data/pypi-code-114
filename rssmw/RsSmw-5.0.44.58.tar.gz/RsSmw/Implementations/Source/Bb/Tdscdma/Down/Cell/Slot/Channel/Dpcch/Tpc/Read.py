from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	def set(self, read: enums.TpcReadMode, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:TPC:READ \n
		Snippet: driver.source.bb.tdscdma.down.cell.slot.channel.dpcch.tpc.read.set(read = enums.TpcReadMode.CONTinuous, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the read out mode for the bit pattern of the TPC field. \n
			:param read: CONTinuous| S0A| S1A| S01A| S10A CONTinous The TPC bits are used cyclically. S0A The TPC bits are used once and then the TPC sequence is continued with 0 bits. S1A The TPC bits are used once and then the TPC sequence is continued with 1 bit. S01A The TPC bits are used once and then the TPC sequence is continued with 0 and 1 bits alternately S10A The TPC bits are used once, and then the TPC sequence is continued with 1 and 0 bits alternately
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(read, enums.TpcReadMode)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:TPC:READ {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> enums.TpcReadMode:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:TPC:READ \n
		Snippet: value: enums.TpcReadMode = driver.source.bb.tdscdma.down.cell.slot.channel.dpcch.tpc.read.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the read out mode for the bit pattern of the TPC field. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: read: CONTinuous| S0A| S1A| S01A| S10A CONTinous The TPC bits are used cyclically. S0A The TPC bits are used once and then the TPC sequence is continued with 0 bits. S1A The TPC bits are used once and then the TPC sequence is continued with 1 bit. S01A The TPC bits are used once and then the TPC sequence is continued with 0 and 1 bits alternately S10A The TPC bits are used once, and then the TPC sequence is continued with 1 and 0 bits alternately"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:TPC:READ?')
		return Conversions.str_to_scalar_enum(response, enums.TpcReadMode)
