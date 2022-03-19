from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TbIndex:
	"""TbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbIndex", core, parent)

	def set(self, nbiot_tb_size_idx: int, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:PUSCh:TBINdex \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.trans.pusch.tbIndex.set(nbiot_tb_size_idx = 1, userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Sets the transport block size index. \n
			:param nbiot_tb_size_idx: integer Range: 0 to 12
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
		"""
		param = Conversions.decimal_value_to_str(nbiot_tb_size_idx)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:PUSCh:TBINdex {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:PUSCh:TBINdex \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.niot.trans.pusch.tbIndex.get(userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Sets the transport block size index. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
			:return: nbiot_tb_size_idx: integer Range: 0 to 12"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:PUSCh:TBINdex?')
		return Conversions.str_to_int(response)
