from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Selftest:
	"""Selftest commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selftest", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:SELFtest \n
		Snippet: driver.source.efrontend.selftest.set() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:SELFtest')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:SELFtest \n
		Snippet: driver.source.efrontend.selftest.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:EFRontend:SELFtest', opc_timeout_ms)

	def get_result(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:SELFtest:RESult \n
		Snippet: value: str = driver.source.efrontend.selftest.get_result() \n
		No command help available \n
			:return: fe_selftest_res: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:SELFtest:RESult?')
		return trim_str_response(response)
