from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlayFile:
	"""PlayFile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("playFile", core, parent)

	def get_length(self) -> int:
		"""SCPI: TSGen:READ:PLAYfile:LENGth \n
		Snippet: value: int = driver.tsGen.read.playFile.get_length() \n
		Queries calculated original loop time. \n
			:return: length: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('TSGen:READ:PLAYfile:LENGth?')
		return Conversions.str_to_int(response)
