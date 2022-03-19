from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbIndex:
	"""RbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbIndex", core, parent)

	def set(self, res_block_index: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:RBINdex \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.rbIndex.set(res_block_index = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the resource block number in that the NB-IoT transmissions are allocated. \n
			:param res_block_index: integer Range: Depends on other values
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(res_block_index)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:RBINdex {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:RBINdex \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.niot.rbIndex.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the resource block number in that the NB-IoT transmissions are allocated. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: res_block_index: integer Range: Depends on other values"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:RBINdex?')
		return Conversions.str_to_int(response)
