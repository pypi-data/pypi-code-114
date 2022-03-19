from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, board_id: List[str]) -> List[str]:
		"""SCPI: DIAGnostic<HW>:EEPRom:BIDentifier:CATalog \n
		Snippet: value: List[str] = driver.diagnostic.eeprom.bidentifier.catalog.get(board_id = ['1', '2', '3']) \n
		No command help available \n
			:param board_id: No help available
			:return: board_id: No help available"""
		param = Conversions.list_to_csv_quoted_str(board_id)
		response = self._core.io.query_str(f'DIAGnostic<HwInstance>:EEPRom:BIDentifier:CATalog? {param}')
		return Conversions.str_to_str_list(response)
