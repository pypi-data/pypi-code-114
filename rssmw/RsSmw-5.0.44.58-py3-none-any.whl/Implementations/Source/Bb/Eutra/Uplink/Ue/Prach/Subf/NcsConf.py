from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcsConf:
	"""NcsConf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncsConf", core, parent)

	def set(self, ncs_config: int, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:SUBF<CH0>:NCSConf \n
		Snippet: driver.source.bb.eutra.uplink.ue.prach.subf.ncsConf.set(ncs_config = 1, userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		Selects the Ncs configuration of the selected subframe. \n
			:param ncs_config: integer For details on the value range, see Table 'Value range Ncs configuration'. Range: 0 to 15
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.decimal_value_to_str(ncs_config)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:NCSConf {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:SUBF<CH0>:NCSConf \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.prach.subf.ncsConf.get(userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		Selects the Ncs configuration of the selected subframe. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: ncs_config: integer For details on the value range, see Table 'Value range Ncs configuration'. Range: 0 to 15"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:NCSConf?')
		return Conversions.str_to_int(response)
