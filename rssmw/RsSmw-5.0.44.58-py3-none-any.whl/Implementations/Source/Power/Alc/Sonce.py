from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sonce:
	"""Sonce commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sonce", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ALC:SONCe \n
		Snippet: driver.source.power.alc.sonce.set() \n
		Activates level control for correction purposes temporarily. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:POWer:ALC:SONCe')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ALC:SONCe \n
		Snippet: driver.source.power.alc.sonce.set_with_opc() \n
		Activates level control for correction purposes temporarily. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:POWer:ALC:SONCe', opc_timeout_ms)
