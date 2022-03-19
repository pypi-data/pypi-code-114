from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:FRC:STATe \n
		Snippet: driver.source.bb.eutra.uplink.ue.cell.frc.state.set(state = False, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Enables/disables FRC configuration. Enabling FRC configuration sets some parameters to their predefined values, i.e.
		several parameters are displayed as read-only. Reconfiguration of the values of this parameters is possible only after
		disabling the FRC configuration. The FRC State is disabled and cannot be enabled, if a user defined cyclic prefix
		(BB:EUTR:UL:CPC USER) is selected. \n
			:param state: 1| ON| 0| OFF
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(state)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:FRC:STATe {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:FRC:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.ue.cell.frc.state.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Enables/disables FRC configuration. Enabling FRC configuration sets some parameters to their predefined values, i.e.
		several parameters are displayed as read-only. Reconfiguration of the values of this parameters is possible only after
		disabling the FRC configuration. The FRC State is disabled and cannot be enabled, if a user defined cyclic prefix
		(BB:EUTR:UL:CPC USER) is selected. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: state: 1| ON| 0| OFF"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:FRC:STATe?')
		return Conversions.str_to_bool(response)
