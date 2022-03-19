from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:SCRambling:STATe \n
		Snippet: driver.source.bb.oneweb.uplink.ue.cell.pusch.scrambling.state.set(state = False, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Enables/disables scrambling for all PUSCH/PUACH allocations of the corresponding UE. \n
			:param state: 0| 1| OFF| ON
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(state)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:SCRambling:STATe {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:SCRambling:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.ue.cell.pusch.scrambling.state.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Enables/disables scrambling for all PUSCH/PUACH allocations of the corresponding UE. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: state: 0| 1| OFF| ON"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:SCRambling:STATe?')
		return Conversions.str_to_bool(response)
