from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def set(self, idn: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ID \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.id.set(idn = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Specifies the ID in the CtrData field of the LL_PERIODIC_SYNC_IND PDU. \n
			:param idn: numeric
			:param bitcount: integer Range: 16 to 16
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('idn', idn, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ID {param}'.rstrip())

	# noinspection PyTypeChecker
	class IdStruct(StructBase):
		"""Response structure. Fields: \n
			- Idn: List[str]: numeric
			- Bitcount: int: integer Range: 16 to 16"""
		__meta_args_list = [
			ArgStruct('Idn', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: List[str] = None
			self.Bitcount: int = None

	def get(self) -> IdStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ID \n
		Snippet: value: IdStruct = driver.source.bb.btooth.econfiguration.pconfiguration.id.get() \n
		Specifies the ID in the CtrData field of the LL_PERIODIC_SYNC_IND PDU. \n
			:return: structure: for return value, see the help for IdStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ID?', self.__class__.IdStruct())
