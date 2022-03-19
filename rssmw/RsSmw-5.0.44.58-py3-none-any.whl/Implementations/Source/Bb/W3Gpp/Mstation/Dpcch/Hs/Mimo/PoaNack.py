from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoaNack:
	"""PoaNack commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poaNack", core, parent)

	def set(self, poa_nack: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:POANack \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.poaNack.set(poa_nack = 1.0, mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_ACK/NACK of an ACK/NACK response to two scheduled transport blocks relative
		to the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PACK/NACK used during the HARQ-ACK
		slots is calculated as: PACK/NACK = PCQI + Poff_ACK/NACK \n
			:param poa_nack: float Range: -10 to 10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(poa_nack)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:POANack {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:POANack \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.poaNack.get(mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_ACK/NACK of an ACK/NACK response to two scheduled transport blocks relative
		to the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PACK/NACK used during the HARQ-ACK
		slots is calculated as: PACK/NACK = PCQI + Poff_ACK/NACK \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: poa_nack: float Range: -10 to 10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:POANack?')
		return Conversions.str_to_float(response)
