from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

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
	def get_mode(self) -> enums.NetMode:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:IPADdress:MODE \n
		Snippet: value: enums.NetMode = driver.system.communicate.bb.network.ipAddress.get_mode() \n
		Selects manual or automatic setting of the IP address. \n
			:return: mode: AUTO| STATic
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:IPADdress:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.NetMode)

	def set_mode(self, mode: enums.NetMode) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:IPADdress:MODE \n
		Snippet: driver.system.communicate.bb.network.ipAddress.set_mode(mode = enums.NetMode.AUTO) \n
		Selects manual or automatic setting of the IP address. \n
			:param mode: AUTO| STATic
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NetMode)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:IPADdress:MODE {param}')

	def get_gateway(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:[IPADdress]:GATeway \n
		Snippet: value: str = driver.system.communicate.bb.network.ipAddress.get_gateway() \n
		No command help available \n
			:return: gateway: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:IPADdress:GATeway?')
		return trim_str_response(response)

	def set_gateway(self, gateway: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:[IPADdress]:GATeway \n
		Snippet: driver.system.communicate.bb.network.ipAddress.set_gateway(gateway = '1') \n
		No command help available \n
			:param gateway: No help available
		"""
		param = Conversions.value_to_quoted_str(gateway)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:IPADdress:GATeway {param}')

	def get_value(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:IPADdress \n
		Snippet: value: str = driver.system.communicate.bb.network.ipAddress.get_value() \n
		Sets the IP address. \n
			:return: ip_address: string Range: 0.0.0.0. to ff.ff.ff.ff
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:IPADdress?')
		return trim_str_response(response)

	def set_value(self, ip_address: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:IPADdress \n
		Snippet: driver.system.communicate.bb.network.ipAddress.set_value(ip_address = '1') \n
		Sets the IP address. \n
			:param ip_address: string Range: 0.0.0.0. to ff.ff.ff.ff
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:IPADdress {param}')

	def clone(self) -> 'IpAddress':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAddress(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
