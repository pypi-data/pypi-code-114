from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apply:
	"""Apply commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apply", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:LEVel:APPLy \n
		Snippet: driver.source.regenerator.simulation.level.apply.set() \n
		Sets the output level at the dedicated connector to the calculated level. To query the calculated level, use the command
		[:SOURce<hw>]:REGenerator:SIMulation:LEVel?. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:LEVel:APPLy')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:LEVel:APPLy \n
		Snippet: driver.source.regenerator.simulation.level.apply.set_with_opc() \n
		Sets the output level at the dedicated connector to the calculated level. To query the calculated level, use the command
		[:SOURce<hw>]:REGenerator:SIMulation:LEVel?. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:REGenerator:SIMulation:LEVel:APPLy', opc_timeout_ms)
