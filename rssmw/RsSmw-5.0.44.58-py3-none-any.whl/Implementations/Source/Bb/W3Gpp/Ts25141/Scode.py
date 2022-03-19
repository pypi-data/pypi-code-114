from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scode:
	"""Scode commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scode", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Ts25141ScrCodeMode:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:SCODe:MODE \n
		Snippet: value: enums.Ts25141ScrCodeMode = driver.source.bb.w3Gpp.ts25141.scode.get_mode() \n
		Sets the type for the scrambling code for the uplink direction. In downlink direction (test case 6.6) , the scrambling
		generator can be switched on and off. \n
			:return: mode: OFF| ON| LONG| SHORt
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:SCODe:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141ScrCodeMode)

	def set_mode(self, mode: enums.Ts25141ScrCodeMode) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:SCODe:MODE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.scode.set_mode(mode = enums.Ts25141ScrCodeMode.LONG) \n
		Sets the type for the scrambling code for the uplink direction. In downlink direction (test case 6.6) , the scrambling
		generator can be switched on and off. \n
			:param mode: OFF| ON| LONG| SHORt
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Ts25141ScrCodeMode)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:SCODe:MODE {param}')

	def get_value(self) -> List[str]:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:SCODe \n
		Snippet: value: List[str] = driver.source.bb.w3Gpp.ts25141.scode.get_value() \n
		Sets the scrambling code. The value range depends on whether the generator is used in uplink or downlink direction (test
		case 6.6) according to the selected test case. \n
			:return: scode: integer
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:SCODe?')
		return Conversions.str_to_str_list(response)

	def set_value(self, scode: List[str]) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:SCODe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.scode.set_value(scode = ['raw1', 'raw2', 'raw3']) \n
		Sets the scrambling code. The value range depends on whether the generator is used in uplink or downlink direction (test
		case 6.6) according to the selected test case. \n
			:param scode: integer
		"""
		param = Conversions.list_to_csv_str(scode)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:SCODe {param}')
