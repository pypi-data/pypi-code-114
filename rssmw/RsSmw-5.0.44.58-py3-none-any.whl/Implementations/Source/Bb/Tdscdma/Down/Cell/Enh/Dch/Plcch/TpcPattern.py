from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpcPattern:
	"""TpcPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpcPattern", core, parent)

	def set(self, tpc_pattern: List[str], bitcount: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:PLCCh:TPCPattern \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.plcch.tpcPattern.set(tpc_pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, cell = repcap.Cell.Default) \n
		Sets the TPC pattern and the pattern length. \n
			:param tpc_pattern: numeric
			:param bitcount: integer Range: 1 to 21
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('tpc_pattern', tpc_pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:PLCCh:TPCPattern {param}'.rstrip())

	# noinspection PyTypeChecker
	class TpcPatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Tpc_Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 21"""
		__meta_args_list = [
			ArgStruct('Tpc_Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tpc_Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, cell=repcap.Cell.Default) -> TpcPatternStruct:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:PLCCh:TPCPattern \n
		Snippet: value: TpcPatternStruct = driver.source.bb.tdscdma.down.cell.enh.dch.plcch.tpcPattern.get(cell = repcap.Cell.Default) \n
		Sets the TPC pattern and the pattern length. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: structure: for return value, see the help for TpcPatternStruct structure arguments."""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:PLCCh:TPCPattern?', self.__class__.TpcPatternStruct())
