from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rvector:
	"""Rvector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvector", core, parent)

	def set(self, rvector: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:RVECtor \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.rvector.set(rvector = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the random vector of the Central for device identification. The parameter is an initialization vector provided by
		the Host in the HCI_ULP_Start_Encryption command. \n
			:param rvector: numeric
			:param bitcount: integer Range: 64 to 64
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('rvector', rvector, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:RVECtor {param}'.rstrip())

	# noinspection PyTypeChecker
	class RvectorStruct(StructBase):
		"""Response structure. Fields: \n
			- Rvector: List[str]: numeric
			- Bitcount: int: integer Range: 64 to 64"""
		__meta_args_list = [
			ArgStruct('Rvector', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rvector: List[str] = None
			self.Bitcount: int = None

	def get(self) -> RvectorStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:RVECtor \n
		Snippet: value: RvectorStruct = driver.source.bb.btooth.econfiguration.pconfiguration.rvector.get() \n
		Sets the random vector of the Central for device identification. The parameter is an initialization vector provided by
		the Host in the HCI_ULP_Start_Encryption command. \n
			:return: structure: for return value, see the help for RvectorStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:RVECtor?', self.__class__.RvectorStruct())
