from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NonePy:
	"""NonePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nonePy", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:SELect:NONE \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.select.nonePy.set() \n
		Enables or disables all of the available SV IDs. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:SELect:NONE')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:SELect:NONE \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.select.nonePy.set_with_opc() \n
		Enables or disables all of the available SV IDs. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:SELect:NONE', opc_timeout_ms)
