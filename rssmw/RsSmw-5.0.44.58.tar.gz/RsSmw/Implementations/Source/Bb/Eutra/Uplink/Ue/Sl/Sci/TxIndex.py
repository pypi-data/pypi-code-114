from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxIndex:
	"""TxIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txIndex", core, parent)

	def set(self, tx_index: bool, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:TXINdex \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.sci.txIndex.set(tx_index = False, userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Specifies the retransmission index field. \n
			:param tx_index: 1| ON| 0| OFF
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
		"""
		param = Conversions.bool_to_str(tx_index)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:TXINdex {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:TXINdex \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.ue.sl.sci.txIndex.get(userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Specifies the retransmission index field. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
			:return: tx_index: 1| ON| 0| OFF"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:TXINdex?')
		return Conversions.str_to_bool(response)
