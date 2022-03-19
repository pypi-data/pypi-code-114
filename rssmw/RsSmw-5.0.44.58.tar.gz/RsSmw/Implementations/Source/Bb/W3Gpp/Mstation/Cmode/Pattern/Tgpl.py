from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tgpl:
	"""Tgpl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tgpl", core, parent)

	def set(self, tgpl: int, mobileStation=repcap.MobileStation.Default, patternIx=repcap.PatternIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CMODe:PATTern<CH>:TGPL \n
		Snippet: driver.source.bb.w3Gpp.mstation.cmode.pattern.tgpl.set(tgpl = 1, mobileStation = repcap.MobileStation.Default, patternIx = repcap.PatternIx.Default) \n
		The command sets the transmission gap pattern lengths. Setting 0 is available only for pattern 2. The transmission gap
		pattern lengths of the base station with the same suffix as the selected user equipment is set to the same value. \n
			:param tgpl: integer Range: 0 to 100
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param patternIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
		"""
		param = Conversions.decimal_value_to_str(tgpl)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		patternIx_cmd_val = self._cmd_group.get_repcap_cmd_value(patternIx, repcap.PatternIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CMODe:PATTern{patternIx_cmd_val}:TGPL {param}')

	def get(self, mobileStation=repcap.MobileStation.Default, patternIx=repcap.PatternIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CMODe:PATTern<CH>:TGPL \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.cmode.pattern.tgpl.get(mobileStation = repcap.MobileStation.Default, patternIx = repcap.PatternIx.Default) \n
		The command sets the transmission gap pattern lengths. Setting 0 is available only for pattern 2. The transmission gap
		pattern lengths of the base station with the same suffix as the selected user equipment is set to the same value. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param patternIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
			:return: tgpl: integer Range: 0 to 100"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		patternIx_cmd_val = self._cmd_group.get_repcap_cmd_value(patternIx, repcap.PatternIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CMODe:PATTern{patternIx_cmd_val}:TGPL?')
		return Conversions.str_to_int(response)
