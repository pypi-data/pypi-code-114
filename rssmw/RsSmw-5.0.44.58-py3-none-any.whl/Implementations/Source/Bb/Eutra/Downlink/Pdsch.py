from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsch:
	"""Pdsch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	def get_pb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PDSCh:PB \n
		Snippet: value: int = driver.source.bb.eutra.downlink.pdsch.get_pb() \n
		Sets the cell-specific ratio rho_B/rho_A according to . \n
			:return: pb: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PDSCh:PB?')
		return Conversions.str_to_int(response)

	def set_pb(self, pb: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PDSCh:PB \n
		Snippet: driver.source.bb.eutra.downlink.pdsch.set_pb(pb = 1) \n
		Sets the cell-specific ratio rho_B/rho_A according to . \n
			:param pb: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(pb)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PDSCh:PB {param}')

	def get_ratba(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PDSCh:RATBa \n
		Snippet: value: float = driver.source.bb.eutra.downlink.pdsch.get_ratba() \n
		Sets the transmit energy ratio among the resource elements allocated for teh channel in the OFDM symbols containing
		reference signal (P_B) and such not containing one (P_A) . \n
			:return: ratio_pb_pa: float Range: -10 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PDSCh:RATBa?')
		return Conversions.str_to_float(response)

	def set_ratba(self, ratio_pb_pa: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PDSCh:RATBa \n
		Snippet: driver.source.bb.eutra.downlink.pdsch.set_ratba(ratio_pb_pa = 1.0) \n
		Sets the transmit energy ratio among the resource elements allocated for teh channel in the OFDM symbols containing
		reference signal (P_B) and such not containing one (P_A) . \n
			:param ratio_pb_pa: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(ratio_pb_pa)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PDSCh:RATBa {param}')
