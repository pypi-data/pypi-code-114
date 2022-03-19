from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], bitcount: int, cellNull=repcap.CellNull.Nr0, ssPbchNull=repcap.SsPbchNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SSPBch<ST0>:POSition:PATTern \n
		Snippet: driver.source.bb.nr5G.node.cell.sspbch.position.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, cellNull = repcap.CellNull.Nr0, ssPbchNull = repcap.SsPbchNull.Default) \n
		Sets a bit pattern as a data source. \n
			:param pattern: 64 bits An internally generated sequence according to a bit pattern. Each bit applies to one SS/PBCH block. 1: SS/PBCH block is present 0: SS/PBCH transmission is suppressed.
			:param bitcount: integer Range: 4 to 64
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param ssPbchNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sspbch')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		ssPbchNull_cmd_val = self._cmd_group.get_repcap_cmd_value(ssPbchNull, repcap.SsPbchNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SSPBch{ssPbchNull_cmd_val}:POSition:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: 64 bits An internally generated sequence according to a bit pattern. Each bit applies to one SS/PBCH block. 1: SS/PBCH block is present 0: SS/PBCH transmission is suppressed.
			- Bitcount: int: integer Range: 4 to 64"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, cellNull=repcap.CellNull.Nr0, ssPbchNull=repcap.SsPbchNull.Default) -> PatternStruct:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SSPBch<ST0>:POSition:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.nr5G.node.cell.sspbch.position.pattern.get(cellNull = repcap.CellNull.Nr0, ssPbchNull = repcap.SsPbchNull.Default) \n
		Sets a bit pattern as a data source. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param ssPbchNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sspbch')
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		ssPbchNull_cmd_val = self._cmd_group.get_repcap_cmd_value(ssPbchNull, repcap.SsPbchNull)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SSPBch{ssPbchNull_cmd_val}:POSition:PATTern?', self.__class__.PatternStruct())
