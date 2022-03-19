from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Additional:
	"""Additional commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("additional", core, parent)

	def get_samples(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:ADDitional:[SAMPles] \n
		Snippet: value: int = driver.source.bb.a3Tsc.frame.additional.get_samples() \n
		Queries the number of additional samples added at the end of a frame to facilitate sampling clock alignment. \n
			:return: add_samples: integer Range: 0 to 127
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:FRAMe:ADDitional:SAMPles?')
		return Conversions.str_to_int(response)
