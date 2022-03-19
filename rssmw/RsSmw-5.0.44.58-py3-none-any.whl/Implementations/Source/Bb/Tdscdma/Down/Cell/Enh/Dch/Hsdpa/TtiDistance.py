from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TtiDistance:
	"""TtiDistance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttiDistance", core, parent)

	def set(self, tti_distance: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:TTIDistance \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.ttiDistance.set(tti_distance = 1, cell = repcap.Cell.Default) \n
		Sets the inter-TTI distance. The inter-TTI is the distance between two packets in HSDPA packet mode and determines
		whether data is sent each TTI or there is a DTX transmission in some of the TTIs. An inter-TTI distance of 1 means
		continuous generation. \n
			:param tti_distance: integer Range: 1 to 8
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(tti_distance)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:TTIDistance {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:TTIDistance \n
		Snippet: value: int = driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.ttiDistance.get(cell = repcap.Cell.Default) \n
		Sets the inter-TTI distance. The inter-TTI is the distance between two packets in HSDPA packet mode and determines
		whether data is sent each TTI or there is a DTX transmission in some of the TTIs. An inter-TTI distance of 1 means
		continuous generation. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: tti_distance: integer Range: 1 to 8"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:TTIDistance?')
		return Conversions.str_to_int(response)
