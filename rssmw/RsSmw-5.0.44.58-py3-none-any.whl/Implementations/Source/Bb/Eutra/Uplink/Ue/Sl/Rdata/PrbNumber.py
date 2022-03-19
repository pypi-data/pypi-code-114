from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrbNumber:
	"""PrbNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prbNumber", core, parent)

	def set(self, prb_number: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:PRBNumber \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdata.prbNumber.set(prb_number = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of resource blocks each of the SL bands occupies. \n
			:param prb_number: integer Range: 1 to 100
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(prb_number)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:PRBNumber {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:PRBNumber \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rdata.prbNumber.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of resource blocks each of the SL bands occupies. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: prb_number: integer Range: 1 to 100"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:PRBNumber?')
		return Conversions.str_to_int(response)
