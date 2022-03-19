from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rafter:
	"""Rafter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rafter", core, parent)

	def set(self, repeat_after: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:RAFTer \n
		Snippet: driver.source.bb.w3Gpp.mstation.prach.rafter.set(repeat_after = 1, mobileStation = repcap.MobileStation.Default) \n
		Sets the number of access slots after that the PRACH structure is repeated. \n
			:param repeat_after: integer Range: 1 to 1000
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(repeat_after)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:RAFTer {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:RAFTer \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.prach.rafter.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the number of access slots after that the PRACH structure is repeated. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: repeat_after: integer Range: 1 to 1000"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:RAFTer?')
		return Conversions.str_to_int(response)
