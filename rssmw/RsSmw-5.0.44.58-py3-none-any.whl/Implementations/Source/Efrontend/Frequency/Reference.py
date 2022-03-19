from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def get_list_py(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:EFRontend:FREQuency:REFerence:LIST \n
		Snippet: value: List[str] = driver.source.efrontend.frequency.reference.get_list_py() \n
		Queries reference frequencies of connected RF frontends in a comma-separated list. \n
			:return: freq_conv_fe_ref_cat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:FREQuency:REFerence:LIST?')
		return Conversions.str_to_str_list(response)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.FeRefFreq:
		"""SCPI: [SOURce<HW>]:EFRontend:FREQuency:REFerence \n
		Snippet: value: enums.FeRefFreq = driver.source.efrontend.frequency.reference.get_value() \n
		Sets the reference frequency, that is used for RF frequency conversion at the connected external frontend. \n
			:return: fe_ref_freq: FG64| F1G| F10M FG64 640 MHz F1G 1 GHz F10M 10 MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:FREQuency:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.FeRefFreq)

	def set_value(self, fe_ref_freq: enums.FeRefFreq) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:FREQuency:REFerence \n
		Snippet: driver.source.efrontend.frequency.reference.set_value(fe_ref_freq = enums.FeRefFreq.F10M) \n
		Sets the reference frequency, that is used for RF frequency conversion at the connected external frontend. \n
			:param fe_ref_freq: FG64| F1G| F10M FG64 640 MHz F1G 1 GHz F10M 10 MHz
		"""
		param = Conversions.enum_scalar_to_str(fe_ref_freq, enums.FeRefFreq)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:FREQuency:REFerence {param}')
