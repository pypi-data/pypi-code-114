from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Burst:
	"""Burst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)

	def get_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:[BURSt]:DURation \n
		Snippet: value: float = driver.source.noise.impulsive.burst.get_duration() \n
		Queries the time during which the noise generator is active in a frame. \n
			:return: ipls_burst_duration: float Range: 0.01E-6 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:IMPulsive:BURSt:DURation?')
		return Conversions.str_to_float(response)
