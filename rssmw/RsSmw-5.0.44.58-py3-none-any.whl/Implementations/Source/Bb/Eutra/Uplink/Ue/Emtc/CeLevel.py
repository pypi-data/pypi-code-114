from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CeLevel:
	"""CeLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ceLevel", core, parent)

	def set(self, ce_level: enums.EutraCeLevel, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:EMTC:CELevel \n
		Snippet: driver.source.bb.eutra.uplink.ue.emtc.ceLevel.set(ce_level = enums.EutraCeLevel.CE01, userEquipment = repcap.UserEquipment.Default) \n
		Set the coverage extension level (CE) . \n
			:param ce_level: CE01| CE23
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(ce_level, enums.EutraCeLevel)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:EMTC:CELevel {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraCeLevel:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:EMTC:CELevel \n
		Snippet: value: enums.EutraCeLevel = driver.source.bb.eutra.uplink.ue.emtc.ceLevel.get(userEquipment = repcap.UserEquipment.Default) \n
		Set the coverage extension level (CE) . \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: ce_level: CE01| CE23"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:EMTC:CELevel?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCeLevel)
