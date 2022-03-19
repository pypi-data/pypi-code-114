from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdiversity:
	"""Tdiversity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdiversity", core, parent)

	def set(self, tdiversity: enums.TxDiv, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:TDIVersity \n
		Snippet: driver.source.bb.w3Gpp.bstation.tdiversity.set(tdiversity = enums.TxDiv.ANT1, baseStation = repcap.BaseStation.Default) \n
		Selects the antenna and the antenna configuration to be simulated. To simulate transmit diversity, a two-antenna system
		has to be selected and Open Loop Transmit Diversity has to be activated (command BB:W3GP:BST:OLTD ON) . \n
			:param tdiversity: SANT| ANT1| ANT2| OFF SANT = single-antenna system
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(tdiversity, enums.TxDiv)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:TDIVersity {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.TxDiv:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:TDIVersity \n
		Snippet: value: enums.TxDiv = driver.source.bb.w3Gpp.bstation.tdiversity.get(baseStation = repcap.BaseStation.Default) \n
		Selects the antenna and the antenna configuration to be simulated. To simulate transmit diversity, a two-antenna system
		has to be selected and Open Loop Transmit Diversity has to be activated (command BB:W3GP:BST:OLTD ON) . \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: tdiversity: SANT| ANT1| ANT2| OFF SANT = single-antenna system"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:TDIVersity?')
		return Conversions.str_to_scalar_enum(response, enums.TxDiv)
