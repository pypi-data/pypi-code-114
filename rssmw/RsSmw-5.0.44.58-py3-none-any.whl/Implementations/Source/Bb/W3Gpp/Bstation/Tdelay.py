from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdelay:
	"""Tdelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdelay", core, parent)

	def set(self, tdelay: int, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:TDELay \n
		Snippet: driver.source.bb.w3Gpp.bstation.tdelay.set(tdelay = 1, baseStation = repcap.BaseStation.Default) \n
		Adds a time shift for the selected base station compared to base station 1. \n
			:param tdelay: integer Range: 0 to 38400 , Unit: chip
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.decimal_value_to_str(tdelay)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:TDELay {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:TDELay \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.tdelay.get(baseStation = repcap.BaseStation.Default) \n
		Adds a time shift for the selected base station compared to base station 1. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: tdelay: integer Range: 0 to 38400 , Unit: chip"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:TDELay?')
		return Conversions.str_to_int(response)
