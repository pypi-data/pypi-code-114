from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scch:
	"""Scch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scch", core, parent)

	def set(self, scch: bool, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:SCCH \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.scch.set(scch = False, cell = repcap.Cell.Default) \n
		Enables/disables the HS-SCCH. \n
			:param scch: 1| ON| 0| OFF
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(scch)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:SCCH {param}')

	def get(self, cell=repcap.Cell.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:SCCH \n
		Snippet: value: bool = driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.scch.get(cell = repcap.Cell.Default) \n
		Enables/disables the HS-SCCH. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: scch: 1| ON| 0| OFF"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:SCCH?')
		return Conversions.str_to_bool(response)
