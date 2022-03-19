from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pci:
	"""Pci commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pci", core, parent)

	def set(self, pci: int, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, channelQualId=repcap.ChannelQualId.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:PCQI<DI>:PCI \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.row.pcqi.pci.set(pci = 1, mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, channelQualId = repcap.ChannelQualId.Default) \n
		No command help available \n
			:param pci: integer Range: 0 to 3
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcqi')
		"""
		param = Conversions.decimal_value_to_str(pci)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:PCQI{channelQualId_cmd_val}:PCI {param}')

	def get(self, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, channelQualId=repcap.ChannelQualId.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:PCQI<DI>:PCI \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.row.pcqi.pci.get(mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, channelQualId = repcap.ChannelQualId.Default) \n
		No command help available \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcqi')
			:return: pci: integer Range: 0 to 3"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:PCQI{channelQualId_cmd_val}:PCI?')
		return Conversions.str_to_int(response)
