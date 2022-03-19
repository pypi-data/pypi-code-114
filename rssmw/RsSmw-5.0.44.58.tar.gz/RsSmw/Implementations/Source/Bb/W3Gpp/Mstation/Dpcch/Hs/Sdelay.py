from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sdelay:
	"""Sdelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sdelay", core, parent)

	def set(self, sdelay: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:SDELay \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.sdelay.set(sdelay = 1, mobileStation = repcap.MobileStation.Default) \n
		Sets the delay between the uplink HS-DPCCH and the frame of uplink DPCH. \n
			:param sdelay: integer a multiple m of 256 chips according to TS 25.211 7.7 Range: 0 to 250, Unit: * 256 Chips
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(sdelay)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:SDELay {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:SDELay \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.sdelay.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the delay between the uplink HS-DPCCH and the frame of uplink DPCH. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: sdelay: integer a multiple m of 256 chips according to TS 25.211 7.7 Range: 0 to 250, Unit: * 256 Chips"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:SDELay?')
		return Conversions.str_to_int(response)
