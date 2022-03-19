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

	def set(self, mode: enums.EutraSlMode, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:MODE \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.mode.set(mode = enums.EutraSlMode.COMM, userEquipment = repcap.UserEquipment.Default) \n
		Sets the mode of the sidelink communication. \n
			:param mode: COMM| DISC | V2X
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EutraSlMode)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSlMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:MODE \n
		Snippet: value: enums.EutraSlMode = driver.source.bb.eutra.uplink.ue.sl.mode.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the mode of the sidelink communication. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: mode: COMM| DISC | V2X"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSlMode)
