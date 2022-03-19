from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Counters:
	"""Counters commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("counters", core, parent)

	def reset(self) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:DIAGnostic:COUNters:RESet \n
		Snippet: driver.system.communicate.bb.qsfp.network.diagnostic.counters.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:DIAGnostic:COUNters:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:DIAGnostic:COUNters:RESet \n
		Snippet: driver.system.communicate.bb.qsfp.network.diagnostic.counters.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:DIAGnostic:COUNters:RESet', opc_timeout_ms)

	def get_value(self) -> List[float]:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:DIAGnostic:COUNters \n
		Snippet: value: List[float] = driver.system.communicate.bb.qsfp.network.diagnostic.counters.get_value() \n
		No command help available \n
			:return: hs_net_statistics: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:DIAGnostic:COUNters?')
		return response
