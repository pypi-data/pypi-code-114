from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L5Band:
	"""L5Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l5Band", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:L5Band:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.l5Band.get_state() \n
		Activates the RF band. \n
			:return: l_5_band_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:L5Band:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, l_5_band_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:L5Band:[STATe] \n
		Snippet: driver.source.bb.gnss.l5Band.set_state(l_5_band_state = False) \n
		Activates the RF band. \n
			:param l_5_band_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(l_5_band_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:L5Band:STATe {param}')
