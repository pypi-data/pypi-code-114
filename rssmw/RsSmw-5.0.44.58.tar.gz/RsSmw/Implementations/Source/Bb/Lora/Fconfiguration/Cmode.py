from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmode:
	"""Cmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmode", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:CMODe:STATe \n
		Snippet: value: bool = driver.source.bb.lora.fconfiguration.cmode.get_state() \n
		Activates the compressed mode of the header data in the frame. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:FCONfiguration:CMODe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:CMODe:STATe \n
		Snippet: driver.source.bb.lora.fconfiguration.cmode.set_state(state = False) \n
		Activates the compressed mode of the header data in the frame. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:FCONfiguration:CMODe:STATe {param}')
