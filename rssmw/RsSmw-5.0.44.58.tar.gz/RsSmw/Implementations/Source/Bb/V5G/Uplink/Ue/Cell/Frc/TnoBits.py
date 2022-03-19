from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TnoBits:
	"""TnoBits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tnoBits", core, parent)

	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:[CELL<CCIDX>]:FRC:TNOBits \n
		Snippet: value: int = driver.source.bb.v5G.uplink.ue.cell.frc.tnoBits.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: total_bit_count: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:FRC:TNOBits?')
		return Conversions.str_to_int(response)
