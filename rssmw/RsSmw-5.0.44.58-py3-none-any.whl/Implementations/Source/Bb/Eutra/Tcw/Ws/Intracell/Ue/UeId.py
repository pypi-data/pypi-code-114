from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeId:
	"""UeId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueId", core, parent)

	def set(self, intracell_ueid: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:INTRacell:UE<CH>:UEID \n
		Snippet: driver.source.bb.eutra.tcw.ws.intracell.ue.ueId.set(intracell_ueid = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the intra cell UE ID/n_RNTI for the wanted signal UE. \n
			:param intracell_ueid: integer Range: 0 to 65535
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(intracell_ueid)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:INTRacell:UE{userEquipment_cmd_val}:UEID {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:INTRacell:UE<CH>:UEID \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.intracell.ue.ueId.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the intra cell UE ID/n_RNTI for the wanted signal UE. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: intracell_ueid: integer Range: 0 to 65535"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:INTRacell:UE{userEquipment_cmd_val}:UEID?')
		return Conversions.str_to_int(response)
