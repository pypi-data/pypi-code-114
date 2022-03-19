from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 8 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def common(self):
		"""common commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	@property
	def ipAddress(self):
		"""ipAddress commands group. 1 Sub-classes, 2 commands."""
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

	def get_mac_address(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:MACaddress \n
		Snippet: value: str = driver.system.communicate.bcIp.network.get_mac_address() \n
		Queries the MAC address of the network adapter. \n
			:return: mac_address: string Range: 00:00:00:00:00:00 to ff:ff:ff:ff:ff:ff
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BCIP:NETWork:MACaddress?')
		return trim_str_response(response)

	def set_mac_address(self, mac_address: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:MACaddress \n
		Snippet: driver.system.communicate.bcIp.network.set_mac_address(mac_address = '1') \n
		Queries the MAC address of the network adapter. \n
			:param mac_address: string Range: 00:00:00:00:00:00 to ff:ff:ff:ff:ff:ff
		"""
		param = Conversions.value_to_quoted_str(mac_address)
		self._core.io.write(f'SYSTem:COMMunicate:BCIP:NETWork:MACaddress {param}')

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.NetProtocol:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:PROTocol \n
		Snippet: value: enums.NetProtocol = driver.system.communicate.bcIp.network.get_protocol() \n
		Specifies the network protocol. \n
			:return: protocol: UDP
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BCIP:NETWork:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.NetProtocol)

	def set_protocol(self, protocol: enums.NetProtocol) -> None:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:PROTocol \n
		Snippet: driver.system.communicate.bcIp.network.set_protocol(protocol = enums.NetProtocol.TCP) \n
		Specifies the network protocol. \n
			:param protocol: UDP
		"""
		param = Conversions.enum_scalar_to_str(protocol, enums.NetProtocol)
		self._core.io.write(f'SYSTem:COMMunicate:BCIP:NETWork:PROTocol {param}')

	def get_status(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:STATus \n
		Snippet: value: bool = driver.system.communicate.bcIp.network.get_status() \n
		Queries the network connection state. \n
			:return: network_status: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BCIP:NETWork:STATus?')
		return Conversions.str_to_bool(response)

	def set_status(self, network_status: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:STATus \n
		Snippet: driver.system.communicate.bcIp.network.set_status(network_status = False) \n
		Queries the network connection state. \n
			:param network_status: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(network_status)
		self._core.io.write(f'SYSTem:COMMunicate:BCIP:NETWork:STATus {param}')

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
