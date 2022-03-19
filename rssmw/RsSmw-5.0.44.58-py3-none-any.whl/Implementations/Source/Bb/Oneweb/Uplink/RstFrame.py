from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RstFrame:
	"""RstFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rstFrame", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:RSTFrame \n
		Snippet: driver.source.bb.oneweb.uplink.rstFrame.set() \n
		Resets all subframe settings of the selected link direction to the default values. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:RSTFrame')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:RSTFrame \n
		Snippet: driver.source.bb.oneweb.uplink.rstFrame.set_with_opc() \n
		Resets all subframe settings of the selected link direction to the default values. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ONEWeb:UL:RSTFrame', opc_timeout_ms)
