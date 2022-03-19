from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 9 total commands, 0 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	def get_cut_trans(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:CUTTrans \n
		Snippet: value: bool = driver.source.bb.ofdm.filterPy.get_cut_trans() \n
		Cuts the transient response of the filtering operation at the beginning and end of the signal. \n
			:return: cut_trans_resp: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:CUTTrans?')
		return Conversions.str_to_bool(response)

	def set_cut_trans(self, cut_trans_resp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:CUTTrans \n
		Snippet: driver.source.bb.ofdm.filterPy.set_cut_trans(cut_trans_resp = False) \n
		Cuts the transient response of the filtering operation at the beginning and end of the signal. \n
			:param cut_trans_resp: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(cut_trans_resp)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FILTer:CUTTrans {param}')

	def get_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:LENGth \n
		Snippet: value: int = driver.source.bb.ofdm.filterPy.get_length() \n
		Sets the filter length. \n
			:return: filter_length: integer Range: 1 to 800
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, filter_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:LENGth \n
		Snippet: driver.source.bb.ofdm.filterPy.set_length(filter_length = 1) \n
		Sets the filter length. \n
			:param filter_length: integer Range: 1 to 800
		"""
		param = Conversions.decimal_value_to_str(filter_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FILTer:LENGth {param}')

	def get_rolloff(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:ROLLoff \n
		Snippet: value: float = driver.source.bb.ofdm.filterPy.get_rolloff() \n
		Sets the filter parameter. \n
			:return: rolloff: float Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:ROLLoff?')
		return Conversions.str_to_float(response)

	def set_rolloff(self, rolloff: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:ROLLoff \n
		Snippet: driver.source.bb.ofdm.filterPy.set_rolloff(rolloff = 1.0) \n
		Sets the filter parameter. \n
			:param rolloff: float Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(rolloff)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FILTer:ROLLoff {param}')

	def get_sb_attenuation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:SBATtenuation \n
		Snippet: value: float = driver.source.bb.ofdm.filterPy.get_sb_attenuation() \n
		Sets the attenuation in the filter stop band. \n
			:return: stb_attenuation: float Range: 10 to 120
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:SBATtenuation?')
		return Conversions.str_to_float(response)

	def set_sb_attenuation(self, stb_attenuation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:SBATtenuation \n
		Snippet: driver.source.bb.ofdm.filterPy.set_sb_attenuation(stb_attenuation = 1.0) \n
		Sets the attenuation in the filter stop band. \n
			:param stb_attenuation: float Range: 10 to 120
		"""
		param = Conversions.decimal_value_to_str(stb_attenuation)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FILTer:SBATtenuation {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.C5GfiltT:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:TYPE \n
		Snippet: value: enums.C5GfiltT = driver.source.bb.ofdm.filterPy.get_type_py() \n
		Sets the baseband filter type. \n
			:return: filter_type: RC| RRC| DIRichlet| RECT| DCH| STRunc| USER| PHYDyas| NONE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.C5GfiltT)

	def set_type_py(self, filter_type: enums.C5GfiltT) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:TYPE \n
		Snippet: driver.source.bb.ofdm.filterPy.set_type_py(filter_type = enums.C5GfiltT.DCH) \n
		Sets the baseband filter type. \n
			:param filter_type: RC| RRC| DIRichlet| RECT| DCH| STRunc| USER| PHYDyas| NONE
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.C5GfiltT)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FILTer:TYPE {param}')

	def get_ucatalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:UCATalog \n
		Snippet: value: List[str] = driver.source.bb.ofdm.filterPy.get_ucatalog() \n
		Queries the user filetr files in the default directory. Only files with the file extension *.dat are listed. \n
			:return: c_5_gfilter_cat_name: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:UCATalog?')
		return Conversions.str_to_str_list(response)

	def get_ulength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:ULENgth \n
		Snippet: value: int = driver.source.bb.ofdm.filterPy.get_ulength() \n
		Queries the filter length. \n
			:return: user_filter_len: integer Range: 1 to 800
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:ULENgth?')
		return Conversions.str_to_int(response)

	def get_uselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:USELection \n
		Snippet: value: str = driver.source.bb.ofdm.filterPy.get_uselection() \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.dat.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: user_sel: string complete file path incl file name and file extenssion
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:USELection?')
		return trim_str_response(response)

	def set_uselection(self, user_sel: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:USELection \n
		Snippet: driver.source.bb.ofdm.filterPy.set_uselection(user_sel = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.dat.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param user_sel: string complete file path incl file name and file extenssion
		"""
		param = Conversions.value_to_quoted_str(user_sel)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FILTer:USELection {param}')

	# noinspection PyTypeChecker
	def get_windowing(self) -> enums.C5GfilterWind:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:WINDowing \n
		Snippet: value: enums.C5GfilterWind = driver.source.bb.ofdm.filterPy.get_windowing() \n
		Sets the windowing method. \n
			:return: windowing: NONE| HANNing| HAMMing
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FILTer:WINDowing?')
		return Conversions.str_to_scalar_enum(response, enums.C5GfilterWind)

	def set_windowing(self, windowing: enums.C5GfilterWind) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FILTer:WINDowing \n
		Snippet: driver.source.bb.ofdm.filterPy.set_windowing(windowing = enums.C5GfilterWind.HAMMing) \n
		Sets the windowing method. \n
			:param windowing: NONE| HANNing| HAMMing
		"""
		param = Conversions.enum_scalar_to_str(windowing, enums.C5GfilterWind)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FILTer:WINDowing {param}')
