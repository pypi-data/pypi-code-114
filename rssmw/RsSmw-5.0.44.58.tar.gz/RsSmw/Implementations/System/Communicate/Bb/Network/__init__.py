from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 12 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def ipAddress(self):
		"""ipAddress commands group. 1 Sub-classes, 3 commands."""
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
		"""common commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	def get_busy(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:BUSY \n
		Snippet: value: bool = driver.system.communicate.bb.network.get_busy() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:BUSY?')
		return Conversions.str_to_bool(response)

	def get_mac_address(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:MACaddress \n
		Snippet: value: str = driver.system.communicate.bb.network.get_mac_address() \n
		Queries the MAC address of the network adapter. This is a password-protected function. Unlock the protection level 1 to
		access it, see method RsSmw.System.Protect.State.set in the R&S SMW user manual. \n
			:return: mac_address: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:MACaddress?')
		return trim_str_response(response)

	def set_mac_address(self, mac_address: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:MACaddress \n
		Snippet: driver.system.communicate.bb.network.set_mac_address(mac_address = '1') \n
		Queries the MAC address of the network adapter. This is a password-protected function. Unlock the protection level 1 to
		access it, see method RsSmw.System.Protect.State.set in the R&S SMW user manual. \n
			:param mac_address: string
		"""
		param = Conversions.value_to_quoted_str(mac_address)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:MACaddress {param}')

	def get_port(self) -> int:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:PORT \n
		Snippet: value: int = driver.system.communicate.bb.network.get_port() \n
		Sets the port address use for network traffic. \n
			:return: port: integer Range: 0 to 65536
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, port: int) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:PORT \n
		Snippet: driver.system.communicate.bb.network.set_port(port = 1) \n
		Sets the port address use for network traffic. \n
			:param port: integer Range: 0 to 65536
		"""
		param = Conversions.decimal_value_to_str(port)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:PORT {param}')

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.NetProtocol:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:PROTocol \n
		Snippet: value: enums.NetProtocol = driver.system.communicate.bb.network.get_protocol() \n
		Selects the communication protocol for the network traffic. \n
			:return: protocol: UDP| TCP
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.NetProtocol)

	def set_protocol(self, protocol: enums.NetProtocol) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:PROTocol \n
		Snippet: driver.system.communicate.bb.network.set_protocol(protocol = enums.NetProtocol.TCP) \n
		Selects the communication protocol for the network traffic. \n
			:param protocol: UDP| TCP
		"""
		param = Conversions.enum_scalar_to_str(protocol, enums.NetProtocol)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:PROTocol {param}')

	def get_status(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:STATus \n
		Snippet: value: bool = driver.system.communicate.bb.network.get_status() \n
		Queries the network configuration state. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:STATus?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
