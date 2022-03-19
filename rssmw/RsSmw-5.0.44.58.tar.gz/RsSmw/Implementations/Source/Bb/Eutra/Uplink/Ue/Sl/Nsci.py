from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsci:
	"""Nsci commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsci", core, parent)

	def set(self, sci_num_configs: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:NSCI \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.nsci.set(sci_num_configs = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of SCI (SL control information) configurations. \n
			:param sci_num_configs: integer Range: 0 to 49
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(sci_num_configs)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:NSCI {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:NSCI \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.nsci.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of SCI (SL control information) configurations. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: sci_num_configs: integer Range: 0 to 49"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:NSCI?')
		return Conversions.str_to_int(response)
