from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	# noinspection PyTypeChecker
	def get_fh_mode(self) -> enums.UlFreqHopMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:FHMode \n
		Snippet: value: enums.UlFreqHopMode = driver.source.bb.v5G.uplink.pusch.get_fh_mode() \n
		No command help available \n
			:return: freq_hopping_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUSCh:FHMode?')
		return Conversions.str_to_scalar_enum(response, enums.UlFreqHopMode)

	def set_fh_mode(self, freq_hopping_mode: enums.UlFreqHopMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:FHMode \n
		Snippet: driver.source.bb.v5G.uplink.pusch.set_fh_mode(freq_hopping_mode = enums.UlFreqHopMode.INTer) \n
		No command help available \n
			:param freq_hopping_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(freq_hopping_mode, enums.UlFreqHopMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUSCh:FHMode {param}')

	def get_fh_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:FHOFfset \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pusch.get_fh_offset() \n
		No command help available \n
			:return: fhopp_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUSCh:FHOFfset?')
		return Conversions.str_to_int(response)

	def set_fh_offset(self, fhopp_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:FHOFfset \n
		Snippet: driver.source.bb.v5G.uplink.pusch.set_fh_offset(fhopp_offset = 1) \n
		No command help available \n
			:param fhopp_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(fhopp_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUSCh:FHOFfset {param}')

	def get_nhoffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:NHOFfset \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pusch.get_nhoffset() \n
		No command help available \n
			:return: nb_hopping_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUSCh:NHOFfset?')
		return Conversions.str_to_int(response)

	def set_nhoffset(self, nb_hopping_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:NHOFfset \n
		Snippet: driver.source.bb.v5G.uplink.pusch.set_nhoffset(nb_hopping_offset = 1) \n
		No command help available \n
			:param nb_hopping_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(nb_hopping_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUSCh:NHOFfset {param}')

	def get_nhopping(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:NHOPping \n
		Snippet: value: bool = driver.source.bb.v5G.uplink.pusch.get_nhopping() \n
		No command help available \n
			:return: nb_hopping: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUSCh:NHOPping?')
		return Conversions.str_to_bool(response)

	def set_nhopping(self, nb_hopping: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:NHOPping \n
		Snippet: driver.source.bb.v5G.uplink.pusch.set_nhopping(nb_hopping = False) \n
		No command help available \n
			:param nb_hopping: No help available
		"""
		param = Conversions.bool_to_str(nb_hopping)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUSCh:NHOPping {param}')

	def get_nosm(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:NOSM \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pusch.get_nosm() \n
		No command help available \n
			:return: sub_band_count: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUSCh:NOSM?')
		return Conversions.str_to_int(response)

	def set_nosm(self, sub_band_count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUSCh:NOSM \n
		Snippet: driver.source.bb.v5G.uplink.pusch.set_nosm(sub_band_count = 1) \n
		No command help available \n
			:param sub_band_count: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_band_count)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUSCh:NOSM {param}')
