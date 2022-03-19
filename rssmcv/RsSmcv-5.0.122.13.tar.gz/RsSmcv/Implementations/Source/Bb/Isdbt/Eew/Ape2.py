from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ape2:
	"""Ape2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ape2", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:APE2 \n
		Snippet: driver.source.bb.isdbt.eew.ape2.set() \n
		Issues a seismic motion warning based on the settings for epicenter 2. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:APE2')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:APE2 \n
		Snippet: driver.source.bb.isdbt.eew.ape2.set_with_opc() \n
		Issues a seismic motion warning based on the settings for epicenter 2. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ISDBt:EEW:APE2', opc_timeout_ms)
