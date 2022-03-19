from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoNack:
	"""PoNack commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poNack", core, parent)

	def set(self, po_nack: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:PONAck \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.poNack.set(po_nack = 1.0, mobileStation = repcap.MobileStation.Default) \n
		(Up to Release 7) Sets the channel power part of the NACK in dB. \n
			:param po_nack: float Range: -10 to 10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(po_nack)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:PONAck {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:PONAck \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.dpcch.hs.poNack.get(mobileStation = repcap.MobileStation.Default) \n
		(Up to Release 7) Sets the channel power part of the NACK in dB. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: po_nack: float Range: -10 to 10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:PONAck?')
		return Conversions.str_to_float(response)
