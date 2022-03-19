from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: enums.TdscdmaTfciLen, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:TFCI:LENGth \n
		Snippet: driver.source.bb.tdscdma.down.cell.slot.channel.dpcch.tfci.length.set(length = enums.TdscdmaTfciLen._0, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the length of the TFCI field in bits. \n
			:param length: 0| 4| 6| 8| 12| 16| 24| 32| 48
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(length, enums.TdscdmaTfciLen)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:TFCI:LENGth {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default, channelNull=repcap.ChannelNull.Default) -> enums.TdscdmaTfciLen:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SLOT<CH0>:CHANnel<US0>:DPCCh:TFCI:LENGth \n
		Snippet: value: enums.TdscdmaTfciLen = driver.source.bb.tdscdma.down.cell.slot.channel.dpcch.tfci.length.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the length of the TFCI field in bits. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: length: 0| 4| 6| 8| 12| 16| 24| 32| 48"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:TFCI:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaTfciLen)
