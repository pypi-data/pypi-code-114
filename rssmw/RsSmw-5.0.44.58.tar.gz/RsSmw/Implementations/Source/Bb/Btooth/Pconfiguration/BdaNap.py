from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BdaNap:
	"""BdaNap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bdaNap", core, parent)

	def set(self, bda_nap: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:BDANap \n
		Snippet: driver.source.bb.btooth.pconfiguration.bdaNap.set(bda_nap = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Enters the non-significant address part of Bluetooth Device Address. The length of NAP is 16 bits or 4 hexadecimal
		figures. \n
			:param bda_nap: numeric Range: #H0000 to #HFFFF
			:param bitcount: integer Range: 16 to 16
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('bda_nap', bda_nap, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:BDANap {param}'.rstrip())

	# noinspection PyTypeChecker
	class BdaNapStruct(StructBase):
		"""Response structure. Fields: \n
			- Bda_Nap: List[str]: numeric Range: #H0000 to #HFFFF
			- Bitcount: int: integer Range: 16 to 16"""
		__meta_args_list = [
			ArgStruct('Bda_Nap', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bda_Nap: List[str] = None
			self.Bitcount: int = None

	def get(self) -> BdaNapStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:BDANap \n
		Snippet: value: BdaNapStruct = driver.source.bb.btooth.pconfiguration.bdaNap.get() \n
		Enters the non-significant address part of Bluetooth Device Address. The length of NAP is 16 bits or 4 hexadecimal
		figures. \n
			:return: structure: for return value, see the help for BdaNapStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:BDANap?', self.__class__.BdaNapStruct())
