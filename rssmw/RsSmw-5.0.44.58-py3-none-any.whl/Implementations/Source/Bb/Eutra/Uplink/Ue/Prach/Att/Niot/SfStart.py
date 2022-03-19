from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfStart:
	"""SfStart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfStart", core, parent)

	def set(self, starting_sf: int, userEquipment=repcap.UserEquipment.Default, attenuationNull=repcap.AttenuationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:ATT<CH0>:NIOT:SFSTart \n
		Snippet: driver.source.bb.eutra.uplink.ue.prach.att.niot.sfStart.set(starting_sf = 1, userEquipment = repcap.UserEquipment.Default, attenuationNull = repcap.AttenuationNull.Default) \n
		Sets the starting subframe. \n
			:param starting_sf: integer Range: 0 to 1E4
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param attenuationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Att')
		"""
		param = Conversions.decimal_value_to_str(starting_sf)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		attenuationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationNull, repcap.AttenuationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:ATT{attenuationNull_cmd_val}:NIOT:SFSTart {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, attenuationNull=repcap.AttenuationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:ATT<CH0>:NIOT:SFSTart \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.prach.att.niot.sfStart.get(userEquipment = repcap.UserEquipment.Default, attenuationNull = repcap.AttenuationNull.Default) \n
		Sets the starting subframe. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param attenuationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Att')
			:return: starting_sf: integer Range: 0 to 1E4"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		attenuationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationNull, repcap.AttenuationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:ATT{attenuationNull_cmd_val}:NIOT:SFSTart?')
		return Conversions.str_to_int(response)
