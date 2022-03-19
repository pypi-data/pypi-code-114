from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HddStreaming:
	"""HddStreaming commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hddStreaming", core, parent)

	def get_blevel(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA:HDDStreaming:BLEVel \n
		Snippet: value: float = driver.source.bb.sirius.data.hddStreaming.get_blevel() \n
		No command help available \n
			:return: blevel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:DATA:HDDStreaming:BLEVel?')
		return Conversions.str_to_float(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA:HDDStreaming:STATe \n
		Snippet: value: bool = driver.source.bb.sirius.data.hddStreaming.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:DATA:HDDStreaming:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA:HDDStreaming:STATe \n
		Snippet: driver.source.bb.sirius.data.hddStreaming.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:DATA:HDDStreaming:STATe {param}')
