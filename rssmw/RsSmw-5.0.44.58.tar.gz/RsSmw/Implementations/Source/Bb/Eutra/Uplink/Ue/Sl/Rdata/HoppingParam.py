from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HoppingParam:
	"""HoppingParam commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hoppingParam", core, parent)

	def set(self, hopping_param: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:HOPPingparam \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdata.hoppingParam.set(hopping_param = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the frequency hopping parameter. \n
			:param hopping_param: integer Range: 0 to 504
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(hopping_param)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:HOPPingparam {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:HOPPingparam \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rdata.hoppingParam.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the frequency hopping parameter. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: hopping_param: integer Range: 0 to 504"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:HOPPingparam?')
		return Conversions.str_to_int(response)
