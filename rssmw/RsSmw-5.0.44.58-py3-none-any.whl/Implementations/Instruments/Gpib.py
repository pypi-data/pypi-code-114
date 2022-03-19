from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gpib:
	"""Gpib commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gpib", core, parent)

	def get_address(self) -> List[int]:
		"""SCPI: INSTruments:GPIB:ADDRess \n
		Snippet: value: List[int] = driver.instruments.gpib.get_address() \n
		No command help available \n
			:return: serial: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('INSTruments:GPIB:ADDRess?')
		return response

	def set_address(self, serial: List[int]) -> None:
		"""SCPI: INSTruments:GPIB:ADDRess \n
		Snippet: driver.instruments.gpib.set_address(serial = [1, 2, 3]) \n
		No command help available \n
			:param serial: No help available
		"""
		param = Conversions.list_to_csv_str(serial)
		self._core.io.write(f'INSTruments:GPIB:ADDRess {param}')

	def get_board(self) -> List[int]:
		"""SCPI: INSTruments:GPIB:BOARd \n
		Snippet: value: List[int] = driver.instruments.gpib.get_board() \n
		No command help available \n
			:return: board: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('INSTruments:GPIB:BOARd?')
		return response

	def set_board(self, board: List[int]) -> None:
		"""SCPI: INSTruments:GPIB:BOARd \n
		Snippet: driver.instruments.gpib.set_board(board = [1, 2, 3]) \n
		No command help available \n
			:param board: No help available
		"""
		param = Conversions.list_to_csv_str(board)
		self._core.io.write(f'INSTruments:GPIB:BOARd {param}')
