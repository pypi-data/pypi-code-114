from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ds:
	"""Ds commands group definition. 9 total commands, 0 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ds", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:CATalog \n
		Snippet: value: List[str] = driver.source.bb.stereo.ds.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_deviation(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:DEViation \n
		Snippet: value: int = driver.source.bb.stereo.ds.get_deviation() \n
		No command help available \n
			:return: deviation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:DEViation?')
		return Conversions.str_to_int(response)

	def set_deviation(self, deviation: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:DEViation \n
		Snippet: driver.source.bb.stereo.ds.set_deviation(deviation = 1) \n
		No command help available \n
			:param deviation: No help available
		"""
		param = Conversions.decimal_value_to_str(deviation)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:DS:DEViation {param}')

	def get_drate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:DRATe \n
		Snippet: value: float = driver.source.bb.stereo.ds.get_drate() \n
		No command help available \n
			:return: drate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:DRATe?')
		return Conversions.str_to_float(response)

	def set_dselect(self, dselect: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:DSELect \n
		Snippet: driver.source.bb.stereo.ds.set_dselect(dselect = '1') \n
		No command help available \n
			:param dselect: No help available
		"""
		param = Conversions.value_to_quoted_str(dselect)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:DS:DSELect {param}')

	# noinspection PyTypeChecker
	def get_dset(self) -> enums.FmStereoRdsRbdsCfgDataSource:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:DSET \n
		Snippet: value: enums.FmStereoRdsRbdsCfgDataSource = driver.source.bb.stereo.ds.get_dset() \n
		No command help available \n
			:return: dset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:DSET?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoRdsRbdsCfgDataSource)

	def set_dset(self, dset: enums.FmStereoRdsRbdsCfgDataSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:DSET \n
		Snippet: driver.source.bb.stereo.ds.set_dset(dset = enums.FmStereoRdsRbdsCfgDataSource.GRPList) \n
		No command help available \n
			:param dset: No help available
		"""
		param = Conversions.enum_scalar_to_str(dset, enums.FmStereoRdsRbdsCfgDataSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:DS:DSET {param}')

	# noinspection PyTypeChecker
	def get_gim(self) -> enums.FmStereoRdsRbdsCfgUsrGrpBeh:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:GIM \n
		Snippet: value: enums.FmStereoRdsRbdsCfgUsrGrpBeh = driver.source.bb.stereo.ds.get_gim() \n
		No command help available \n
			:return: gim: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:GIM?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoRdsRbdsCfgUsrGrpBeh)

	def set_gim(self, gim: enums.FmStereoRdsRbdsCfgUsrGrpBeh) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:GIM \n
		Snippet: driver.source.bb.stereo.ds.set_gim(gim = enums.FmStereoRdsRbdsCfgUsrGrpBeh.HEXFormat) \n
		No command help available \n
			:param gim: No help available
		"""
		param = Conversions.enum_scalar_to_str(gim, enums.FmStereoRdsRbdsCfgUsrGrpBeh)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:DS:GIM {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FmStereoCfgMode:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:MODE \n
		Snippet: value: enums.FmStereoCfgMode = driver.source.bb.stereo.ds.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoCfgMode)

	def set_mode(self, mode: enums.FmStereoCfgMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:MODE \n
		Snippet: driver.source.bb.stereo.ds.set_mode(mode = enums.FmStereoCfgMode.RBDS) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FmStereoCfgMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:DS:MODE {param}')

	def get_phase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:PHASe \n
		Snippet: value: float = driver.source.bb.stereo.ds.get_phase() \n
		No command help available \n
			:return: phase: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:PHASe?')
		return Conversions.str_to_float(response)

	def set_phase(self, phase: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:PHASe \n
		Snippet: driver.source.bb.stereo.ds.set_phase(phase = 1.0) \n
		No command help available \n
			:param phase: No help available
		"""
		param = Conversions.decimal_value_to_str(phase)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:DS:PHASe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:STATe \n
		Snippet: value: bool = driver.source.bb.stereo.ds.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:DS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:DS:STATe \n
		Snippet: driver.source.bb.stereo.ds.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:DS:STATe {param}')
