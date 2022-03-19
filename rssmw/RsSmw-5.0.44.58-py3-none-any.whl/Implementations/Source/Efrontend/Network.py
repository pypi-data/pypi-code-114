from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	def set(self, ip_address: str, subnet_mask: str, dhcp_on: int) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:NETWork \n
		Snippet: driver.source.efrontend.network.set(ip_address = '1', subnet_mask = '1', dhcp_on = 1) \n
		Sets network parameters of the external frontend. \n
			:param ip_address: string IP address of the external frontend
			:param subnet_mask: string Bit group of the subnet in the host identifier
			:param dhcp_on: integer DHCP state Range: 0 to 1
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ip_address', ip_address, DataType.String), ArgSingle('subnet_mask', subnet_mask, DataType.String), ArgSingle('dhcp_on', dhcp_on, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:NETWork {param}'.rstrip())

	# noinspection PyTypeChecker
	class NetworkStruct(StructBase):
		"""Response structure. Fields: \n
			- Ip_Address: str: string IP address of the external frontend
			- Subnet_Mask: str: string Bit group of the subnet in the host identifier
			- Dhcp_On: int: integer DHCP state Range: 0 to 1"""
		__meta_args_list = [
			ArgStruct.scalar_str('Ip_Address'),
			ArgStruct.scalar_str('Subnet_Mask'),
			ArgStruct.scalar_int('Dhcp_On')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ip_Address: str = None
			self.Subnet_Mask: str = None
			self.Dhcp_On: int = None

	def get(self) -> NetworkStruct:
		"""SCPI: [SOURce<HW>]:EFRontend:NETWork \n
		Snippet: value: NetworkStruct = driver.source.efrontend.network.get() \n
		Sets network parameters of the external frontend. \n
			:return: structure: for return value, see the help for NetworkStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:EFRontend:NETWork?', self.__class__.NetworkStruct())
