from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdcch:
	"""Pdcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	def get_ratba(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PDCCh:RATBa \n
		Snippet: value: float = driver.source.bb.eutra.downlink.pdcch.get_ratba() \n
		Sets the transmit energy ratio among the resource elements allocated for teh channel in the OFDM symbols containing
		reference signal (P_B) and such not containing one (P_A) . \n
			:return: ratio_pb_ba: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PDCCh:RATBa?')
		return Conversions.str_to_float(response)

	def set_ratba(self, ratio_pb_ba: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PDCCh:RATBa \n
		Snippet: driver.source.bb.eutra.downlink.pdcch.set_ratba(ratio_pb_ba = 1.0) \n
		Sets the transmit energy ratio among the resource elements allocated for teh channel in the OFDM symbols containing
		reference signal (P_B) and such not containing one (P_A) . \n
			:param ratio_pb_ba: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(ratio_pb_ba)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PDCCh:RATBa {param}')
