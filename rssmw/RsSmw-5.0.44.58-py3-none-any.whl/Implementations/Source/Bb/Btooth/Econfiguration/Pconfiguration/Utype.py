from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Utype:
	"""Utype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utype", core, parent)

	def set(self, utype: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:UTYPe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.utype.set(utype = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Enables that an invalid control packet is indicated. The CtrType field indicates the value of the LL control packet that
		caused the transmission of this packet. \n
			:param utype: numeric
			:param bitcount: integer Range: 8 to 8
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('utype', utype, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:UTYPe {param}'.rstrip())

	# noinspection PyTypeChecker
	class UtypeStruct(StructBase):
		"""Response structure. Fields: \n
			- Utype: List[str]: numeric
			- Bitcount: int: integer Range: 8 to 8"""
		__meta_args_list = [
			ArgStruct('Utype', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Utype: List[str] = None
			self.Bitcount: int = None

	def get(self) -> UtypeStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:UTYPe \n
		Snippet: value: UtypeStruct = driver.source.bb.btooth.econfiguration.pconfiguration.utype.get() \n
		Enables that an invalid control packet is indicated. The CtrType field indicates the value of the LL control packet that
		caused the transmission of this packet. \n
			:return: structure: for return value, see the help for UtypeStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:UTYPe?', self.__class__.UtypeStruct())
