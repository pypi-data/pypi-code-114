from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frame:
	"""Frame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)

	def get_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:FRAMe:DURation \n
		Snippet: value: float = driver.source.bb.a3Tsc.info.frame.get_duration() \n
		Queries the frame duration in ms. \n
			:return: duration: float Range: 0 to 9999.999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:FRAMe:DURation?')
		return Conversions.str_to_float(response)
