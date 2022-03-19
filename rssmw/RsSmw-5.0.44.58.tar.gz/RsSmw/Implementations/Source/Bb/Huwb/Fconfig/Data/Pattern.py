from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, dpattern: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DATA:PATTern \n
		Snippet: driver.source.bb.huwb.fconfig.data.pattern.set(dpattern = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the data pattern, if pattern is selected as the data source. See [:SOURce<hw>]:BB:HUWB:FCONfig:DATA. \n
			:param dpattern: numeric
			:param bitcount: integer Range: 1 to 64
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('dpattern', dpattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:DATA:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Dpattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 64"""
		__meta_args_list = [
			ArgStruct('Dpattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dpattern: List[str] = None
			self.Bitcount: int = None

	def get(self) -> PatternStruct:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DATA:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.huwb.fconfig.data.pattern.get() \n
		Sets the data pattern, if pattern is selected as the data source. See [:SOURce<hw>]:BB:HUWB:FCONfig:DATA. \n
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:HUWB:FCONfig:DATA:PATTern?', self.__class__.PatternStruct())
