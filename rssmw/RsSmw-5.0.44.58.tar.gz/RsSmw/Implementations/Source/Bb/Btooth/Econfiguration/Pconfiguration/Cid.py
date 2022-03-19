from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cid:
	"""Cid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cid", core, parent)

	def set(self, cid: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CID \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.cid.set(cid = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the company identifier of the manufacturer of the Bluetooth Controller. A 16 bit value is set. Note: This parameter
		is relevant for data frame configuration and for the packet type LL_VERSION_IND. \n
			:param cid: numeric
			:param bitcount: integer Range: 16 to 16
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('cid', cid, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CID {param}'.rstrip())

	# noinspection PyTypeChecker
	class CidStruct(StructBase):
		"""Response structure. Fields: \n
			- Cid: List[str]: numeric
			- Bitcount: int: integer Range: 16 to 16"""
		__meta_args_list = [
			ArgStruct('Cid', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cid: List[str] = None
			self.Bitcount: int = None

	def get(self) -> CidStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CID \n
		Snippet: value: CidStruct = driver.source.bb.btooth.econfiguration.pconfiguration.cid.get() \n
		Sets the company identifier of the manufacturer of the Bluetooth Controller. A 16 bit value is set. Note: This parameter
		is relevant for data frame configuration and for the packet type LL_VERSION_IND. \n
			:return: structure: for return value, see the help for CidStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CID?', self.__class__.CidStruct())
