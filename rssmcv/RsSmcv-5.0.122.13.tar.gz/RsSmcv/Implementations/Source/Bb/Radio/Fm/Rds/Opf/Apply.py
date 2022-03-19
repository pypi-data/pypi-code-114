from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apply:
	"""Apply commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apply", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:APPLy \n
		Snippet: driver.source.bb.radio.fm.rds.opf.apply.set() \n
		Triggers transmission of open format data. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:APPLy')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:APPLy \n
		Snippet: driver.source.bb.radio.fm.rds.opf.apply.set_with_opc() \n
		Triggers transmission of open format data. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:APPLy', opc_timeout_ms)
