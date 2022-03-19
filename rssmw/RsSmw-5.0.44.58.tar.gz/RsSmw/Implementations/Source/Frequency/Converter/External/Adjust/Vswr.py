from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vswr:
	"""Vswr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vswr", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:ADJust:VSWR:STATe \n
		Snippet: value: bool = driver.source.frequency.converter.external.adjust.vswr.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:ADJust:VSWR:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:ADJust:VSWR:STATe \n
		Snippet: driver.source.frequency.converter.external.adjust.vswr.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:ADJust:VSWR:STATe {param}')
