from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interleaver:
	"""Interleaver commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaver", core, parent)

	def set(self, interleaver: bool, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:INTerleaver \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.interleaver.set(interleaver = False, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command activates or deactivates channel coding interleaver state 1 for the selected channel. Interleaver state 1 can
		be activated and deactivated for each channel individually. The channel is selected via the suffix at TCHannel.
		Interleaver state 2 can only be activated or deactivated for all the channels together
		([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:INTerleaver2) . \n
			:param interleaver: 1| ON| 0| OFF
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.bool_to_str(interleaver)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:INTerleaver {param}')

	def get(self, transportChannelNull=repcap.TransportChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:INTerleaver \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.interleaver.get(transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command activates or deactivates channel coding interleaver state 1 for the selected channel. Interleaver state 1 can
		be activated and deactivated for each channel individually. The channel is selected via the suffix at TCHannel.
		Interleaver state 2 can only be activated or deactivated for all the channels together
		([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:INTerleaver2) . \n
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: interleaver: 1| ON| 0| OFF"""
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:INTerleaver?')
		return Conversions.str_to_bool(response)
