from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)

	def set(self, port: int, ipVersion=repcap.IpVersion.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:PORT \n
		Snippet: driver.source.bb.inputPy.ip.port.set(port = 1, ipVersion = repcap.IpVersion.Default) \n
		Sets the port of the input IP data at the 'IP Data' connector. \n
			:param port: integer Range: 0 to 65535
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
		"""
		param = Conversions.decimal_value_to_str(port)
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:PORT {param}')

	def get(self, ipVersion=repcap.IpVersion.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:PORT \n
		Snippet: value: int = driver.source.bb.inputPy.ip.port.get(ipVersion = repcap.IpVersion.Default) \n
		Sets the port of the input IP data at the 'IP Data' connector. \n
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
			:return: port: integer Range: 0 to 65535"""
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:PORT?')
		return Conversions.str_to_int(response)
