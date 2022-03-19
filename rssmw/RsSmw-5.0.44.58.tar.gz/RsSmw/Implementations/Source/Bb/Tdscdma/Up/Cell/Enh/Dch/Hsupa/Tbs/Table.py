from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	def set(self, table: enums.TdscdmaEnhHsTbsTableUp, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:TBS:TABLe \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.tbs.table.set(table = enums.TdscdmaEnhHsTbsTableUp.C1TO2, cell = repcap.Cell.Default) \n
		Sets the transport block size table, according to the specification 3GPP TS 25.321, annex BC. \n
			:param table: C1TO2| C3TO6
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(table, enums.TdscdmaEnhHsTbsTableUp)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:TBS:TABLe {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.TdscdmaEnhHsTbsTableUp:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:TBS:TABLe \n
		Snippet: value: enums.TdscdmaEnhHsTbsTableUp = driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.tbs.table.get(cell = repcap.Cell.Default) \n
		Sets the transport block size table, according to the specification 3GPP TS 25.321, annex BC. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: table: C1TO2| C3TO6"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:TBS:TABLe?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaEnhHsTbsTableUp)
