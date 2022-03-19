from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poca:
	"""Poca commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poca", core, parent)

	def set(self, poca: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:POCA \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.poca.set(poca = 1.0, mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_CQI Type A of the PCI/CQI slots in case a CQI Type A report is sent relative
		to the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PCQI Type A used during the
		PCI/CQI slots is calculated as: PCQI Type A = PCQI + Poff_CQI Type A Since the CQI Type B reports are used in a single
		stream transmission, the power PCQI Type B= PCQI. \n
			:param poca: float Range: -10 to 10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(poca)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:POCA {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:POCA \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.poca.get(mobileStation = repcap.MobileStation.Default) \n
		(up to Release 7) Sets the power offset Poff_CQI Type A of the PCI/CQI slots in case a CQI Type A report is sent relative
		to the CQI Power PCQI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:POWer) . The power PCQI Type A used during the
		PCI/CQI slots is calculated as: PCQI Type A = PCQI + Poff_CQI Type A Since the CQI Type B reports are used in a single
		stream transmission, the power PCQI Type B= PCQI. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: poca: float Range: -10 to 10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:POCA?')
		return Conversions.str_to_float(response)
