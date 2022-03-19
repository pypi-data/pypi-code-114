from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrFormat:
	"""PrFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prFormat", core, parent)

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:PRACh:PRFormat \n
		Snippet: value: int = driver.source.bb.v5G.uplink.ue.prach.prFormat.get(userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: prea_format: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:PRACh:PRFormat?')
		return Conversions.str_to_int(response)
