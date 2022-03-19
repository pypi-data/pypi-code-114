from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pbch:
	"""Pbch commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pbch", core, parent)

	def get_mib(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:MIB \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.pbch.get_mib() \n
		Enables transmission of real MIB data. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PBCH:MIB?')
		return Conversions.str_to_bool(response)

	def set_mib(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:MIB \n
		Snippet: driver.source.bb.eutra.downlink.pbch.set_mib(state = False) \n
		Enables transmission of real MIB data. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PBCH:MIB {param}')

	def get_mspare(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:MSPare \n
		Snippet: value: List[str] = driver.source.bb.eutra.downlink.pbch.get_mspare() \n
		Sets the 10 spare bits in the PBCH transmission. \n
			:return: mib_spare_bits: 64 bit
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PBCH:MSPare?')
		return Conversions.str_to_str_list(response)

	def set_mspare(self, mib_spare_bits: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:MSPare \n
		Snippet: driver.source.bb.eutra.downlink.pbch.set_mspare(mib_spare_bits = ['raw1', 'raw2', 'raw3']) \n
		Sets the 10 spare bits in the PBCH transmission. \n
			:param mib_spare_bits: 64 bit
		"""
		param = Conversions.list_to_csv_str(mib_spare_bits)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PBCH:MSPare {param}')

	def get_ratba(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:RATBa \n
		Snippet: value: float = driver.source.bb.eutra.downlink.pbch.get_ratba() \n
		Sets the transmit energy ratio among the resource elements allocated for teh channel in the OFDM symbols containing
		reference signal (P_B) and such not containing one (P_A) . \n
			:return: ratio_pb_pa: float Range: -10 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PBCH:RATBa?')
		return Conversions.str_to_float(response)

	def set_ratba(self, ratio_pb_pa: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:RATBa \n
		Snippet: driver.source.bb.eutra.downlink.pbch.set_ratba(ratio_pb_pa = 1.0) \n
		Sets the transmit energy ratio among the resource elements allocated for teh channel in the OFDM symbols containing
		reference signal (P_B) and such not containing one (P_A) . \n
			:param ratio_pb_pa: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(ratio_pb_pa)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PBCH:RATBa {param}')

	def get_soffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:SOFFset \n
		Snippet: value: int = driver.source.bb.eutra.downlink.pbch.get_soffset() \n
		Sets an offset for the start value of the SFN (System Frame Number) . \n
			:return: sfn_offset: integer Range: 0 to 1020
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PBCH:SOFFset?')
		return Conversions.str_to_int(response)

	def set_soffset(self, sfn_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:SOFFset \n
		Snippet: driver.source.bb.eutra.downlink.pbch.set_soffset(sfn_offset = 1) \n
		Sets an offset for the start value of the SFN (System Frame Number) . \n
			:param sfn_offset: integer Range: 0 to 1020
		"""
		param = Conversions.decimal_value_to_str(sfn_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PBCH:SOFFset {param}')

	# noinspection PyTypeChecker
	def get_sr_period(self) -> enums.PbchSfnRestPeriod:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:SRPeriod \n
		Snippet: value: enums.PbchSfnRestPeriod = driver.source.bb.eutra.downlink.pbch.get_sr_period() \n
		Determines the time span after which the SFN (System Frame Number) restarts. \n
			:return: sfn_rest_period: PERSlength | PER3gpp PER3gpp = '3GPP (1024 Frames) ' PERSlength = SFN restart period to the ARB sequence length
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PBCH:SRPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.PbchSfnRestPeriod)

	def set_sr_period(self, sfn_rest_period: enums.PbchSfnRestPeriod) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PBCH:SRPeriod \n
		Snippet: driver.source.bb.eutra.downlink.pbch.set_sr_period(sfn_rest_period = enums.PbchSfnRestPeriod.PER3gpp) \n
		Determines the time span after which the SFN (System Frame Number) restarts. \n
			:param sfn_rest_period: PERSlength | PER3gpp PER3gpp = '3GPP (1024 Frames) ' PERSlength = SFN restart period to the ARB sequence length
		"""
		param = Conversions.enum_scalar_to_str(sfn_rest_period, enums.PbchSfnRestPeriod)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PBCH:SRPeriod {param}')
