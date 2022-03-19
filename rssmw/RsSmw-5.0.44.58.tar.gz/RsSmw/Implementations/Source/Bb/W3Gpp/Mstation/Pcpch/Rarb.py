from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rarb:
	"""Rarb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rarb", core, parent)

	def set(self, state: bool, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:RARB \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.rarb.set(state = False, mobileStation = repcap.MobileStation.Default) \n
		Enables/disables repeating the selected PCPCH structure during one ARB sequence. \n
			:param state: 1| ON| 0| OFF ON Within one ARB sequence, the selected PCPCH structure is repeated once. OFF The selected PCPCH structure can be repeated several time, depending on the structure length ([:SOURcehw]:BB:W3GPp:MSTationst:PRACh:TIMing:SPERiod?) and the [:SOURcehw]:BB:W3GPp:MSTationst:PCPCh:RAFTer.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.bool_to_str(state)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:RARB {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:RARB \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.pcpch.rarb.get(mobileStation = repcap.MobileStation.Default) \n
		Enables/disables repeating the selected PCPCH structure during one ARB sequence. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: state: 1| ON| 0| OFF ON Within one ARB sequence, the selected PCPCH structure is repeated once. OFF The selected PCPCH structure can be repeated several time, depending on the structure length ([:SOURcehw]:BB:W3GPp:MSTationst:PRACh:TIMing:SPERiod?) and the [:SOURcehw]:BB:W3GPp:MSTationst:PCPCh:RAFTer."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:RARB?')
		return Conversions.str_to_bool(response)
