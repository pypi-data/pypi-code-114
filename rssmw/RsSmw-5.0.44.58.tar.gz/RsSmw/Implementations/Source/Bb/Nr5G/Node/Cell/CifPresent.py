from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CifPresent:
	"""CifPresent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cifPresent", core, parent)

	def set(self, cif_present: bool, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:CIFPresent \n
		Snippet: driver.source.bb.nr5G.node.cell.cifPresent.set(cif_present = False, cellNull = repcap.CellNull.Nr0) \n
		Defines whether the carrier indicator field (CIF) is included in the PDCCH DCI formats transmitted from the corresponding
		cell. The CIF is present in each DCI format and identifies the component carrier that carries the PDSCH or PUSCH for the
		particular PDCCH in the cross-carrier approach. According to the 5G NR specification, cross-carrier scheduling is enabled
		by higher-level signaling. To simulate a cross-carrier scheduling in this implementation, enable the 'Node > Carriers >
		CIF Present' per each cell. \n
			:param cif_present: 1| ON| 0| OFF
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.bool_to_str(cif_present)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:CIFPresent {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:CIFPresent \n
		Snippet: value: bool = driver.source.bb.nr5G.node.cell.cifPresent.get(cellNull = repcap.CellNull.Nr0) \n
		Defines whether the carrier indicator field (CIF) is included in the PDCCH DCI formats transmitted from the corresponding
		cell. The CIF is present in each DCI format and identifies the component carrier that carries the PDSCH or PUSCH for the
		particular PDCCH in the cross-carrier approach. According to the 5G NR specification, cross-carrier scheduling is enabled
		by higher-level signaling. To simulate a cross-carrier scheduling in this implementation, enable the 'Node > Carriers >
		CIF Present' per each cell. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: cif_present: 1| ON| 0| OFF"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:CIFPresent?')
		return Conversions.str_to_bool(response)
