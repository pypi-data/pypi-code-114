from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Discard:
	"""Discard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("discard", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:DISCard \n
		Snippet: driver.source.bb.nr5G.qckset.discard.set() \n
		Ignores the configuration. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:DISCard')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:DISCard \n
		Snippet: driver.source.bb.nr5G.qckset.discard.set_with_opc() \n
		Ignores the configuration. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:NR5G:QCKSet:DISCard', opc_timeout_ms)
