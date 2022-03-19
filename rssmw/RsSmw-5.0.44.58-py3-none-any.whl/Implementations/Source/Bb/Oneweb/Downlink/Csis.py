from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csis:
	"""Csis commands group definition. 11 total commands, 0 Subgroups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csis", core, parent)

	def get_config(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:CONFig \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.csis.get_config() \n
		No command help available \n
			:return: csi_rs_config: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:CONFig?')
		return Conversions.str_to_int(response)

	def set_config(self, csi_rs_config: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:CONFig \n
		Snippet: driver.source.bb.oneweb.downlink.csis.set_config(csi_rs_config = 1) \n
		No command help available \n
			:param csi_rs_config: No help available
		"""
		param = Conversions.decimal_value_to_str(csi_rs_config)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:CONFig {param}')

	# noinspection PyTypeChecker
	def get_nap(self) -> enums.CsiRsNumAp:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:NAP \n
		Snippet: value: enums.CsiRsNumAp = driver.source.bb.oneweb.downlink.csis.get_nap() \n
		No command help available \n
			:return: csi_rs_num_ap: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:NAP?')
		return Conversions.str_to_scalar_enum(response, enums.CsiRsNumAp)

	def set_nap(self, csi_rs_num_ap: enums.CsiRsNumAp) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:NAP \n
		Snippet: driver.source.bb.oneweb.downlink.csis.set_nap(csi_rs_num_ap = enums.CsiRsNumAp.AP1) \n
		No command help available \n
			:param csi_rs_num_ap: No help available
		"""
		param = Conversions.enum_scalar_to_str(csi_rs_num_ap, enums.CsiRsNumAp)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:NAP {param}')

	def get_pow(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:POW \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.csis.get_pow() \n
		No command help available \n
			:return: csi_rs_pow: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:POW?')
		return Conversions.str_to_float(response)

	def set_pow(self, csi_rs_pow: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:POW \n
		Snippet: driver.source.bb.oneweb.downlink.csis.set_pow(csi_rs_pow = 1.0) \n
		No command help available \n
			:param csi_rs_pow: No help available
		"""
		param = Conversions.decimal_value_to_str(csi_rs_pow)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:POW {param}')

	def get_sf_delta(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:SFDelta \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.csis.get_sf_delta() \n
		No command help available \n
			:return: csi_rs_offs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:SFDelta?')
		return Conversions.str_to_int(response)

	def get_sfi(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:SFI \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.csis.get_sfi() \n
		No command help available \n
			:return: csi_rs_sf_conf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:SFI?')
		return Conversions.str_to_int(response)

	def set_sfi(self, csi_rs_sf_conf: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:SFI \n
		Snippet: driver.source.bb.oneweb.downlink.csis.set_sfi(csi_rs_sf_conf = 1) \n
		No command help available \n
			:param csi_rs_sf_conf: No help available
		"""
		param = Conversions.decimal_value_to_str(csi_rs_sf_conf)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:SFI {param}')

	def get_sft(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:SFT \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.csis.get_sft() \n
		No command help available \n
			:return: csi_rs_period: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:SFT?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.downlink.csis.get_state() \n
		No command help available \n
			:return: csi_rs_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, csi_rs_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:STATe \n
		Snippet: driver.source.bb.oneweb.downlink.csis.set_state(csi_rs_state = False) \n
		No command help available \n
			:param csi_rs_state: No help available
		"""
		param = Conversions.bool_to_str(csi_rs_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:STATe {param}')

	def get_zp(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:ZP \n
		Snippet: value: List[str] = driver.source.bb.oneweb.downlink.csis.get_zp() \n
		No command help available \n
			:return: zero_power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:ZP?')
		return Conversions.str_to_str_list(response)

	def set_zp(self, zero_power: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:ZP \n
		Snippet: driver.source.bb.oneweb.downlink.csis.set_zp(zero_power = ['raw1', 'raw2', 'raw3']) \n
		No command help available \n
			:param zero_power: No help available
		"""
		param = Conversions.list_to_csv_str(zero_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:ZP {param}')

	def get_zp_delta(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:ZPDelta \n
		Snippet: value: List[str] = driver.source.bb.oneweb.downlink.csis.get_zp_delta() \n
		No command help available \n
			:return: zero_power_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:ZPDelta?')
		return Conversions.str_to_str_list(response)

	def get_zpi(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:ZPI \n
		Snippet: value: List[str] = driver.source.bb.oneweb.downlink.csis.get_zpi() \n
		No command help available \n
			:return: zero_pow_conf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:ZPI?')
		return Conversions.str_to_str_list(response)

	def set_zpi(self, zero_pow_conf: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:ZPI \n
		Snippet: driver.source.bb.oneweb.downlink.csis.set_zpi(zero_pow_conf = ['raw1', 'raw2', 'raw3']) \n
		No command help available \n
			:param zero_pow_conf: No help available
		"""
		param = Conversions.list_to_csv_str(zero_pow_conf)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:ZPI {param}')

	def get_zpt(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSIS:ZPT \n
		Snippet: value: List[str] = driver.source.bb.oneweb.downlink.csis.get_zpt() \n
		No command help available \n
			:return: zero_power_per: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSIS:ZPT?')
		return Conversions.str_to_str_list(response)
