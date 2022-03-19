from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EtrSize:
	"""EtrSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("etrSize", core, parent)

	def set(self, edt_tran_block_size: enums.EutraNbiotEdtTranBlckSizeB, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:PUSCh:ETRSize \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.trans.pusch.etrSize.set(edt_tran_block_size = enums.EutraNbiotEdtTranBlckSizeB._1000, userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Specifies the used transport block size for early data transmission in UL. \n
			:param edt_tran_block_size: 88| 328| 408| 456| 504| 536| 584| 680| 712| 776| 808| 936| 1000 Unit: bit
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
		"""
		param = Conversions.enum_scalar_to_str(edt_tran_block_size, enums.EutraNbiotEdtTranBlckSizeB)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:PUSCh:ETRSize {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> enums.EutraNbiotEdtTranBlckSizeB:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:PUSCh:ETRSize \n
		Snippet: value: enums.EutraNbiotEdtTranBlckSizeB = driver.source.bb.eutra.uplink.ue.niot.trans.pusch.etrSize.get(userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Specifies the used transport block size for early data transmission in UL. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
			:return: edt_tran_block_size: 88| 328| 408| 456| 504| 536| 584| 680| 712| 776| 808| 936| 1000 Unit: bit"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:PUSCh:ETRSize?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotEdtTranBlckSizeB)
