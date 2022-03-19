from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.IdEutraNbiotMode, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:MODE \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.mode.set(mode = enums.IdEutraNbiotMode.ALON, userEquipment = repcap.UserEquipment.Default) \n
		Selects the operating mode. \n
			:param mode: INBD| ALON| GBD
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.IdEutraNbiotMode)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.IdEutraNbiotMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:MODE \n
		Snippet: value: enums.IdEutraNbiotMode = driver.source.bb.eutra.uplink.ue.niot.mode.get(userEquipment = repcap.UserEquipment.Default) \n
		Selects the operating mode. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: mode: INBD| ALON| GBD"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IdEutraNbiotMode)
