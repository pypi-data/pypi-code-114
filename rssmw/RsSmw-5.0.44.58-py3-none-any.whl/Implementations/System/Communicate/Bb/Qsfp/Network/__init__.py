from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 14 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def diagnostic(self):
		"""diagnostic commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_diagnostic'):
			from .Diagnostic import Diagnostic
			self._diagnostic = Diagnostic(self._core, self._cmd_group)
		return self._diagnostic

	@property
	def ipAddress(self):
		"""ipAddress commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ipAddress'):
			from .IpAddress import IpAddress
			self._ipAddress = IpAddress(self._core, self._cmd_group)
		return self._ipAddress

	@property
	def common(self):
		"""common commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	def get_application(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:APPLication \n
		Snippet: value: str = driver.system.communicate.bb.qsfp.network.get_application() \n
		No command help available \n
			:return: running_app: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:APPLication?')
		return trim_str_response(response)

	def get_mac_address(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:MACaddress \n
		Snippet: value: str = driver.system.communicate.bb.qsfp.network.get_mac_address() \n
		No command help available \n
			:return: mac_address: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:MACaddress?')
		return trim_str_response(response)

	def get_port(self) -> int:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:PORT \n
		Snippet: value: int = driver.system.communicate.bb.qsfp.network.get_port() \n
		No command help available \n
			:return: port_number: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, port_number: int) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:PORT \n
		Snippet: driver.system.communicate.bb.qsfp.network.set_port(port_number = 1) \n
		No command help available \n
			:param port_number: No help available
		"""
		param = Conversions.decimal_value_to_str(port_number)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:PORT {param}')

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.NetProtocolUdpOnly:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:PROTocol \n
		Snippet: value: enums.NetProtocolUdpOnly = driver.system.communicate.bb.qsfp.network.get_protocol() \n
		No command help available \n
			:return: protocol: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.NetProtocolUdpOnly)

	def set_protocol(self, protocol: enums.NetProtocolUdpOnly) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:PROTocol \n
		Snippet: driver.system.communicate.bb.qsfp.network.set_protocol(protocol = enums.NetProtocolUdpOnly.UDP) \n
		No command help available \n
			:param protocol: No help available
		"""
		param = Conversions.enum_scalar_to_str(protocol, enums.NetProtocolUdpOnly)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:PROTocol {param}')

	def get_status(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:STATus \n
		Snippet: value: bool = driver.system.communicate.bb.qsfp.network.get_status() \n
		No command help available \n
			:return: network_status: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:STATus?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
