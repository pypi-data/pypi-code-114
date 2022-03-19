from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:EXECute \n
		Snippet: driver.source.bb.w3Gpp.pparameter.execute.set() \n
		This command presets the channel table of base station 1 with the parameters defined by the PPARameter commands. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:PPARameter:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:EXECute \n
		Snippet: driver.source.bb.w3Gpp.pparameter.execute.set_with_opc() \n
		This command presets the channel table of base station 1 with the parameters defined by the PPARameter commands. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:W3GPp:PPARameter:EXECute', opc_timeout_ms)
