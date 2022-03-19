from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prtt:
	"""Prtt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prtt", core, parent)

	def set(self, transition_time: float, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:PRACh:PRTT \n
		Snippet: driver.source.bb.v5G.uplink.ue.prach.prtt.set(transition_time = 1.0, userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param transition_time: No help available
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(transition_time)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:PRACh:PRTT {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:PRACh:PRTT \n
		Snippet: value: float = driver.source.bb.v5G.uplink.ue.prach.prtt.get(userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: transition_time: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:PRACh:PRTT?')
		return Conversions.str_to_float(response)
