from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TbCount:
	"""TbCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbCount", core, parent)

	def set(self, tb_count: int, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:TBCount \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.tbCount.set(tb_count = 1, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command sets the transport block count. \n
			:param tb_count: integer Range: 1 to 16
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.decimal_value_to_str(tb_count)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:TBCount {param}')

	def get(self, transportChannelNull=repcap.TransportChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:TBCount \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.tbCount.get(transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command sets the transport block count. \n
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: tb_count: integer Range: 1 to 16"""
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:TBCount?')
		return Conversions.str_to_int(response)
