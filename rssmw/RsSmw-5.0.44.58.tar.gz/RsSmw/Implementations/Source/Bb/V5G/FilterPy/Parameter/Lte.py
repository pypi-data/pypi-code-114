from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lte:
	"""Lte commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	def get_coffactor(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:COFFactor \n
		Snippet: value: float = driver.source.bb.v5G.filterPy.parameter.lte.get_coffactor() \n
		No command help available \n
			:return: cutoff_factor: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:COFFactor?')
		return Conversions.str_to_float(response)

	def set_coffactor(self, cutoff_factor: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:COFFactor \n
		Snippet: driver.source.bb.v5G.filterPy.parameter.lte.set_coffactor(cutoff_factor = 1.0) \n
		No command help available \n
			:param cutoff_factor: No help available
		"""
		param = Conversions.decimal_value_to_str(cutoff_factor)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:COFFactor {param}')

	def get_cofs(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:COFS \n
		Snippet: value: float = driver.source.bb.v5G.filterPy.parameter.lte.get_cofs() \n
		No command help available \n
			:return: cut_off_freq_shift: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:COFS?')
		return Conversions.str_to_float(response)

	def set_cofs(self, cut_off_freq_shift: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:COFS \n
		Snippet: driver.source.bb.v5G.filterPy.parameter.lte.set_cofs(cut_off_freq_shift = 1.0) \n
		No command help available \n
			:param cut_off_freq_shift: No help available
		"""
		param = Conversions.decimal_value_to_str(cut_off_freq_shift)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:COFS {param}')

	# noinspection PyTypeChecker
	def get_optimization(self) -> enums.FiltOptType:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:OPTimization \n
		Snippet: value: enums.FiltOptType = driver.source.bb.v5G.filterPy.parameter.lte.get_optimization() \n
		No command help available \n
			:return: optimization: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:OPTimization?')
		return Conversions.str_to_scalar_enum(response, enums.FiltOptType)

	def set_optimization(self, optimization: enums.FiltOptType) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:OPTimization \n
		Snippet: driver.source.bb.v5G.filterPy.parameter.lte.set_optimization(optimization = enums.FiltOptType.ACP) \n
		No command help available \n
			:param optimization: No help available
		"""
		param = Conversions.enum_scalar_to_str(optimization, enums.FiltOptType)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:OPTimization {param}')

	def get_ro_factor(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:ROFactor \n
		Snippet: value: float = driver.source.bb.v5G.filterPy.parameter.lte.get_ro_factor() \n
		No command help available \n
			:return: rolloff_factor: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:ROFactor?')
		return Conversions.str_to_float(response)

	def set_ro_factor(self, rolloff_factor: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:PARameter:LTE:ROFactor \n
		Snippet: driver.source.bb.v5G.filterPy.parameter.lte.set_ro_factor(rolloff_factor = 1.0) \n
		No command help available \n
			:param rolloff_factor: No help available
		"""
		param = Conversions.decimal_value_to_str(rolloff_factor)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:FILTer:PARameter:LTE:ROFactor {param}')
