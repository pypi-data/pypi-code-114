from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmodel:
	"""Tmodel commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmodel", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:SETTing:TMODel:CATalog \n
		Snippet: value: List[str] = driver.source.bb.tdscdma.setting.tmodel.get_catalog() \n
		Queries the file with the test models defined in the TD-SCDMA standard or a self-defined test setup. \n
			:return: catalog: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:SETTing:TMODel:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:SETTing:TMODel \n
		Snippet: value: str = driver.source.bb.tdscdma.setting.tmodel.get_value() \n
		Selects the file with the test models defined in the TD-SCDMA standard or a self-defined test setup. \n
			:return: tmodel: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:SETTing:TMODel?')
		return trim_str_response(response)

	def set_value(self, tmodel: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:SETTing:TMODel \n
		Snippet: driver.source.bb.tdscdma.setting.tmodel.set_value(tmodel = '1') \n
		Selects the file with the test models defined in the TD-SCDMA standard or a self-defined test setup. \n
			:param tmodel: string
		"""
		param = Conversions.value_to_quoted_str(tmodel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:SETTing:TMODel {param}')
