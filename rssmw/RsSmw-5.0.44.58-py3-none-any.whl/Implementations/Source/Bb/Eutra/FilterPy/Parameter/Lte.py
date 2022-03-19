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
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:COFFactor \n
		Snippet: value: float = driver.source.bb.eutra.filterPy.parameter.lte.get_coffactor() \n
		Sets the cutoff frequency factor for the LTE filter type. \n
			:return: cutoff_factor: float Range: 0.02 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:COFFactor?')
		return Conversions.str_to_float(response)

	def set_coffactor(self, cutoff_factor: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:COFFactor \n
		Snippet: driver.source.bb.eutra.filterPy.parameter.lte.set_coffactor(cutoff_factor = 1.0) \n
		Sets the cutoff frequency factor for the LTE filter type. \n
			:param cutoff_factor: float Range: 0.02 to 2
		"""
		param = Conversions.decimal_value_to_str(cutoff_factor)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:COFFactor {param}')

	def get_cofs(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:COFS \n
		Snippet: value: float = driver.source.bb.eutra.filterPy.parameter.lte.get_cofs() \n
		Sets the filter parameter. \n
			:return: cut_off_freq_shift: float Range: -1 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:COFS?')
		return Conversions.str_to_float(response)

	def set_cofs(self, cut_off_freq_shift: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:COFS \n
		Snippet: driver.source.bb.eutra.filterPy.parameter.lte.set_cofs(cut_off_freq_shift = 1.0) \n
		Sets the filter parameter. \n
			:param cut_off_freq_shift: float Range: -1 to 1
		"""
		param = Conversions.decimal_value_to_str(cut_off_freq_shift)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:COFS {param}')

	# noinspection PyTypeChecker
	def get_optimization(self) -> enums.FiltOptType:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:OPTimization \n
		Snippet: value: enums.FiltOptType = driver.source.bb.eutra.filterPy.parameter.lte.get_optimization() \n
		Defines the applied LTE filter. \n
			:return: optimization: EVM| ACP| ACPN| BENU Available are EVM, ACP, ACPN (ACP narrow) and BENU (Best EVM, no upsampling) .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:OPTimization?')
		return Conversions.str_to_scalar_enum(response, enums.FiltOptType)

	def set_optimization(self, optimization: enums.FiltOptType) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:OPTimization \n
		Snippet: driver.source.bb.eutra.filterPy.parameter.lte.set_optimization(optimization = enums.FiltOptType.ACP) \n
		Defines the applied LTE filter. \n
			:param optimization: EVM| ACP| ACPN| BENU Available are EVM, ACP, ACPN (ACP narrow) and BENU (Best EVM, no upsampling) .
		"""
		param = Conversions.enum_scalar_to_str(optimization, enums.FiltOptType)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:OPTimization {param}')

	def get_ro_factor(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:ROFactor \n
		Snippet: value: float = driver.source.bb.eutra.filterPy.parameter.lte.get_ro_factor() \n
		Sets the rolloff factor for the LTE filter type. \n
			:return: rolloff_factor: float Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:ROFactor?')
		return Conversions.str_to_float(response)

	def set_ro_factor(self, rolloff_factor: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:FILTer:PARameter:LTE:ROFactor \n
		Snippet: driver.source.bb.eutra.filterPy.parameter.lte.set_ro_factor(rolloff_factor = 1.0) \n
		Sets the rolloff factor for the LTE filter type. \n
			:param rolloff_factor: float Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(rolloff_factor)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:FILTer:PARameter:LTE:ROFactor {param}')
