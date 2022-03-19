from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nretrans:
	"""Nretrans commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nretrans", core, parent)

	def set(self, num_retrans: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:NRETrans \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdisc.nretrans.set(num_retrans = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of PSDCH retransmissions. \n
			:param num_retrans: integer Range: 0 to 3
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(num_retrans)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:NRETrans {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:NRETrans \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rdisc.nretrans.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of PSDCH retransmissions. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: num_retrans: integer Range: 0 to 3"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:NRETrans?')
		return Conversions.str_to_int(response)
