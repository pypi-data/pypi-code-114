from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OltDiversity:
	"""OltDiversity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oltDiversity", core, parent)

	def set(self, olt_diversity: bool, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:OLTDiversity \n
		Snippet: driver.source.bb.w3Gpp.bstation.oltDiversity.set(olt_diversity = False, baseStation = repcap.BaseStation.Default) \n
		Activates/deactivates open loop transmit diversity. The antenna whose signal is to be simulated is selected with the
		command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:TDIVersity. \n
			:param olt_diversity: ON| OFF
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.bool_to_str(olt_diversity)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:OLTDiversity {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:OLTDiversity \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.oltDiversity.get(baseStation = repcap.BaseStation.Default) \n
		Activates/deactivates open loop transmit diversity. The antenna whose signal is to be simulated is selected with the
		command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:TDIVersity. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: olt_diversity: ON| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:OLTDiversity?')
		return Conversions.str_to_bool(response)
