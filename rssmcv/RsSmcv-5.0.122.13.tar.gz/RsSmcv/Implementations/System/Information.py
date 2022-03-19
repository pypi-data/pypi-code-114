from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Information:
	"""Information commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("information", core, parent)

	def get_sr(self) -> str:
		"""SCPI: SYSTem:INFormation:SR \n
		Snippet: value: str = driver.system.information.get_sr() \n
		No command help available \n
			:return: sr_info: No help available
		"""
		response = self._core.io.query_str('SYSTem:INFormation:SR?')
		return trim_str_response(response)

	def set_sr(self, sr_info: str) -> None:
		"""SCPI: SYSTem:INFormation:SR \n
		Snippet: driver.system.information.set_sr(sr_info = '1') \n
		No command help available \n
			:param sr_info: No help available
		"""
		param = Conversions.value_to_quoted_str(sr_info)
		self._core.io.write(f'SYSTem:INFormation:SR {param}')
