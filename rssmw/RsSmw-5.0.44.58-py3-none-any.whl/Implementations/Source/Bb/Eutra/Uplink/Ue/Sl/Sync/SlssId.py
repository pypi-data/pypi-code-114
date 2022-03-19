from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlssId:
	"""SlssId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slssId", core, parent)

	def set(self, slss_id: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SYNC:SLSSid \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.sync.slssId.set(slss_id = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the sidelink synchronization signal ID. \n
			:param slss_id: integer Range: 0 to 335
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(slss_id)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SYNC:SLSSid {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SYNC:SLSSid \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.sync.slssId.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the sidelink synchronization signal ID. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: slss_id: integer Range: 0 to 335"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SYNC:SLSSid?')
		return Conversions.str_to_int(response)
