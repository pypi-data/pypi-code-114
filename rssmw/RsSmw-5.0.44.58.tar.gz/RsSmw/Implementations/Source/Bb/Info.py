from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	def get_psequencer(self) -> str:
		"""SCPI: [SOURce]:BB:INFO:PSEQuencer \n
		Snippet: value: str = driver.source.bb.info.get_psequencer() \n
		No command help available \n
			:return: info_xml_string: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:INFO:PSEQuencer?')
		return trim_str_response(response)
