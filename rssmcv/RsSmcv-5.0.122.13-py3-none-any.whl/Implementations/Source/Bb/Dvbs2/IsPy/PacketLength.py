from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PacketLength:
	"""PacketLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("packetLength", core, parent)

	# noinspection PyTypeChecker
	def get(self, inputStream=repcap.InputStream.Default) -> enums.InputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[IS<CH>]:PACKetlength \n
		Snippet: value: enums.InputSignalPacketLength = driver.source.bb.dvbs2.isPy.packetLength.get(inputStream = repcap.InputStream.Default) \n
		Queries the packet length of the external transport stream in bytes. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: packet_length: P188| P204| INValid P188|P204 188/204 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length."""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:IS{inputStream_cmd_val}:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalPacketLength)
