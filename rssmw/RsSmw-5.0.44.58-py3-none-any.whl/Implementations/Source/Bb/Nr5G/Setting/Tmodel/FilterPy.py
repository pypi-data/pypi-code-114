from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	# noinspection PyTypeChecker
	def get_bw(self) -> enums.FilterBandwidth:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:BW \n
		Snippet: value: enums.FilterBandwidth = driver.source.bb.nr5G.setting.tmodel.filterPy.get_bw() \n
		Applies a bandwidth filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:return: filter_bandwidth: ALL| F5| F10| F15| F20| F25| F30| F40| F50| F60| F70| F80| F90| F100| F200| F400
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:BW?')
		return Conversions.str_to_scalar_enum(response, enums.FilterBandwidth)

	def set_bw(self, filter_bandwidth: enums.FilterBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:BW \n
		Snippet: driver.source.bb.nr5G.setting.tmodel.filterPy.set_bw(filter_bandwidth = enums.FilterBandwidth.ALL) \n
		Applies a bandwidth filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:param filter_bandwidth: ALL| F5| F10| F15| F20| F25| F30| F40| F50| F60| F70| F80| F90| F100| F200| F400
		"""
		param = Conversions.enum_scalar_to_str(filter_bandwidth, enums.FilterBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:BW {param}')

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog \n
		Snippet: value: List[str] = driver.source.bb.nr5G.setting.tmodel.filterPy.get_catalog() \n
		Queries the filenames of predefined test signal files in the default directory after applying a filter. \n
			:return: nr_5_gcat_name_tmod_modified: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:CATalog?')
		return Conversions.str_to_str_list(response)

	# noinspection PyTypeChecker
	def get_duplexing(self) -> enums.FilterDuplexing:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:DUPLexing \n
		Snippet: value: enums.FilterDuplexing = driver.source.bb.nr5G.setting.tmodel.filterPy.get_duplexing() \n
		Applies a duplexing filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:return: filter_duplexing: ALL| FDD| TDD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.FilterDuplexing)

	def set_duplexing(self, filter_duplexing: enums.FilterDuplexing) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:DUPLexing \n
		Snippet: driver.source.bb.nr5G.setting.tmodel.filterPy.set_duplexing(filter_duplexing = enums.FilterDuplexing.ALL) \n
		Applies a duplexing filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:param filter_duplexing: ALL| FDD| TDD
		"""
		param = Conversions.enum_scalar_to_str(filter_duplexing, enums.FilterDuplexing)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:DUPLexing {param}')

	# noinspection PyTypeChecker
	def get_freq(self) -> enums.FilterFreqRange:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:FREQ \n
		Snippet: value: enums.FilterFreqRange = driver.source.bb.nr5G.setting.tmodel.filterPy.get_freq() \n
		Applies a frequency range filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:return: filter_freq_range: ALL| FR1| FR2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:FREQ?')
		return Conversions.str_to_scalar_enum(response, enums.FilterFreqRange)

	def set_freq(self, filter_freq_range: enums.FilterFreqRange) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:FREQ \n
		Snippet: driver.source.bb.nr5G.setting.tmodel.filterPy.set_freq(filter_freq_range = enums.FilterFreqRange.ALL) \n
		Applies a frequency range filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:param filter_freq_range: ALL| FR1| FR2
		"""
		param = Conversions.enum_scalar_to_str(filter_freq_range, enums.FilterFreqRange)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:FREQ {param}')

	# noinspection PyTypeChecker
	def get_scs(self) -> enums.FilterSubcarrierSpacing:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:SCS \n
		Snippet: value: enums.FilterSubcarrierSpacing = driver.source.bb.nr5G.setting.tmodel.filterPy.get_scs() \n
		Applies a subcarrier spacing filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:return: filter_scs: ALL| F15| F30| F60| F120
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:SCS?')
		return Conversions.str_to_scalar_enum(response, enums.FilterSubcarrierSpacing)

	def set_scs(self, filter_scs: enums.FilterSubcarrierSpacing) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:SCS \n
		Snippet: driver.source.bb.nr5G.setting.tmodel.filterPy.set_scs(filter_scs = enums.FilterSubcarrierSpacing.ALL) \n
		Applies a subcarrier spacing filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:param filter_scs: ALL| F15| F30| F60| F120
		"""
		param = Conversions.enum_scalar_to_str(filter_scs, enums.FilterSubcarrierSpacing)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:SCS {param}')

	# noinspection PyTypeChecker
	def get_tmodel(self) -> enums.FilterTestModels:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:TMODel \n
		Snippet: value: enums.FilterTestModels = driver.source.bb.nr5G.setting.tmodel.filterPy.get_tmodel() \n
		Applies a test model filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:return: filter_test_model: ALL| TM1_1| TM1_2| TM2| TM2a| TM3_1| TM3_1A| TM3_2| TM3_3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:TMODel?')
		return Conversions.str_to_scalar_enum(response, enums.FilterTestModels)

	def set_tmodel(self, filter_test_model: enums.FilterTestModels) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:TMODel \n
		Snippet: driver.source.bb.nr5G.setting.tmodel.filterPy.set_tmodel(filter_test_model = enums.FilterTestModels.ALL) \n
		Applies a test model filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:param filter_test_model: ALL| TM1_1| TM1_2| TM2| TM2a| TM3_1| TM3_1A| TM3_2| TM3_3
		"""
		param = Conversions.enum_scalar_to_str(filter_test_model, enums.FilterTestModels)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:TMODel {param}')

	# noinspection PyTypeChecker
	def get_tm_standard(self) -> enums.TestModelType:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:TMSTandard \n
		Snippet: value: enums.TestModelType = driver.source.bb.nr5G.setting.tmodel.filterPy.get_tm_standard() \n
		Applies a standard filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:return: test_model_stand: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:TMSTandard?')
		return Conversions.str_to_scalar_enum(response, enums.TestModelType)

	def set_tm_standard(self, test_model_stand: enums.TestModelType) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:TMODel:FILTer:TMSTandard \n
		Snippet: driver.source.bb.nr5G.setting.tmodel.filterPy.set_tm_standard(test_model_stand = enums.TestModelType.NR) \n
		Applies a standard filter to narrow down the files returned by the query
		[:SOURce<hw>]:BB:NR5G:SETTing:TMODel:FILTer:CATalog. \n
			:param test_model_stand: NR 3GPP test models. ORAN ORAN test cases.
		"""
		param = Conversions.enum_scalar_to_str(test_model_stand, enums.TestModelType)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:TMODel:FILTer:TMSTandard {param}')
