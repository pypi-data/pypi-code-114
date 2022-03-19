from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pramp:
	"""Pramp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pramp", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:PRAMp:STATe \n
		Snippet: value: bool = driver.source.bb.esequencer.pramp.get_state() \n
		If activated, a maker signal created internally is used to control the RF pulse modulator. This leads to a better ON/OFF
		ratio. \n
			:return: rf_pow_ramp_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:PRAMp:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, rf_pow_ramp_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:PRAMp:STATe \n
		Snippet: driver.source.bb.esequencer.pramp.set_state(rf_pow_ramp_state = False) \n
		If activated, a maker signal created internally is used to control the RF pulse modulator. This leads to a better ON/OFF
		ratio. \n
			:param rf_pow_ramp_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(rf_pow_ramp_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:PRAMp:STATe {param}')
