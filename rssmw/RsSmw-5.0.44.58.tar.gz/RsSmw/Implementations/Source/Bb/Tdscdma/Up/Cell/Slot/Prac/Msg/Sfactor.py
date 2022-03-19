from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfactor:
	"""Sfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfactor", core, parent)

	def set(self, sfactor: enums.TdscdmaSpreadFactor, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:MSG:SFACtor \n
		Snippet: driver.source.bb.tdscdma.up.cell.slot.prac.msg.sfactor.set(sfactor = enums.TdscdmaSpreadFactor._1, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the spreading factor for the PRACH. \n
			:param sfactor: 4| 8| 16
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.enum_scalar_to_str(sfactor, enums.TdscdmaSpreadFactor)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:MSG:SFACtor {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> enums.TdscdmaSpreadFactor:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:MSG:SFACtor \n
		Snippet: value: enums.TdscdmaSpreadFactor = driver.source.bb.tdscdma.up.cell.slot.prac.msg.sfactor.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the spreading factor for the PRACH. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: sfactor: 4| 8| 16"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:MSG:SFACtor?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaSpreadFactor)
