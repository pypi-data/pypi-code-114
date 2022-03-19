from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.UeMode, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:MODE \n
		Snippet: driver.source.bb.oneweb.uplink.ue.mode.set(mode = enums.UeMode.PRACh, userEquipment = repcap.UserEquipment.Default) \n
		Selects whether the user equipment is in standard or in PRACH mode. \n
			:param mode: STD| PRACh
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.UeMode)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.UeMode:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:MODE \n
		Snippet: value: enums.UeMode = driver.source.bb.oneweb.uplink.ue.mode.get(userEquipment = repcap.UserEquipment.Default) \n
		Selects whether the user equipment is in standard or in PRACH mode. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: mode: STD| PRACh"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.UeMode)
