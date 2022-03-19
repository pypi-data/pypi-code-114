from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubSize:
	"""SubSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subSize", core, parent)

	def set(self, sub_channel_size: enums.EutraSlV2xSubchannelSize, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:SUBSize \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.v2X.subSize.set(sub_channel_size = enums.EutraSlV2xSubchannelSize._10, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of resource blocks the subchannel spans. \n
			:param sub_channel_size: 4| 5| 6| 8| 9| 10| 12| 15| 16| 18| 20| 25| 30| 48| 50| 72| 96| 75| 100| 32
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(sub_channel_size, enums.EutraSlV2xSubchannelSize)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:SUBSize {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSlV2xSubchannelSize:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:SUBSize \n
		Snippet: value: enums.EutraSlV2xSubchannelSize = driver.source.bb.eutra.uplink.ue.sl.v2X.subSize.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of resource blocks the subchannel spans. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: sub_channel_size: 4| 5| 6| 8| 9| 10| 12| 15| 16| 18| 20| 25| 30| 48| 50| 72| 96| 75| 100| 32"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:SUBSize?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSlV2xSubchannelSize)
