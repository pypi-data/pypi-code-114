from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L1Band:
	"""L1Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l1Band", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:L1Band:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.l1Band.get_state() \n
		Activates the RF band. \n
			:return: l_1_band_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:L1Band:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, l_1_band_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:L1Band:[STATe] \n
		Snippet: driver.source.bb.gnss.l1Band.set_state(l_1_band_state = False) \n
		Activates the RF band. \n
			:param l_1_band_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(l_1_band_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:L1Band:STATe {param}')
