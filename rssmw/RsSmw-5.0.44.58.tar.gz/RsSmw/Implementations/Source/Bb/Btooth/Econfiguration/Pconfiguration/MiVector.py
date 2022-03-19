from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MiVector:
	"""MiVector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("miVector", core, parent)

	def set(self, mi_vector: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MIVector \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.miVector.set(mi_vector = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the portion of Central or the portion of the Peripheral of the initialization vector (IVm/IVs) . \n
			:param mi_vector: numeric
			:param bitcount: integer Range: 32 to 32
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('mi_vector', mi_vector, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MIVector {param}'.rstrip())

	# noinspection PyTypeChecker
	class MiVectorStruct(StructBase):
		"""Response structure. Fields: \n
			- Mi_Vector: List[str]: No parameter help available
			- Bitcount: int: integer Range: 32 to 32"""
		__meta_args_list = [
			ArgStruct('Mi_Vector', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mi_Vector: List[str] = None
			self.Bitcount: int = None

	def get(self) -> MiVectorStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MIVector \n
		Snippet: value: MiVectorStruct = driver.source.bb.btooth.econfiguration.pconfiguration.miVector.get() \n
		Sets the portion of Central or the portion of the Peripheral of the initialization vector (IVm/IVs) . \n
			:return: structure: for return value, see the help for MiVectorStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MIVector?', self.__class__.MiVectorStruct())
