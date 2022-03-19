from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipAddress", core, parent)

	@property
	def subnet(self):
		"""subnet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subnet'):
			from .Subnet import Subnet
			self._subnet = Subnet(self._core, self._cmd_group)
		return self._subnet

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.NetModeStaticOnly:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:IPADdress:MODE \n
		Snippet: value: enums.NetModeStaticOnly = driver.system.communicate.bb.qsfp.network.ipAddress.get_mode() \n
		No command help available \n
			:return: ip_address_mode: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:IPADdress:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.NetModeStaticOnly)

	def set_mode(self, ip_address_mode: enums.NetModeStaticOnly) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:IPADdress:MODE \n
		Snippet: driver.system.communicate.bb.qsfp.network.ipAddress.set_mode(ip_address_mode = enums.NetModeStaticOnly.STATic) \n
		No command help available \n
			:param ip_address_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(ip_address_mode, enums.NetModeStaticOnly)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:IPADdress:MODE {param}')

	def get_value(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:IPADdress \n
		Snippet: value: str = driver.system.communicate.bb.qsfp.network.ipAddress.get_value() \n
		No command help available \n
			:return: ip_address: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:IPADdress?')
		return trim_str_response(response)

	def set_value(self, ip_address: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:IPADdress \n
		Snippet: driver.system.communicate.bb.qsfp.network.ipAddress.set_value(ip_address = '1') \n
		No command help available \n
			:param ip_address: No help available
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:IPADdress {param}')

	def clone(self) -> 'IpAddress':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAddress(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
