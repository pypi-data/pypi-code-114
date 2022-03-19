from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 12 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def ipAddress(self):
		"""ipAddress commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_ipAddress'):
			from .IpAddress import IpAddress
			self._ipAddress = IpAddress(self._core, self._cmd_group)
		return self._ipAddress

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import Restart
			self._restart = Restart(self._core, self._cmd_group)
		return self._restart

	@property
	def common(self):
		"""common commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	def get_mac_address(self) -> str:
		"""SCPI: SYSTem:COMMunicate:NETWork:MACaddress \n
		Snippet: value: str = driver.system.communicate.network.get_mac_address() \n
		Queries the MAC address of the network adapter. This is a password-protected function. Unlock the protection level 1 to
		access it. See method RsSmw.System.Protect.State.set. \n
			:return: mac_address: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:MACaddress?')
		return trim_str_response(response)

	def set_mac_address(self, mac_address: str) -> None:
		"""SCPI: SYSTem:COMMunicate:NETWork:MACaddress \n
		Snippet: driver.system.communicate.network.set_mac_address(mac_address = '1') \n
		Queries the MAC address of the network adapter. This is a password-protected function. Unlock the protection level 1 to
		access it. See method RsSmw.System.Protect.State.set. \n
			:param mac_address: string
		"""
		param = Conversions.value_to_quoted_str(mac_address)
		self._core.io.write(f'SYSTem:COMMunicate:NETWork:MACaddress {param}')

	def get_resource(self) -> str:
		"""SCPI: SYSTem:COMMunicate:NETWork:RESource \n
		Snippet: value: str = driver.system.communicate.network.get_resource() \n
		Queries the visa resource string for Ethernet instruments. \n
			:return: resource: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:RESource?')
		return trim_str_response(response)

	def get_status(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:NETWork:STATus \n
		Snippet: value: bool = driver.system.communicate.network.get_status() \n
		Queries the network configuration state. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:STATus?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
