from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TtiDistance:
	"""TtiDistance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttiDistance", core, parent)

	def set(self, tti_distance: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:TTIDistance \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.ttiDistance.set(tti_distance = 1, mobileStation = repcap.MobileStation.Default) \n
		Selects the distance between two packets in HSDPA packet mode. \n
			:param tti_distance: integer Range: 1 to 16
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(tti_distance)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:TTIDistance {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:TTIDistance \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.ttiDistance.get(mobileStation = repcap.MobileStation.Default) \n
		Selects the distance between two packets in HSDPA packet mode. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: tti_distance: integer Range: 1 to 16"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:TTIDistance?')
		return Conversions.str_to_int(response)
