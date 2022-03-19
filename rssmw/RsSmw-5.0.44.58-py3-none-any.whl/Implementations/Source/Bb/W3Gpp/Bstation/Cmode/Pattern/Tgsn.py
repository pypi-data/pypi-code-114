from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tgsn:
	"""Tgsn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tgsn", core, parent)

	def set(self, tgsn: int, baseStation=repcap.BaseStation.Default, patternIx=repcap.PatternIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:PATTern<CH>:TGSN \n
		Snippet: driver.source.bb.w3Gpp.bstation.cmode.pattern.tgsn.set(tgsn = 1, baseStation = repcap.BaseStation.Default, patternIx = repcap.PatternIx.Default) \n
		Sets the transmission gap slot number of pattern 1. \n
			:param tgsn: integer Range: 0 to 14
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param patternIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
		"""
		param = Conversions.decimal_value_to_str(tgsn)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		patternIx_cmd_val = self._cmd_group.get_repcap_cmd_value(patternIx, repcap.PatternIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:PATTern{patternIx_cmd_val}:TGSN {param}')

	def get(self, baseStation=repcap.BaseStation.Default, patternIx=repcap.PatternIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:PATTern<CH>:TGSN \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.cmode.pattern.tgsn.get(baseStation = repcap.BaseStation.Default, patternIx = repcap.PatternIx.Default) \n
		Sets the transmission gap slot number of pattern 1. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param patternIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
			:return: tgsn: integer Range: 0 to 14"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		patternIx_cmd_val = self._cmd_group.get_repcap_cmd_value(patternIx, repcap.PatternIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:PATTern{patternIx_cmd_val}:TGSN?')
		return Conversions.str_to_int(response)
