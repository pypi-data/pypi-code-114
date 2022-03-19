from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Next:
	"""Next commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("next", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:COPY:NEXT \n
		Snippet: driver.source.fsimulator.mimo.copy.next.set() \n
		Copies the matrix values of the current tap to the subsequent tap. If the current tap is the last tap, the command is
		discarded. See also [:SOURce<hw>]:FSIMulator:MIMO:COPY:ALL. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:COPY:NEXT')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:COPY:NEXT \n
		Snippet: driver.source.fsimulator.mimo.copy.next.set_with_opc() \n
		Copies the matrix values of the current tap to the subsequent tap. If the current tap is the last tap, the command is
		discarded. See also [:SOURce<hw>]:FSIMulator:MIMO:COPY:ALL. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:MIMO:COPY:NEXT', opc_timeout_ms)
