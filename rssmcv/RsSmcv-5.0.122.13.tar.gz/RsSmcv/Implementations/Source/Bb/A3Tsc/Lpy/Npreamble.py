from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npreamble:
	"""Npreamble commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npreamble", core, parent)

	def get_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:NPReamble:[SYMBols] \n
		Snippet: value: int = driver.source.bb.a3Tsc.lpy.npreamble.get_symbols() \n
		Queries the total number of OFDM symbols contained in the preamble. \n
			:return: num_pre_symb: integer Range: 1 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:L:NPReamble:SYMBols?')
		return Conversions.str_to_int(response)
