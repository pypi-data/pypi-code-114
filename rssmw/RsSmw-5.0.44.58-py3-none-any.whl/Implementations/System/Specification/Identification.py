from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Identification:
	"""Identification commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("identification", core, parent)

	def get_catalog(self) -> str:
		"""SCPI: SYSTem:SPECification:IDENtification:CATalog \n
		Snippet: value: str = driver.system.specification.identification.get_catalog() \n
		Queries the parameter identifiers (<Id>) available in the data sheet. \n
			:return: id_list: string Comma-separated string of the parameter identifiers (Id)
		"""
		response = self._core.io.query_str('SYSTem:SPECification:IDENtification:CATalog?')
		return trim_str_response(response)
