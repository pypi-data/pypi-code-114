from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Etbs:
	"""Etbs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("etbs", core, parent)

	def set(self, edt_tbs: enums.EutraNbiotEdtTranBlckSizeA, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:PUSCh:ETBS \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.trans.pusch.etbs.set(edt_tbs = enums.EutraNbiotEdtTranBlckSizeA._1000, userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Sets the maximum transport block size for early data transmission in UL. \n
			:param edt_tbs: 88| 328| 408| 504| 584| 680| 808| 936| 1000 Unit: bit
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
		"""
		param = Conversions.enum_scalar_to_str(edt_tbs, enums.EutraNbiotEdtTranBlckSizeA)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:PUSCh:ETBS {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> enums.EutraNbiotEdtTranBlckSizeA:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:PUSCh:ETBS \n
		Snippet: value: enums.EutraNbiotEdtTranBlckSizeA = driver.source.bb.eutra.uplink.ue.niot.trans.pusch.etbs.get(userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Sets the maximum transport block size for early data transmission in UL. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
			:return: edt_tbs: 88| 328| 408| 504| 584| 680| 808| 936| 1000 Unit: bit"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:PUSCh:ETBS?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotEdtTranBlckSizeA)
