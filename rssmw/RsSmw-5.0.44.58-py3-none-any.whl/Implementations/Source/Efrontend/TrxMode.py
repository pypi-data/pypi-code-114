from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrxMode:
	"""TrxMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trxMode", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:EFRontend:TRXMode:[STATe] \n
		Snippet: value: bool = driver.source.efrontend.trxMode.get_state() \n
		No command help available \n
			:return: rx_tx_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:TRXMode:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, rx_tx_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:TRXMode:[STATe] \n
		Snippet: driver.source.efrontend.trxMode.set_state(rx_tx_mode = False) \n
		No command help available \n
			:param rx_tx_mode: No help available
		"""
		param = Conversions.bool_to_str(rx_tx_mode)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:TRXMode:STATe {param}')
