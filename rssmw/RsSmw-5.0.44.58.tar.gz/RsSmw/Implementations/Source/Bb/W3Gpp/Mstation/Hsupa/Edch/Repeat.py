from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Repeat:
	"""Repeat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("repeat", core, parent)

	def set(self, repeat: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:EDCH:REPeat \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.edch.repeat.set(repeat = 1, mobileStation = repcap.MobileStation.Default) \n
		Determine the number of TTIs after that the E-DCH scheduling is repeated. \n
			:param repeat: integer Range: 1 to dynamic
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(repeat)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:EDCH:REPeat {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:EDCH:REPeat \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.hsupa.edch.repeat.get(mobileStation = repcap.MobileStation.Default) \n
		Determine the number of TTIs after that the E-DCH scheduling is repeated. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: repeat: integer Range: 1 to dynamic"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:EDCH:REPeat?')
		return Conversions.str_to_int(response)
