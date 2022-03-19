from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowOffset:
	"""PowOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powOffset", core, parent)

	def set(self, power_offset: float, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:[CELL<CCIDX>]:REFSig:SRS:POWoffset \n
		Snippet: driver.source.bb.v5G.uplink.ue.cell.refsig.srs.powOffset.set(power_offset = 1.0, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param power_offset: No help available
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(power_offset)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:SRS:POWoffset {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:[CELL<CCIDX>]:REFSig:SRS:POWoffset \n
		Snippet: value: float = driver.source.bb.v5G.uplink.ue.cell.refsig.srs.powOffset.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: power_offset: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:SRS:POWoffset?')
		return Conversions.str_to_float(response)
