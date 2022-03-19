from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AgPreset:
	"""AgPreset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("agPreset", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:AGPReset \n
		Snippet: driver.source.bb.stereo.grps.agPreset.set() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:AGPReset')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:AGPReset \n
		Snippet: driver.source.bb.stereo.grps.agPreset.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:STEReo:GRPS:AGPReset', opc_timeout_ms)
