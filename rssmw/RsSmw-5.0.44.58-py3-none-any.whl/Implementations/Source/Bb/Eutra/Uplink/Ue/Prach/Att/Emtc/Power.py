from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, userEquipment=repcap.UserEquipment.Default, attenuationNull=repcap.AttenuationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:ATT<CH0>:EMTC:POWer \n
		Snippet: driver.source.bb.eutra.uplink.ue.prach.att.emtc.power.set(power = 1.0, userEquipment = repcap.UserEquipment.Default, attenuationNull = repcap.AttenuationNull.Default) \n
		Sets the preamble attempt power relative to the UE power. \n
			:param power: float Range: -80.000 to 10.000
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param attenuationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Att')
		"""
		param = Conversions.decimal_value_to_str(power)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		attenuationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationNull, repcap.AttenuationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:ATT{attenuationNull_cmd_val}:EMTC:POWer {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, attenuationNull=repcap.AttenuationNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:ATT<CH0>:EMTC:POWer \n
		Snippet: value: float = driver.source.bb.eutra.uplink.ue.prach.att.emtc.power.get(userEquipment = repcap.UserEquipment.Default, attenuationNull = repcap.AttenuationNull.Default) \n
		Sets the preamble attempt power relative to the UE power. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param attenuationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Att')
			:return: power: float Range: -80.000 to 10.000"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		attenuationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationNull, repcap.AttenuationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:ATT{attenuationNull_cmd_val}:EMTC:POWer?')
		return Conversions.str_to_float(response)
