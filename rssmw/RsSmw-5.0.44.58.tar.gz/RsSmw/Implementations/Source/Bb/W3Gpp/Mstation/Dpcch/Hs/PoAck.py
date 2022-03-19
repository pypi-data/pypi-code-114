from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoAck:
	"""PoAck commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poAck", core, parent)

	def set(self, po_ack: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:POACk \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.poAck.set(po_ack = 1.0, mobileStation = repcap.MobileStation.Default) \n
		(Up to Release 7) Sets the channel power part of the ACK in dB. \n
			:param po_ack: float Range: -10 to 10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(po_ack)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:POACk {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:POACk \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.dpcch.hs.poAck.get(mobileStation = repcap.MobileStation.Default) \n
		(Up to Release 7) Sets the channel power part of the ACK in dB. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: po_ack: float Range: -10 to 10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:POACk?')
		return Conversions.str_to_float(response)
