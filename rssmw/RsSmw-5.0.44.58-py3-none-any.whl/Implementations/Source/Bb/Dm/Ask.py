from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ask:
	"""Ask commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ask", core, parent)

	def get_depth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:ASK:DEPTh \n
		Snippet: value: float = driver.source.bb.dm.ask.get_depth() \n
		Sets the ASK modulation depth for modulation type ASK. \n
			:return: depth: float Range: 0 to 100, Unit: PCT
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:ASK:DEPTh?')
		return Conversions.str_to_float(response)

	def set_depth(self, depth: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:ASK:DEPTh \n
		Snippet: driver.source.bb.dm.ask.set_depth(depth = 1.0) \n
		Sets the ASK modulation depth for modulation type ASK. \n
			:param depth: float Range: 0 to 100, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(depth)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:ASK:DEPTh {param}')
