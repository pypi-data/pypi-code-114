from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	def set(self, conf_subframes: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:CONSubframes:PUSCh \n
		Snippet: driver.source.bb.eutra.uplink.ue.conSubFrames.pusch.set(conf_subframes = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of configurable subframes. \n
			:param conf_subframes: integer Range: 1 to 40
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(conf_subframes)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CONSubframes:PUSCh {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:CONSubframes:PUSCh \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.conSubFrames.pusch.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of configurable subframes. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: conf_subframes: integer Range: 1 to 40"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CONSubframes:PUSCh?')
		return Conversions.str_to_int(response)
