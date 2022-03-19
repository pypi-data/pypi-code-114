from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DacRestart:
	"""DacRestart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dacRestart", core, parent)

	def set(self, restart_state: bool, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:DACRestart \n
		Snippet: driver.source.bb.oneweb.uplink.ue.dacRestart.set(restart_state = False, userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param restart_state: No help available
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.bool_to_str(restart_state)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:DACRestart {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:DACRestart \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.ue.dacRestart.get(userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: restart_state: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:DACRestart?')
		return Conversions.str_to_bool(response)
