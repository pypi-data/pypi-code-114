from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nalloc:
	"""Nalloc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nalloc", core, parent)

	def set(self, num_transmission: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:NALLoc \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.nalloc.set(num_transmission = 1, userEquipment = repcap.UserEquipment.Default) \n
		In discovery mode, sets the number of sidelink transmissions. \n
			:param num_transmission: integer Range: 0 to 100
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(num_transmission)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:NALLoc {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:NALLoc \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.nalloc.get(userEquipment = repcap.UserEquipment.Default) \n
		In discovery mode, sets the number of sidelink transmissions. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: num_transmission: integer Range: 0 to 100"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:NALLoc?')
		return Conversions.str_to_int(response)
