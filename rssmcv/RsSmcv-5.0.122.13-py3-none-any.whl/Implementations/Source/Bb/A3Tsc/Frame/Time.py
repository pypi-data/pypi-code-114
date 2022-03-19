from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def get_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:TIME:[OFFSet] \n
		Snippet: value: int = driver.source.bb.a3Tsc.frame.time.get_offset() \n
		Queries the number of sample periods between the nearest preceding or coincident millisecond boundary and the leading
		edge of the frame. \n
			:return: time_offset: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:FRAMe:TIME:OFFSet?')
		return Conversions.str_to_int(response)
