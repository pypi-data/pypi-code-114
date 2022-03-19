from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OrgLayer:
	"""OrgLayer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("orgLayer", core, parent)

	def get(self, test_arg: str) -> str:
		"""SCPI: [SOURce]:FSIMulator:TEST:ORGLayer \n
		Snippet: value: str = driver.source.fsimulator.test.orgLayer.get(test_arg = '1') \n
		No command help available \n
			:param test_arg: No help available
			:return: test_answer: No help available"""
		param = Conversions.value_to_quoted_str(test_arg)
		response = self._core.io.query_str(f'SOURce:FSIMulator:TEST:ORGLayer? {param}')
		return trim_str_response(response)
