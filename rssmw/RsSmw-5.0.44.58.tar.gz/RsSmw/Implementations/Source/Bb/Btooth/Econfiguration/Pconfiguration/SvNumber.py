from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SvNumber:
	"""SvNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("svNumber", core, parent)

	def set(self, sv_number: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SVNumber \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.svNumber.set(sv_number = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets a unique value for each implementation or revision of an implementation of the Bluetooth Controller. A 16-bit value
		is set. Note: This parameter is relevant for data frame configuration and for the packet type: LL_VERSION_IND. \n
			:param sv_number: numeric
			:param bitcount: integer Range: 16 to 16
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('sv_number', sv_number, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SVNumber {param}'.rstrip())

	# noinspection PyTypeChecker
	class SvNumberStruct(StructBase):
		"""Response structure. Fields: \n
			- Sv_Number: List[str]: numeric
			- Bitcount: int: integer Range: 16 to 16"""
		__meta_args_list = [
			ArgStruct('Sv_Number', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sv_Number: List[str] = None
			self.Bitcount: int = None

	def get(self) -> SvNumberStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SVNumber \n
		Snippet: value: SvNumberStruct = driver.source.bb.btooth.econfiguration.pconfiguration.svNumber.get() \n
		Sets a unique value for each implementation or revision of an implementation of the Bluetooth Controller. A 16-bit value
		is set. Note: This parameter is relevant for data frame configuration and for the packet type: LL_VERSION_IND. \n
			:return: structure: for return value, see the help for SvNumberStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SVNumber?', self.__class__.SvNumberStruct())
