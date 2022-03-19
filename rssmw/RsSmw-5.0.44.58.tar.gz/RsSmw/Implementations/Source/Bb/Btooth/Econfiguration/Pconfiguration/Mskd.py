from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mskd:
	"""Mskd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mskd", core, parent)

	def set(self, mskd: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MSKD \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.mskd.set(mskd = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the portion of Central or the portion of the Peripheral of the session key diversifier (SKDm/SKDs) . \n
			:param mskd: numeric
			:param bitcount: integer Range: 64 to 64
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('mskd', mskd, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MSKD {param}'.rstrip())

	# noinspection PyTypeChecker
	class MskdStruct(StructBase):
		"""Response structure. Fields: \n
			- Mskd: List[str]: No parameter help available
			- Bitcount: int: integer Range: 64 to 64"""
		__meta_args_list = [
			ArgStruct('Mskd', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mskd: List[str] = None
			self.Bitcount: int = None

	def get(self) -> MskdStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MSKD \n
		Snippet: value: MskdStruct = driver.source.bb.btooth.econfiguration.pconfiguration.mskd.get() \n
		Sets the portion of Central or the portion of the Peripheral of the session key diversifier (SKDm/SKDs) . \n
			:return: structure: for return value, see the help for MskdStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MSKD?', self.__class__.MskdStruct())
