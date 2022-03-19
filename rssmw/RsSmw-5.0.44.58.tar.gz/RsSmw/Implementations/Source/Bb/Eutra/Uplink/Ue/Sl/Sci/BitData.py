from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitData:
	"""BitData commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitData", core, parent)

	def get(self, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:BITData \n
		Snippet: value: List[str] = driver.source.bb.eutra.uplink.ue.sl.sci.bitData.get(userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Queries the resulting bit data as configured with the [:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:SCI<ch0> commands. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
			:return: bit_data: bit pattern"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:BITData?')
		return Conversions.str_to_str_list(response)
