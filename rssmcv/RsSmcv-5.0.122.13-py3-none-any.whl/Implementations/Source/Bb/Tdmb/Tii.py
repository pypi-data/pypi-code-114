from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tii:
	"""Tii commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tii", core, parent)

	def get_main(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:TII:MAIN \n
		Snippet: value: int = driver.source.bb.tdmb.tii.get_main() \n
		Defines the main ID. \n
			:return: tii_main: integer Range: 0 to 69
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:TII:MAIN?')
		return Conversions.str_to_int(response)

	def set_main(self, tii_main: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:TII:MAIN \n
		Snippet: driver.source.bb.tdmb.tii.set_main(tii_main = 1) \n
		Defines the main ID. \n
			:param tii_main: integer Range: 0 to 69
		"""
		param = Conversions.decimal_value_to_str(tii_main)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:TII:MAIN {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDMB:TII:STATe \n
		Snippet: value: bool = driver.source.bb.tdmb.tii.get_state() \n
		Enables/disables the transmission of the signal. \n
			:return: tii_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:TII:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, tii_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:TII:STATe \n
		Snippet: driver.source.bb.tdmb.tii.set_state(tii_state = False) \n
		Enables/disables the transmission of the signal. \n
			:param tii_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tii_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:TII:STATe {param}')

	def get_sub(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:TII:SUB \n
		Snippet: value: int = driver.source.bb.tdmb.tii.get_sub() \n
		Defines the sub ID. \n
			:return: tii_sub: integer Range: 1 to 23
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:TII:SUB?')
		return Conversions.str_to_int(response)

	def set_sub(self, tii_sub: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:TII:SUB \n
		Snippet: driver.source.bb.tdmb.tii.set_sub(tii_sub = 1) \n
		Defines the sub ID. \n
			:param tii_sub: integer Range: 1 to 23
		"""
		param = Conversions.decimal_value_to_str(tii_sub)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:TII:SUB {param}')
