from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TdWind:
	"""TdWind commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdWind", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TDWind:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.tdWind.get_state() \n
		Enables time domain windowing. \n
			:return: td_window: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TDWind:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, td_window: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TDWind:STATe \n
		Snippet: driver.source.bb.nr5G.tdWind.set_state(td_window = False) \n
		Enables time domain windowing. \n
			:param td_window: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(td_window)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TDWind:STATe {param}')
