from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamble:
	"""Preamble commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preamble", core, parent)

	def get_structure(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:PREamble:[STRucture] \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.bootstrap.preamble.get_structure() \n
		Queries the structure of the preamble symbols following the last bootstrap symbol. \n
			:return: pre_structure: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:PREamble:STRucture?')
		return Conversions.str_to_int(response)
