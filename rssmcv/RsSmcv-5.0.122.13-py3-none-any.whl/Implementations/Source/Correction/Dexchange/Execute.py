from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:EXECute \n
		Snippet: driver.source.correction.dexchange.execute.set() \n
		Executes the import or export of the selected correction list, according to the previously set transfer direction with
		command [:SOURce<hw>]:CORRection:DEXChange:MODE. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:CORRection:DEXChange:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:EXECute \n
		Snippet: driver.source.correction.dexchange.execute.set_with_opc() \n
		Executes the import or export of the selected correction list, according to the previously set transfer direction with
		command [:SOURce<hw>]:CORRection:DEXChange:MODE. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:DEXChange:EXECute', opc_timeout_ms)
