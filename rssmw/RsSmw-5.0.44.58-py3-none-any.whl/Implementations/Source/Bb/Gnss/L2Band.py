from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L2Band:
	"""L2Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l2Band", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:L2Band:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.l2Band.get_state() \n
		Activates the RF band. \n
			:return: l_2_band_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:L2Band:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, l_2_band_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:L2Band:[STATe] \n
		Snippet: driver.source.bb.gnss.l2Band.set_state(l_2_band_state = False) \n
		Activates the RF band. \n
			:param l_2_band_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(l_2_band_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:L2Band:STATe {param}')
