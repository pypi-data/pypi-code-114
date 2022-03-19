from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prend:
	"""Prend commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prend", core, parent)

	def set(self, prb_end: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:PRENd \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdata.prend.set(prb_end = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the parameters prb-Start and prb-End and define allocation of the two SL bands. \n
			:param prb_end: integer Range: 0 to 99
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(prb_end)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:PRENd {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:PRENd \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rdata.prend.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the parameters prb-Start and prb-End and define allocation of the two SL bands. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: prb_end: integer Range: 0 to 99"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:PRENd?')
		return Conversions.str_to_int(response)
