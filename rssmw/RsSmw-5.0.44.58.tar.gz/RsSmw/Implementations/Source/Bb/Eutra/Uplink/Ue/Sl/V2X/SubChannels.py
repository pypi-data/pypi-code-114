from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubChannels:
	"""SubChannels commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subChannels", core, parent)

	def set(self, num_subchannels: enums.EutraSlV2xNumSubchannels, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:SUBChannels \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.v2X.subChannels.set(num_subchannels = enums.EutraSlV2xNumSubchannels._1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of subchannels. \n
			:param num_subchannels: 1| 3| 5| 8| 10| 15| 20
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(num_subchannels, enums.EutraSlV2xNumSubchannels)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:SUBChannels {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSlV2xNumSubchannels:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:SUBChannels \n
		Snippet: value: enums.EutraSlV2xNumSubchannels = driver.source.bb.eutra.uplink.ue.sl.v2X.subChannels.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of subchannels. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: num_subchannels: 1| 3| 5| 8| 10| 15| 20"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:SUBChannels?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSlV2xNumSubchannels)
