from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmAttribute:
	"""RmAttribute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmAttribute", core, parent)

	def set(self, rm_attribute: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:DCCH:RMATtribute \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.dcch.rmAttribute.set(rm_attribute = 1, cell = repcap.Cell.Default) \n
		Sets the rate matching. \n
			:param rm_attribute: integer Range: 16 to 1024
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(rm_attribute)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:DCCH:RMATtribute {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:DCCH:RMATtribute \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.enh.dch.dcch.rmAttribute.get(cell = repcap.Cell.Default) \n
		Sets the rate matching. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: rm_attribute: integer Range: 16 to 1024"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:DCCH:RMATtribute?')
		return Conversions.str_to_int(response)
