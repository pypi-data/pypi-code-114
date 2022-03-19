from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:LOSCillator:INPut:FREQuency \n
		Snippet: value: float = driver.source.frequency.loscillator.inputPy.get_frequency() \n
		Queries the required external reference frequency. \n
			:return: frequency: float Range: 100E3 to 20E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:LOSCillator:INPut:FREQuency?')
		return Conversions.str_to_float(response)
