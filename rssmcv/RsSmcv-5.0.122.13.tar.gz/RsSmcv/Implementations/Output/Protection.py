from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protection:
	"""Protection commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("protection", core, parent)

	def clear(self) -> None:
		"""SCPI: OUTPut<HW>:PROTection:CLEar \n
		Snippet: driver.output.protection.clear() \n
		Resets the protective circuit after it has been tripped. To define the output state, use the command method RsSmcv.Output.
		State.value. \n
		"""
		self._core.io.write(f'OUTPut<HwInstance>:PROTection:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: OUTPut<HW>:PROTection:CLEar \n
		Snippet: driver.output.protection.clear_with_opc() \n
		Resets the protective circuit after it has been tripped. To define the output state, use the command method RsSmcv.Output.
		State.value. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'OUTPut<HwInstance>:PROTection:CLEar', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: OUTPut<HW>:PROTection:STATe \n
		Snippet: value: bool = driver.output.protection.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('OUTPut<HwInstance>:PROTection:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: OUTPut<HW>:PROTection:STATe \n
		Snippet: driver.output.protection.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'OUTPut<HwInstance>:PROTection:STATe {param}')

	def get_tripped(self) -> bool:
		"""SCPI: OUTPut<HW>:PROTection:TRIPped \n
		Snippet: value: bool = driver.output.protection.get_tripped() \n
		Queries the state of the protective circuit. \n
			:return: tripped: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('OUTPut<HwInstance>:PROTection:TRIPped?')
		return Conversions.str_to_bool(response)
