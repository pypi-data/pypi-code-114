from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModPreset:
	"""ModPreset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modPreset", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:MODPreset \n
		Snippet: driver.source.bb.ofdm.modPreset.set() \n
		Calls the default settings for the selected moduilation type, see [:SOURce<hw>]:BB:OFDM:MODulation. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:MODPreset')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:MODPreset \n
		Snippet: driver.source.bb.ofdm.modPreset.set_with_opc() \n
		Calls the default settings for the selected moduilation type, see [:SOURce<hw>]:BB:OFDM:MODulation. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:OFDM:MODPreset', opc_timeout_ms)
