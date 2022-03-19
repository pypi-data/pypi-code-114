from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mac:
	"""Mac commands group definition. 25 total commands, 5 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mac", core, parent)

	@property
	def address(self):
		"""address commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_address'):
			from .Address import Address
			self._address = Address(self._core, self._cmd_group)
		return self._address

	@property
	def fcontrol(self):
		"""fcontrol commands group. 0 Sub-classes, 13 commands."""
		if not hasattr(self, '_fcontrol'):
			from .Fcontrol import Fcontrol
			self._fcontrol = Fcontrol(self._core, self._cmd_group)
		return self._fcontrol

	@property
	def fcs(self):
		"""fcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fcs'):
			from .Fcs import Fcs
			self._fcs = Fcs(self._core, self._cmd_group)
		return self._fcs

	@property
	def qsControl(self):
		"""qsControl commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_qsControl'):
			from .QsControl import QsControl
			self._qsControl = QsControl(self._core, self._cmd_group)
		return self._qsControl

	@property
	def scontrol(self):
		"""scontrol commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_scontrol'):
			from .Scontrol import Scontrol
			self._scontrol = Scontrol(self._core, self._cmd_group)
		return self._scontrol

	def get_did(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:DID \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.get_did() \n
		Sets the value of the duration ID field. Depending on the frame type, the 2-byte field Duration/ID is used to transmit
		the association identity of the station transmitting the frame or it indicates the duration assigned to the frame type.
		Exactly 16 bit must be entered. \n
			:return: did: 16 bits
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:DID?')
		return Conversions.str_to_str_list(response)

	def set_did(self, did: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:DID \n
		Snippet: driver.source.bb.wlad.pconfig.mac.set_did(did = ['raw1', 'raw2', 'raw3']) \n
		Sets the value of the duration ID field. Depending on the frame type, the 2-byte field Duration/ID is used to transmit
		the association identity of the station transmitting the frame or it indicates the duration assigned to the frame type.
		Exactly 16 bit must be entered. \n
			:param did: 16 bits
		"""
		param = Conversions.list_to_csv_str(did)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:DID {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.mac.get_state() \n
		Activates/deactivates the generation of the MAC Header. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:STATe \n
		Snippet: driver.source.bb.wlad.pconfig.mac.set_state(state = False) \n
		Activates/deactivates the generation of the MAC Header. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:STATe {param}')

	def clone(self) -> 'Mac':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mac(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
