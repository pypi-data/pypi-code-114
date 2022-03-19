from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sweep:
	"""Sweep commands group definition. 27 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sweep", core, parent)

	@property
	def combined(self):
		"""combined commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_combined'):
			from .Combined import Combined
			self._combined = Combined(self._core, self._cmd_group)
		return self._combined

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 7 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def reset_all(self) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:RESet:[ALL] \n
		Snippet: driver.source.sweep.reset_all() \n
		Resets all active sweeps to the starting point. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:SWEep:RESet:ALL')

	def reset_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:RESet:[ALL] \n
		Snippet: driver.source.sweep.reset_all_with_opc() \n
		Resets all active sweeps to the starting point. \n
		Same as reset_all, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:SWEep:RESet:ALL', opc_timeout_ms)

	def clone(self) -> 'Sweep':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sweep(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
