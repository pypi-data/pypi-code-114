from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StartSf:
	"""StartSf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("startSf", core, parent)

	def set(self, start_sf: int, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:STARtsf \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.sci.startSf.set(start_sf = 1, userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the first subframe used for the SL transmission. \n
			:param start_sf: integer Range: 0 to 655650
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
		"""
		param = Conversions.decimal_value_to_str(start_sf)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:STARtsf {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:STARtsf \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.sci.startSf.get(userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the first subframe used for the SL transmission. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
			:return: start_sf: integer Range: 0 to 655650"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:STARtsf?')
		return Conversions.str_to_int(response)
