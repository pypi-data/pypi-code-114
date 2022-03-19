from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Group:
	"""Group commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)

	def get_sequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:GROup:SEQuence \n
		Snippet: value: str = driver.source.bb.radio.fm.rds.group.get_sequence() \n
		No command help available \n
			:return: group_sequence: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:GROup:SEQuence?')
		return trim_str_response(response)

	def set_sequence(self, group_sequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:GROup:SEQuence \n
		Snippet: driver.source.bb.radio.fm.rds.group.set_sequence(group_sequence = '1') \n
		No command help available \n
			:param group_sequence: string
		"""
		param = Conversions.value_to_quoted_str(group_sequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:GROup:SEQuence {param}')
