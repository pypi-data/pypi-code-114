from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generic:
	"""Generic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generic", core, parent)

	def get_msg(self) -> str:
		"""SCPI: SYSTem:GENeric:MSG \n
		Snippet: value: str = driver.system.generic.get_msg() \n
		No command help available \n
			:return: generic_message: No help available
		"""
		response = self._core.io.query_str('SYSTem:GENeric:MSG?')
		return trim_str_response(response)

	def set_msg(self, generic_message: str) -> None:
		"""SCPI: SYSTem:GENeric:MSG \n
		Snippet: driver.system.generic.set_msg(generic_message = '1') \n
		No command help available \n
			:param generic_message: No help available
		"""
		param = Conversions.value_to_quoted_str(generic_message)
		self._core.io.write(f'SYSTem:GENeric:MSG {param}')
