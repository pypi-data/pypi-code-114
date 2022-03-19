from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrptSubset:
	"""TrptSubset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trptSubset", core, parent)

	def set(self, trpt_subset: List[str], userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:TRPTsubset \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdata.trptSubset.set(trpt_subset = ['raw1', 'raw2', 'raw3'], userEquipment = repcap.UserEquipment.Default) \n
		The TRTP subset is a time resources pattern that indicates the set of available subframes to be used for sidelink
		communication. \n
			:param trpt_subset: 5 bits
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.list_to_csv_str(trpt_subset)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:TRPTsubset {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:TRPTsubset \n
		Snippet: value: List[str] = driver.source.bb.eutra.uplink.ue.sl.rdata.trptSubset.get(userEquipment = repcap.UserEquipment.Default) \n
		The TRTP subset is a time resources pattern that indicates the set of available subframes to be used for sidelink
		communication. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: trpt_subset: 5 bits"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:TRPTsubset?')
		return Conversions.str_to_str_list(response)
