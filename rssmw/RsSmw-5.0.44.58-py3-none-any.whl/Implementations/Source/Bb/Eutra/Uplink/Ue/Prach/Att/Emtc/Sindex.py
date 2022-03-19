from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sindex:
	"""Sindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sindex", core, parent)

	def set(self, sequence_index: int, userEquipment=repcap.UserEquipment.Default, attenuationNull=repcap.AttenuationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:ATT<CH0>:EMTC:SINDex \n
		Snippet: driver.source.bb.eutra.uplink.ue.prach.att.emtc.sindex.set(sequence_index = 1, userEquipment = repcap.UserEquipment.Default, attenuationNull = repcap.AttenuationNull.Default) \n
		Sets the sequence index v. \n
			:param sequence_index: integer Range: 0 to 63
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param attenuationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Att')
		"""
		param = Conversions.decimal_value_to_str(sequence_index)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		attenuationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationNull, repcap.AttenuationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:ATT{attenuationNull_cmd_val}:EMTC:SINDex {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, attenuationNull=repcap.AttenuationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:ATT<CH0>:EMTC:SINDex \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.prach.att.emtc.sindex.get(userEquipment = repcap.UserEquipment.Default, attenuationNull = repcap.AttenuationNull.Default) \n
		Sets the sequence index v. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param attenuationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Att')
			:return: sequence_index: integer Range: 0 to 63"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		attenuationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationNull, repcap.AttenuationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:ATT{attenuationNull_cmd_val}:EMTC:SINDex?')
		return Conversions.str_to_int(response)
