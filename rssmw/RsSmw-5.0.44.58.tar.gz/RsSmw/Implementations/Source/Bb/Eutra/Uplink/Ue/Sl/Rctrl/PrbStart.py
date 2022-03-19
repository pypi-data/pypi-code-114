from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrbStart:
	"""PrbStart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prbStart", core, parent)

	def set(self, prb_start: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RCTRl:PRBStart \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rctrl.prbStart.set(prb_start = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the parameters prb-Start and prb-End and define allocation of the two SL bands. \n
			:param prb_start: integer Range: 0 to 99
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(prb_start)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RCTRl:PRBStart {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RCTRl:PRBStart \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rctrl.prbStart.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the parameters prb-Start and prb-End and define allocation of the two SL bands. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: prb_start: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RCTRl:PRBStart?')
		return Conversions.str_to_int(response)
