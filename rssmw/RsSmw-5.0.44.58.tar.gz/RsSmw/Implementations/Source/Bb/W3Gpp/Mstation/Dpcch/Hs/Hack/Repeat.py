from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Repeat:
	"""Repeat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("repeat", core, parent)

	def set(self, hack_rep: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:HACK:REPeat \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.hack.repeat.set(hack_rep = 1, mobileStation = repcap.MobileStation.Default) \n
		Defines the cycle length after that the information in the HS-DPCCH scheduling table is read out again from the beginning. \n
			:param hack_rep: integer Range: 1 to dynamic
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(hack_rep)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:HACK:REPeat {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:HACK:REPeat \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.hack.repeat.get(mobileStation = repcap.MobileStation.Default) \n
		Defines the cycle length after that the information in the HS-DPCCH scheduling table is read out again from the beginning. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: hack_rep: integer Range: 1 to dynamic"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:HACK:REPeat?')
		return Conversions.str_to_int(response)
