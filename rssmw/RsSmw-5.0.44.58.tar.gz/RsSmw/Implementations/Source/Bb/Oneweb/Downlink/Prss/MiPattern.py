from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MiPattern:
	"""MiPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("miPattern", core, parent)

	def set(self, prs_muting_info: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PRSS:MIPattern \n
		Snippet: driver.source.bb.oneweb.downlink.prss.miPattern.set(prs_muting_info = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		No command help available \n
			:param prs_muting_info: No help available
			:param bitcount: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('prs_muting_info', prs_muting_info, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PRSS:MIPattern {param}'.rstrip())

	# noinspection PyTypeChecker
	class MiPatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Prs_Muting_Info: List[str]: No parameter help available
			- Bitcount: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Prs_Muting_Info', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Prs_Muting_Info: List[str] = None
			self.Bitcount: int = None

	def get(self) -> MiPatternStruct:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PRSS:MIPattern \n
		Snippet: value: MiPatternStruct = driver.source.bb.oneweb.downlink.prss.miPattern.get() \n
		No command help available \n
			:return: structure: for return value, see the help for MiPatternStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:ONEWeb:DL:PRSS:MIPattern?', self.__class__.MiPatternStruct())
