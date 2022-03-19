from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def reset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OSTReams:OUTPut:RESet \n
		Snippet: driver.source.bb.gnss.ostreams.output.reset() \n
		Resets the output stream configuration, where all outputs are disabled. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:OSTReams:OUTPut:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OSTReams:OUTPut:RESet \n
		Snippet: driver.source.bb.gnss.ostreams.output.reset_with_opc() \n
		Resets the output stream configuration, where all outputs are disabled. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:OSTReams:OUTPut:RESet', opc_timeout_ms)
