from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apply:
	"""Apply commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apply", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:NOTCh:APPLy \n
		Snippet: driver.source.bb.dvb.notch.apply.set() \n
		Adopt the configured settings. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:NOTCh:APPLy')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:NOTCh:APPLy \n
		Snippet: driver.source.bb.dvb.notch.apply.set_with_opc() \n
		Adopt the configured settings. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DVB:NOTCh:APPLy', opc_timeout_ms)
