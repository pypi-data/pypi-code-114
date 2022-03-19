from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Used:
	"""Used commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("used", core, parent)

	def get_bandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBT:USED:[BANDwidth] \n
		Snippet: value: float = driver.source.bb.dvbt.used.get_bandwidth() \n
		Defines the used bandwidth. \n
			:return: used_bw: float Range: 1000000 to 10000000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:USED:BANDwidth?')
		return Conversions.str_to_float(response)

	def set_bandwidth(self, used_bw: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:USED:[BANDwidth] \n
		Snippet: driver.source.bb.dvbt.used.set_bandwidth(used_bw = 1.0) \n
		Defines the used bandwidth. \n
			:param used_bw: float Range: 1000000 to 10000000
		"""
		param = Conversions.decimal_value_to_str(used_bw)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:USED:BANDwidth {param}')
