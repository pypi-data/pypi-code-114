from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: enums.NumbersB, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:MSG:LENGth \n
		Snippet: driver.source.bb.tdscdma.up.cell.slot.prac.msg.length.set(length = enums.NumbersB._1, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the message length of the random access channel in subframes. \n
			:param length: 1| 2| 4
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.enum_scalar_to_str(length, enums.NumbersB)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:MSG:LENGth {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> enums.NumbersB:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:MSG:LENGth \n
		Snippet: value: enums.NumbersB = driver.source.bb.tdscdma.up.cell.slot.prac.msg.length.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the message length of the random access channel in subframes. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: length: 1| 2| 4"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:MSG:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersB)
