from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmod:
	"""Tmod commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmod", core, parent)

	def get_downlink(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:SETTing:TMOD:DL \n
		Snippet: value: str = driver.source.bb.eutra.setting.tmod.get_downlink() \n
		Selects a predefined test model as defined in . \n
			:return: filename: test_model_name
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:SETTing:TMOD:DL?')
		return trim_str_response(response)

	def set_downlink(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:SETTing:TMOD:DL \n
		Snippet: driver.source.bb.eutra.setting.tmod.set_downlink(filename = '1') \n
		Selects a predefined test model as defined in . \n
			:param filename: test_model_name
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:SETTing:TMOD:DL {param}')

	def get_tdd(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:SETTing:TMOD:TDD \n
		Snippet: value: str = driver.source.bb.eutra.setting.tmod.get_tdd() \n
		Selects a predefined test model as defined in . \n
			:return: tdd: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:SETTing:TMOD:TDD?')
		return trim_str_response(response)

	def set_tdd(self, tdd: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:SETTing:TMOD:TDD \n
		Snippet: driver.source.bb.eutra.setting.tmod.set_tdd(tdd = '1') \n
		Selects a predefined test model as defined in . \n
			:param tdd: test_model_name
		"""
		param = Conversions.value_to_quoted_str(tdd)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:SETTing:TMOD:TDD {param}')
