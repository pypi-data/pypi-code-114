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
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.InputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:PACKetlength \n
		Snippet: value: enums.InputSignalPacketLength = driver.source.bb.t2Dvb.plp.packetLength.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the packet length of the external transport stream in bytes. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: packet_length: P188| INValid P188 188 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length."""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalPacketLength)
