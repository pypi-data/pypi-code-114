from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Asid:
	"""Asid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asid", core, parent)

	def set(self, asid: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ASID \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.asid.set(asid = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Specifies the 'Advertising Set ID' in hexadecimal format to be signaled within an extended header. \n
			:param asid: numeric
			:param bitcount: integer Range: 4 to 4
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('asid', asid, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ASID {param}'.rstrip())

	# noinspection PyTypeChecker
	class AsidStruct(StructBase):
		"""Response structure. Fields: \n
			- Asid: List[str]: numeric
			- Bitcount: int: integer Range: 4 to 4"""
		__meta_args_list = [
			ArgStruct('Asid', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Asid: List[str] = None
			self.Bitcount: int = None

	def get(self) -> AsidStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ASID \n
		Snippet: value: AsidStruct = driver.source.bb.btooth.econfiguration.pconfiguration.asid.get() \n
		Specifies the 'Advertising Set ID' in hexadecimal format to be signaled within an extended header. \n
			:return: structure: for return value, see the help for AsidStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ASID?', self.__class__.AsidStruct())
