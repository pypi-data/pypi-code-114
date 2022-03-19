from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Remote:
	"""Remote commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("remote", core, parent)

	def get_channel(self) -> List[int]:
		"""SCPI: INSTruments:REMote:CHANnel \n
		Snippet: value: List[int] = driver.instruments.remote.get_channel() \n
		No command help available \n
			:return: channel: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('INSTruments:REMote:CHANnel?')
		return response

	def set_channel(self, channel: List[int]) -> None:
		"""SCPI: INSTruments:REMote:CHANnel \n
		Snippet: driver.instruments.remote.set_channel(channel = [1, 2, 3]) \n
		No command help available \n
			:param channel: No help available
		"""
		param = Conversions.list_to_csv_str(channel)
		self._core.io.write(f'INSTruments:REMote:CHANnel {param}')

	def get_name(self) -> List[str]:
		"""SCPI: INSTruments:REMote:NAME \n
		Snippet: value: List[str] = driver.instruments.remote.get_name() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('INSTruments:REMote:NAME?')
		return Conversions.str_to_str_list(response)

	def set_name(self, name: List[str]) -> None:
		"""SCPI: INSTruments:REMote:NAME \n
		Snippet: driver.instruments.remote.set_name(name = ['1', '2', '3']) \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.list_to_csv_quoted_str(name)
		self._core.io.write(f'INSTruments:REMote:NAME {param}')
