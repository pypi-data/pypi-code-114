from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aaddress:
	"""Aaddress commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aaddress", core, parent)

	def set(self, aaddress: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AADDress \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.aaddress.set(aaddress = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the access address of the link layer connection (32-bit string) . \n
			:param aaddress: numeric
			:param bitcount: integer Range: 32 to 32
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('aaddress', aaddress, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AADDress {param}'.rstrip())

	# noinspection PyTypeChecker
	class AaddressStruct(StructBase):
		"""Response structure. Fields: \n
			- Aaddress: List[str]: numeric
			- Bitcount: int: integer Range: 32 to 32"""
		__meta_args_list = [
			ArgStruct('Aaddress', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aaddress: List[str] = None
			self.Bitcount: int = None

	def get(self) -> AaddressStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AADDress \n
		Snippet: value: AaddressStruct = driver.source.bb.btooth.econfiguration.pconfiguration.aaddress.get() \n
		Sets the access address of the link layer connection (32-bit string) . \n
			:return: structure: for return value, see the help for AaddressStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AADDress?', self.__class__.AaddressStruct())
