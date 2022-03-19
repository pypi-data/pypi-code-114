from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adid:
	"""Adid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adid", core, parent)

	def set(self, adid: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ADID \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.adid.set(adid = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Specifies 'Advertising Data ID' in hexadecimal format to be signaled within an extended header. \n
			:param adid: numeric
			:param bitcount: integer Range: 12 to 12
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('adid', adid, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ADID {param}'.rstrip())

	# noinspection PyTypeChecker
	class AdidStruct(StructBase):
		"""Response structure. Fields: \n
			- Adid: List[str]: numeric
			- Bitcount: int: integer Range: 12 to 12"""
		__meta_args_list = [
			ArgStruct('Adid', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Adid: List[str] = None
			self.Bitcount: int = None

	def get(self) -> AdidStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ADID \n
		Snippet: value: AdidStruct = driver.source.bb.btooth.econfiguration.pconfiguration.adid.get() \n
		Specifies 'Advertising Data ID' in hexadecimal format to be signaled within an extended header. \n
			:return: structure: for return value, see the help for AdidStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ADID?', self.__class__.AdidStruct())
