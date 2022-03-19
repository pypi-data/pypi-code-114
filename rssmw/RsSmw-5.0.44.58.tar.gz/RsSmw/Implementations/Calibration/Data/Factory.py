from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factory:
	"""Factory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factory", core, parent)

	def get_date(self) -> str:
		"""SCPI: CALibration:DATA:FACTory:DATE \n
		Snippet: value: str = driver.calibration.data.factory.get_date() \n
		Queries the date of the last factory calibration. \n
			:return: date: string
		"""
		response = self._core.io.query_str('CALibration:DATA:FACTory:DATE?')
		return trim_str_response(response)
