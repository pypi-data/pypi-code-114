from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:EXECute \n
		Snippet: driver.source.bb.c2K.copy.execute.set() \n
		The command starts the copy process. The dataset of the source station is copied to the destination station. Whether the
		data is copied to a base station or a mobile station depends on which transmission direction is selected (command
		BB:C2K:LINK UP | DOWN) . \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:COPY:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:EXECute \n
		Snippet: driver.source.bb.c2K.copy.execute.set_with_opc() \n
		The command starts the copy process. The dataset of the source station is copied to the destination station. Whether the
		data is copied to a base station or a mobile station depends on which transmission direction is selected (command
		BB:C2K:LINK UP | DOWN) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:C2K:COPY:EXECute', opc_timeout_ms)
