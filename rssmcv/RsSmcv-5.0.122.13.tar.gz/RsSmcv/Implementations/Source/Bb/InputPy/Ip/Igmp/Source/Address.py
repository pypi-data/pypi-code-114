from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def set(self, bc_coding_ip_igmpv_3_source_address: bytes, ipVersion=repcap.IpVersion.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:IGMP:[SOURce]:ADDRess \n
		Snippet: driver.source.bb.inputPy.ip.igmp.source.address.set(bc_coding_ip_igmpv_3_source_address = b'ABCDEFGH', ipVersion = repcap.IpVersion.Default) \n
		Specifies the IGMP source address of the network. \n
			:param bc_coding_ip_igmpv_3_source_address: string
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
		"""
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		self._core.io.write_bin_block(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:IGMP:SOURce:ADDRess ', bc_coding_ip_igmpv_3_source_address)

	def get(self, ipVersion=repcap.IpVersion.Default) -> bytes:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:IGMP:[SOURce]:ADDRess \n
		Snippet: value: bytes = driver.source.bb.inputPy.ip.igmp.source.address.get(ipVersion = repcap.IpVersion.Default) \n
		Specifies the IGMP source address of the network. \n
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
			:return: bc_coding_ip_igmpv_3_source_address: No help available"""
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		response = self._core.io.query_bin_block_ERROR(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:IGMP:SOURce:ADDRess?')
		return response
