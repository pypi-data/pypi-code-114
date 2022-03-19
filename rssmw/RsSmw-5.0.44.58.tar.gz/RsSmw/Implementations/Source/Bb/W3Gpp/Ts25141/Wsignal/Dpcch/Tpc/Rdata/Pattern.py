from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:PATTern \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.rdata.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Determines the bit pattern for the PATTern data source selection. \n
			:param pattern: numeric
			:param bitcount: integer Range: 1 to 64
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 64"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self) -> PatternStruct:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.rdata.pattern.get() \n
		Determines the bit pattern for the PATTern data source selection. \n
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:PATTern?', self.__class__.PatternStruct())
