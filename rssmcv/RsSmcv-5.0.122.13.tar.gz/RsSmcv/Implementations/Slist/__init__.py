from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slist:
	"""Slist commands group definition. 9 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slist", core, parent)

	@property
	def clear(self):
		"""clear commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_clear'):
			from .Clear import Clear
			self._clear = Clear(self._core, self._cmd_group)
		return self._clear

	@property
	def element(self):
		"""element commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_element'):
			from .Element import Element
			self._element = Element(self._core, self._cmd_group)
		return self._element

	@property
	def scan(self):
		"""scan commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_scan'):
			from .Scan import Scan
			self._scan = Scan(self._core, self._cmd_group)
		return self._scan

	@property
	def sensor(self):
		"""sensor commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sensor'):
			from .Sensor import Sensor
			self._sensor = Sensor(self._core, self._cmd_group)
		return self._sensor

	def clear_all(self) -> None:
		"""SCPI: SLISt:CLEar:[ALL] \n
		Snippet: driver.slist.clear_all() \n
		Removes all R&S NRP power sensors from the list. \n
		"""
		self._core.io.write(f'SLISt:CLEar:ALL')

	def clear_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SLISt:CLEar:[ALL] \n
		Snippet: driver.slist.clear_all_with_opc() \n
		Removes all R&S NRP power sensors from the list. \n
		Same as clear_all, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SLISt:CLEar:ALL', opc_timeout_ms)

	def get_list_py(self) -> List[str]:
		"""SCPI: SLISt:[LIST] \n
		Snippet: value: List[str] = driver.slist.get_list_py() \n
		Returns a list of all detected sensors in a comma-separated string. \n
			:return: sensor_list: String of comma-separated entries Each entry contains information on the sensor type, serial number and interface. The order of the entries does not correspond to the order the sensors are displayed in the 'NRP Sensor Mapping' dialog.
		"""
		response = self._core.io.query_str('SLISt:LIST?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Slist':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Slist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
