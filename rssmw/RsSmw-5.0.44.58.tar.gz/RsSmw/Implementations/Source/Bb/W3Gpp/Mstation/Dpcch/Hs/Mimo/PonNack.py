from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PonNack:
	"""PonNack commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ponNack", core, parent)

	def set(self, pon_nack: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:PONNack \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.ponNack.set(pon_nack = 1.0, mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_NACK/NACK of an NACK/NACK response to two scheduled transport blocks
		relative to the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PNACK/NACK used during
		the HARQ-ACK slots is calculated as: PNACK/NACK = PCQI + Poff_NACK/NACK \n
			:param pon_nack: float Range: -10 to 10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(pon_nack)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:PONNack {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:PONNack \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.ponNack.get(mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_NACK/NACK of an NACK/NACK response to two scheduled transport blocks
		relative to the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PNACK/NACK used during
		the HARQ-ACK slots is calculated as: PNACK/NACK = PCQI + Poff_NACK/NACK \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: pon_nack: float Range: -10 to 10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:PONNack?')
		return Conversions.str_to_float(response)
