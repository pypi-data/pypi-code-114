from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vnumber:
	"""Vnumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vnumber", core, parent)

	def set(self, vnumber: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:VNUMber \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.vnumber.set(vnumber = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the company identifier of the manufacturer of the Bluetooth controller. An 8-bit value is set. Note: This parameter
		is relevant for data frame configuration and for the packet type LL_VERSION_IND. \n
			:param vnumber: numeric
			:param bitcount: integer Range: 8 to 8
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('vnumber', vnumber, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:VNUMber {param}'.rstrip())

	# noinspection PyTypeChecker
	class VnumberStruct(StructBase):
		"""Response structure. Fields: \n
			- Vnumber: List[str]: numeric
			- Bitcount: int: integer Range: 8 to 8"""
		__meta_args_list = [
			ArgStruct('Vnumber', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Vnumber: List[str] = None
			self.Bitcount: int = None

	def get(self) -> VnumberStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:VNUMber \n
		Snippet: value: VnumberStruct = driver.source.bb.btooth.econfiguration.pconfiguration.vnumber.get() \n
		Sets the company identifier of the manufacturer of the Bluetooth controller. An 8-bit value is set. Note: This parameter
		is relevant for data frame configuration and for the packet type LL_VERSION_IND. \n
			:return: structure: for return value, see the help for VnumberStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:VNUMber?', self.__class__.VnumberStruct())
