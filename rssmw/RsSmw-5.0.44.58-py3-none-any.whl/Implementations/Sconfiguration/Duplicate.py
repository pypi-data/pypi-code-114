from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duplicate:
	"""Duplicate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duplicate", core, parent)

	def get_stream(self) -> bool:
		"""SCPI: SCONfiguration:DUPLicate:[STReam] \n
		Snippet: value: bool = driver.sconfiguration.duplicate.get_stream() \n
		In a 3x1x1 or 4x1x1 configuration, creates a copy of each stream. Generates are a total number of 6 or 8 streams, where 4
		of them can be signals with real-time data source. \n
			:return: duplicate_stream: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SCONfiguration:DUPLicate:STReam?')
		return Conversions.str_to_bool(response)

	def set_stream(self, duplicate_stream: bool) -> None:
		"""SCPI: SCONfiguration:DUPLicate:[STReam] \n
		Snippet: driver.sconfiguration.duplicate.set_stream(duplicate_stream = False) \n
		In a 3x1x1 or 4x1x1 configuration, creates a copy of each stream. Generates are a total number of 6 or 8 streams, where 4
		of them can be signals with real-time data source. \n
			:param duplicate_stream: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(duplicate_stream)
		self._core.io.write(f'SCONfiguration:DUPLicate:STReam {param}')
