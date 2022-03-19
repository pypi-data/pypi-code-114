from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxMode:
	"""TxMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txMode", core, parent)

	def set(self, sci_tx_mode: enums.NumberA, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:TXMode \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.sci.txMode.set(sci_tx_mode = enums.NumberA._1, userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the transmission mode of the SL transmission. \n
			:param sci_tx_mode: 1| 2 | 3| 4
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
		"""
		param = Conversions.enum_scalar_to_str(sci_tx_mode, enums.NumberA)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:TXMode {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:TXMode \n
		Snippet: value: enums.NumberA = driver.source.bb.eutra.uplink.ue.sl.sci.txMode.get(userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the transmission mode of the SL transmission. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
			:return: sci_tx_mode: 1| 2 | 3| 4"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:TXMode?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)
