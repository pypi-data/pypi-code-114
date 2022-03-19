from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Puach:
	"""Puach commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("puach", core, parent)

	def set(self, conf_subframes: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:CONSubframes:PUACh \n
		Snippet: driver.source.bb.oneweb.uplink.ue.conSubFrames.puach.set(conf_subframes = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of configurable subframes. \n
			:param conf_subframes: integer Range: 1 to 40
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(conf_subframes)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:CONSubframes:PUACh {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:CONSubframes:PUACh \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.ue.conSubFrames.puach.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of configurable subframes. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: conf_subframes: integer Range: 1 to 40"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:CONSubframes:PUACh?')
		return Conversions.str_to_int(response)
