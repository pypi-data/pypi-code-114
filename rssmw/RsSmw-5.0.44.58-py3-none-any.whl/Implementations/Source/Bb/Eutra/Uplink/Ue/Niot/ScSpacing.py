from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScSpacing:
	"""ScSpacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scSpacing", core, parent)

	def set(self, sub_carr_spacing: enums.EutraSubCarrierSpacing, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:SCSPacing \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.scSpacing.set(sub_carr_spacing = enums.EutraSubCarrierSpacing.S15, userEquipment = repcap.UserEquipment.Default) \n
		Sets the subcarrier spacing. \n
			:param sub_carr_spacing: S15| S375
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(sub_carr_spacing, enums.EutraSubCarrierSpacing)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:SCSPacing {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSubCarrierSpacing:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:SCSPacing \n
		Snippet: value: enums.EutraSubCarrierSpacing = driver.source.bb.eutra.uplink.ue.niot.scSpacing.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the subcarrier spacing. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: sub_carr_spacing: S15| S375"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSubCarrierSpacing)
