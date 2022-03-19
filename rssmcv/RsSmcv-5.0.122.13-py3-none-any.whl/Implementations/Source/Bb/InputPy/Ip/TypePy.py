from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.CodingIpType, ipVersion=repcap.IpVersion.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:TYPE \n
		Snippet: driver.source.bb.inputPy.ip.typePy.set(type_py = enums.CodingIpType.MULTicast, ipVersion = repcap.IpVersion.Default) \n
		Sets the IP input type. \n
			:param type_py: UNIcast| MULTicast UNIcast Analyzes all unicast IP packets that arrive at the specified port. See [:SOURcehw]:BB:INPut:IPch:PORT. MULTicast When an IP address is in the multicast address range, an attempt is made to join a multicast group using . Set multicast address and port. See: [:SOURcehw]:BB:INPut:IPch:MULticast:ADDRess [:SOURcehw]:BB:INPut:IPch:PORT
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.CodingIpType)
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, ipVersion=repcap.IpVersion.Default) -> enums.CodingIpType:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:TYPE \n
		Snippet: value: enums.CodingIpType = driver.source.bb.inputPy.ip.typePy.get(ipVersion = repcap.IpVersion.Default) \n
		Sets the IP input type. \n
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
			:return: type_py: UNIcast| MULTicast UNIcast Analyzes all unicast IP packets that arrive at the specified port. See [:SOURcehw]:BB:INPut:IPch:PORT. MULTicast When an IP address is in the multicast address range, an attempt is made to join a multicast group using . Set multicast address and port. See: [:SOURcehw]:BB:INPut:IPch:MULticast:ADDRess [:SOURcehw]:BB:INPut:IPch:PORT"""
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.CodingIpType)
