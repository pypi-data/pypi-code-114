from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mapping:
	"""Mapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mapping", core, parent)

	def get_file(self) -> str:
		"""SCPI: INSTruments:MAPPing:FILE \n
		Snippet: value: str = driver.instruments.mapping.get_file() \n
		No command help available \n
			:return: file: No help available
		"""
		response = self._core.io.query_str('INSTruments:MAPPing:FILE?')
		return trim_str_response(response)

	def set_file(self, file: str) -> None:
		"""SCPI: INSTruments:MAPPing:FILE \n
		Snippet: driver.instruments.mapping.set_file(file = '1') \n
		No command help available \n
			:param file: No help available
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'INSTruments:MAPPing:FILE {param}')
