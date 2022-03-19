from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spoint:
	"""Spoint commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spoint", core, parent)

	def set(self, spoint: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SPOint \n
		Snippet: driver.source.bb.tdscdma.down.cell.spoint.set(spoint = 1, cell = repcap.Cell.Default) \n
		Sets the switching point between the uplink slots and the downlink slots in the frame. \n
			:param spoint: integer Range: 1 to 6
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(spoint)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SPOint {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:SPOint \n
		Snippet: value: int = driver.source.bb.tdscdma.down.cell.spoint.get(cell = repcap.Cell.Default) \n
		Sets the switching point between the uplink slots and the downlink slots in the frame. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: spoint: integer Range: 1 to 6"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:SPOint?')
		return Conversions.str_to_int(response)
