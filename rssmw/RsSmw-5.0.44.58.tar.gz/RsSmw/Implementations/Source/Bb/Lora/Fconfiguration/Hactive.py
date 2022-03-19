from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hactive:
	"""Hactive commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hactive", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:HACTive:STATe \n
		Snippet: value: bool = driver.source.bb.lora.fconfiguration.hactive.get_state() \n
		Activates the header data in the frame. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:FCONfiguration:HACTive:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:HACTive:STATe \n
		Snippet: driver.source.bb.lora.fconfiguration.hactive.set_state(state = False) \n
		Activates the header data in the frame. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:FCONfiguration:HACTive:STATe {param}')
