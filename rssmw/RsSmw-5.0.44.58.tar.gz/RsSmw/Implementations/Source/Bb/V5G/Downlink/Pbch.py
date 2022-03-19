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
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:MIB \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.pbch.get_mib() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PBCH:MIB?')
		return Conversions.str_to_bool(response)

	def set_mib(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:MIB \n
		Snippet: driver.source.bb.v5G.downlink.pbch.set_mib(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PBCH:MIB {param}')

	def get_mspare(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:MSPare \n
		Snippet: value: List[str] = driver.source.bb.v5G.downlink.pbch.get_mspare() \n
		No command help available \n
			:return: mib_spare_bits: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PBCH:MSPare?')
		return Conversions.str_to_str_list(response)

	def set_mspare(self, mib_spare_bits: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:MSPare \n
		Snippet: driver.source.bb.v5G.downlink.pbch.set_mspare(mib_spare_bits = ['raw1', 'raw2', 'raw3']) \n
		No command help available \n
			:param mib_spare_bits: No help available
		"""
		param = Conversions.list_to_csv_str(mib_spare_bits)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PBCH:MSPare {param}')

	def get_ratba(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:RATBa \n
		Snippet: value: float = driver.source.bb.v5G.downlink.pbch.get_ratba() \n
		No command help available \n
			:return: ratio_pb_pa: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PBCH:RATBa?')
		return Conversions.str_to_float(response)

	def set_ratba(self, ratio_pb_pa: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:RATBa \n
		Snippet: driver.source.bb.v5G.downlink.pbch.set_ratba(ratio_pb_pa = 1.0) \n
		No command help available \n
			:param ratio_pb_pa: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio_pb_pa)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PBCH:RATBa {param}')

	def get_soffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:SOFFset \n
		Snippet: value: int = driver.source.bb.v5G.downlink.pbch.get_soffset() \n
		No command help available \n
			:return: sfn_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PBCH:SOFFset?')
		return Conversions.str_to_int(response)

	def set_soffset(self, sfn_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:SOFFset \n
		Snippet: driver.source.bb.v5G.downlink.pbch.set_soffset(sfn_offset = 1) \n
		No command help available \n
			:param sfn_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(sfn_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PBCH:SOFFset {param}')

	# noinspection PyTypeChecker
	def get_sr_period(self) -> enums.PbchSfnRestPeriod:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:SRPeriod \n
		Snippet: value: enums.PbchSfnRestPeriod = driver.source.bb.v5G.downlink.pbch.get_sr_period() \n
		No command help available \n
			:return: sfn_rest_period: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PBCH:SRPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.PbchSfnRestPeriod)

	def set_sr_period(self, sfn_rest_period: enums.PbchSfnRestPeriod) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PBCH:SRPeriod \n
		Snippet: driver.source.bb.v5G.downlink.pbch.set_sr_period(sfn_rest_period = enums.PbchSfnRestPeriod.PER3gpp) \n
		No command help available \n
			:param sfn_rest_period: No help available
		"""
		param = Conversions.enum_scalar_to_str(sfn_rest_period, enums.PbchSfnRestPeriod)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PBCH:SRPeriod {param}')
