from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ping:
	"""Ping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ping", core, parent)

	def set(self, ipVersion=repcap.IpVersion.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:IGMP:[SOURce]:PING \n
		Snippet: driver.source.bb.inputPy.ip.igmp.source.ping.set(ipVersion = repcap.IpVersion.Default) \n
		Triggers pinging of the IGMP source address in the local IP data network.
		Query the result via [:SOURce<hw>]:BB:INPut:IP<ch>:IGMP[:SOURce]:RESult?. \n
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
		"""
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:IGMP:SOURce:PING')

	def set_with_opc(self, ipVersion=repcap.IpVersion.Default, opc_timeout_ms: int = -1) -> None:
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:IGMP:[SOURce]:PING \n
		Snippet: driver.source.bb.inputPy.ip.igmp.source.ping.set_with_opc(ipVersion = repcap.IpVersion.Default) \n
		Triggers pinging of the IGMP source address in the local IP data network.
		Query the result via [:SOURce<hw>]:BB:INPut:IP<ch>:IGMP[:SOURce]:RESult?. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:IGMP:SOURce:PING', opc_timeout_ms)
