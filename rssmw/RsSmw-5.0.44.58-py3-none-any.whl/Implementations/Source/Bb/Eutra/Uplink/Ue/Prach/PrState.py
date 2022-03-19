from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrState:
	"""PrState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prState", core, parent)

	def set(self, state: bool, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:PRSTate \n
		Snippet: driver.source.bb.eutra.uplink.ue.prach.prState.set(state = False, userEquipment = repcap.UserEquipment.Default) \n
		Activates Power Ramping for the PRACH preamble. The start and the end of the preamble is cyclically extended and
		multiplied with a ramping function (sin^2) . \n
			:param state: 1| ON| 0| OFF
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.bool_to_str(state)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:PRSTate {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:PRSTate \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.ue.prach.prState.get(userEquipment = repcap.UserEquipment.Default) \n
		Activates Power Ramping for the PRACH preamble. The start and the end of the preamble is cyclically extended and
		multiplied with a ramping function (sin^2) . \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: state: 1| ON| 0| OFF"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:PRSTate?')
		return Conversions.str_to_bool(response)
