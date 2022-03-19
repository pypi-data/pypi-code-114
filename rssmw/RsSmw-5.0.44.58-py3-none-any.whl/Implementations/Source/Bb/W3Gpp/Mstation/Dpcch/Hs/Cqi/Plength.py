from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plength:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, plength: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:CQI:PLENgth \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.cqi.plength.set(plength = 1, mobileStation = repcap.MobileStation.Default) \n
		Sets the length of the CQI sequence.
		The values of the CQI sequence are defined with command [:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:CQI<ch>[:VALues].
		The pattern is generated cyclically. \n
			:param plength: integer Range: 1 to 10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(plength)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:CQI:PLENgth {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:CQI:PLENgth \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.cqi.plength.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the length of the CQI sequence.
		The values of the CQI sequence are defined with command [:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:CQI<ch>[:VALues].
		The pattern is generated cyclically. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: plength: integer Range: 1 to 10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:CQI:PLENgth?')
		return Conversions.str_to_int(response)
