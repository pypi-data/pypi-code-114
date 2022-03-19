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
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:MIB \n
		Snippet: value: bool = driver.source.bb.oneweb.downlink.pbch.get_mib() \n
		Enables transmission of real MIB data. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:MIB?')
		return Conversions.str_to_bool(response)

	def set_mib(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:MIB \n
		Snippet: driver.source.bb.oneweb.downlink.pbch.set_mib(state = False) \n
		Enables transmission of real MIB data. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:MIB {param}')

	def get_mspare(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:MSPare \n
		Snippet: value: List[str] = driver.source.bb.oneweb.downlink.pbch.get_mspare() \n
		Sets the 10 spare bits in the PBCH transmission. \n
			:return: mib_spare_bits: 64 bit
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:MSPare?')
		return Conversions.str_to_str_list(response)

	def set_mspare(self, mib_spare_bits: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:MSPare \n
		Snippet: driver.source.bb.oneweb.downlink.pbch.set_mspare(mib_spare_bits = ['raw1', 'raw2', 'raw3']) \n
		Sets the 10 spare bits in the PBCH transmission. \n
			:param mib_spare_bits: 64 bit
		"""
		param = Conversions.list_to_csv_str(mib_spare_bits)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:MSPare {param}')

	def get_ratba(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:RATBa \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.pbch.get_ratba() \n
		No command help available \n
			:return: ratio_pb_pa: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:RATBa?')
		return Conversions.str_to_float(response)

	def set_ratba(self, ratio_pb_pa: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:RATBa \n
		Snippet: driver.source.bb.oneweb.downlink.pbch.set_ratba(ratio_pb_pa = 1.0) \n
		No command help available \n
			:param ratio_pb_pa: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio_pb_pa)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:RATBa {param}')

	def get_soffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:SOFFset \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.pbch.get_soffset() \n
		Sets an offset for the start value of the SFN (System Frame Number) . \n
			:return: sfn_offset: integer Range: 0 to 1020
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:SOFFset?')
		return Conversions.str_to_int(response)

	def set_soffset(self, sfn_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:SOFFset \n
		Snippet: driver.source.bb.oneweb.downlink.pbch.set_soffset(sfn_offset = 1) \n
		Sets an offset for the start value of the SFN (System Frame Number) . \n
			:param sfn_offset: integer Range: 0 to 1020
		"""
		param = Conversions.decimal_value_to_str(sfn_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:SOFFset {param}')

	# noinspection PyTypeChecker
	def get_sr_period(self) -> enums.PbchSfnRestPeriod:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:SRPeriod \n
		Snippet: value: enums.PbchSfnRestPeriod = driver.source.bb.oneweb.downlink.pbch.get_sr_period() \n
		No command help available \n
			:return: sfn_rest_period: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:SRPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.PbchSfnRestPeriod)

	def set_sr_period(self, sfn_rest_period: enums.PbchSfnRestPeriod) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PBCH:SRPeriod \n
		Snippet: driver.source.bb.oneweb.downlink.pbch.set_sr_period(sfn_rest_period = enums.PbchSfnRestPeriod.PER3gpp) \n
		No command help available \n
			:param sfn_rest_period: No help available
		"""
		param = Conversions.enum_scalar_to_str(sfn_rest_period, enums.PbchSfnRestPeriod)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PBCH:SRPeriod {param}')
