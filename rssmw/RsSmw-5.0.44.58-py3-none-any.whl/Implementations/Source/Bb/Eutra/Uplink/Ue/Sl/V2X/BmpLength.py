from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BmpLength:
	"""BmpLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bmpLength", core, parent)

	def set(self, bmp_length: enums.EutraSlV2xBmpLength, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:BMPLength \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.v2X.bmpLength.set(bmp_length = enums.EutraSlV2xBmpLength._10, userEquipment = repcap.UserEquipment.Default) \n
		Sets the bitmap length. To set the subframe bitmap, use the commands [:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BITLow and
		[:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BITHigh. \n
			:param bmp_length: 10| 16| 20| 30| 40| 50| 60| 100
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(bmp_length, enums.EutraSlV2xBmpLength)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:BMPLength {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSlV2xBmpLength:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:BMPLength \n
		Snippet: value: enums.EutraSlV2xBmpLength = driver.source.bb.eutra.uplink.ue.sl.v2X.bmpLength.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the bitmap length. To set the subframe bitmap, use the commands [:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BITLow and
		[:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BITHigh. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: bmp_length: 10| 16| 20| 30| 40| 50| 60| 100"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:BMPLength?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSlV2xBmpLength)
