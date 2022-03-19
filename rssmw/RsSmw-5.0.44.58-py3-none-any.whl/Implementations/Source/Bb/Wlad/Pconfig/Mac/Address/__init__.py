from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: AddressField, default value after init: AddressField.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_addressField_get', 'repcap_addressField_set', repcap.AddressField.Nr1)

	def repcap_addressField_set(self, addressField: repcap.AddressField) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AddressField.Default
		Default value after init: AddressField.Nr1"""
		self._cmd_group.set_repcap_enum_value(addressField)

	def repcap_addressField_get(self) -> repcap.AddressField:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, address: List[str], addressField=repcap.AddressField.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:ADDRess<ST> \n
		Snippet: driver.source.bb.wlad.pconfig.mac.address.set(address = ['raw1', 'raw2', 'raw3'], addressField = repcap.AddressField.Default) \n
		Sets the value of the address fields 1 ... 4. Exactly 48 bits must be entered. Each address is 6 bytes (48 bit) long. The
		addresses can be entered in hexadecimal form in the entry field of each address field. The least significant byte (LSB)
		is in left notation. \n
			:param address: 48 bits
			:param addressField: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
		"""
		param = Conversions.list_to_csv_str(address)
		addressField_cmd_val = self._cmd_group.get_repcap_cmd_value(addressField, repcap.AddressField)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:ADDRess{addressField_cmd_val} {param}')

	def get(self, addressField=repcap.AddressField.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:ADDRess<ST> \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.address.get(addressField = repcap.AddressField.Default) \n
		Sets the value of the address fields 1 ... 4. Exactly 48 bits must be entered. Each address is 6 bytes (48 bit) long. The
		addresses can be entered in hexadecimal form in the entry field of each address field. The least significant byte (LSB)
		is in left notation. \n
			:param addressField: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
			:return: address: 48 bits"""
		addressField_cmd_val = self._cmd_group.get_repcap_cmd_value(addressField, repcap.AddressField)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:ADDRess{addressField_cmd_val}?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Address':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Address(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
