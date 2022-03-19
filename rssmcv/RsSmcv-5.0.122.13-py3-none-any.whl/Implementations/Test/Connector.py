from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def get_aux_io(self) -> bool:
		"""SCPI: TEST:CONNector:AUXio \n
		Snippet: value: bool = driver.test.connector.get_aux_io() \n
		No command help available \n
			:return: aux_io: No help available
		"""
		response = self._core.io.query_str('TEST:CONNector:AUXio?')
		return Conversions.str_to_bool(response)

	def get_bnc(self) -> bool:
		"""SCPI: TEST:CONNector:BNC \n
		Snippet: value: bool = driver.test.connector.get_bnc() \n
		No command help available \n
			:return: bnc: No help available
		"""
		response = self._core.io.query_str('TEST:CONNector:BNC?')
		return Conversions.str_to_bool(response)
