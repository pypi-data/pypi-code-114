from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoaAck:
	"""PoaAck commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poaAck", core, parent)

	def set(self, poa_ack: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:POAAck \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.poaAck.set(poa_ack = 1.0, mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_ACK/ACK of an ACK/ACK response to two scheduled transport blocks relative to
		the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PACK/ACK used during the HARQ-ACK
		slots is calculated as: PACK/ACK = PCQI + Poff_ACK/ACK \n
			:param poa_ack: float Range: -10 to 10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(poa_ack)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:POAAck {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:POAAck \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.poaAck.get(mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_ACK/ACK of an ACK/ACK response to two scheduled transport blocks relative to
		the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PACK/ACK used during the HARQ-ACK
		slots is calculated as: PACK/ACK = PCQI + Poff_ACK/ACK \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: poa_ack: float Range: -10 to 10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:POAAck?')
		return Conversions.str_to_float(response)
