from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Utilities import trim_str_response
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, dselect: str, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:DCCH:DATA:DSELect \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.dcch.data.dselect.set(dselect = '1', cell = repcap.Cell.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. For general information on
		file handling in the default and in a specific directory, see section 'MMEMory Subsystem' in the R&S SMWuser manual. For
		the traffic channels, this value is specific for the selected radio configuration. \n
			:param dselect: string Filename incl. file extension or complete file path
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.value_to_quoted_str(dselect)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:DCCH:DATA:DSELect {param}')

	def get(self, cell=repcap.Cell.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:DCCH:DATA:DSELect \n
		Snippet: value: str = driver.source.bb.tdscdma.up.cell.enh.dch.dcch.data.dselect.get(cell = repcap.Cell.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. For general information on
		file handling in the default and in a specific directory, see section 'MMEMory Subsystem' in the R&S SMWuser manual. For
		the traffic channels, this value is specific for the selected radio configuration. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: dselect: string Filename incl. file extension or complete file path"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:DCCH:DATA:DSELect?')
		return trim_str_response(response)
