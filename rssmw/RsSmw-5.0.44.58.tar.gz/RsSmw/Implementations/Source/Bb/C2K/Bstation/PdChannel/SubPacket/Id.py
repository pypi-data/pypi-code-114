from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def set(self, idn: enums.NumbersG, baseStation=repcap.BaseStation.Default, subpacket=repcap.Subpacket.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:SUBPacket<DI>:ID \n
		Snippet: driver.source.bb.c2K.bstation.pdChannel.subPacket.id.set(idn = enums.NumbersG._0, baseStation = repcap.BaseStation.Default, subpacket = repcap.Subpacket.Default) \n
		The command selects the sub packet ID for F_PDCH. The sub packet ID determines the sub packet symbol selection and
		selects one of four available subpackets of the encoder packets. The SPID of sub packet 1 is always 1. \n
			:param idn: 0| 1| 2| 3 Range: 0 to 3
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param subpacket: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubPacket')
		"""
		param = Conversions.enum_scalar_to_str(idn, enums.NumbersG)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		subpacket_cmd_val = self._cmd_group.get_repcap_cmd_value(subpacket, repcap.Subpacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:SUBPacket{subpacket_cmd_val}:ID {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, subpacket=repcap.Subpacket.Default) -> enums.NumbersG:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:SUBPacket<DI>:ID \n
		Snippet: value: enums.NumbersG = driver.source.bb.c2K.bstation.pdChannel.subPacket.id.get(baseStation = repcap.BaseStation.Default, subpacket = repcap.Subpacket.Default) \n
		The command selects the sub packet ID for F_PDCH. The sub packet ID determines the sub packet symbol selection and
		selects one of four available subpackets of the encoder packets. The SPID of sub packet 1 is always 1. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param subpacket: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubPacket')
			:return: idn: 0| 1| 2| 3 Range: 0 to 3"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		subpacket_cmd_val = self._cmd_group.get_repcap_cmd_value(subpacket, repcap.Subpacket)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:SUBPacket{subpacket_cmd_val}:ID?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersG)
