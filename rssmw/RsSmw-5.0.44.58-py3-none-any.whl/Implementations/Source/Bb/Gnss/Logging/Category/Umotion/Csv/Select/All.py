from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:SELect:ALL \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.select.all.set() \n
		Enables or disables all of the available SV IDs. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:SELect:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:SELect:ALL \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.select.all.set_with_opc() \n
		Enables or disables all of the available SV IDs. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:SELect:ALL', opc_timeout_ms)
