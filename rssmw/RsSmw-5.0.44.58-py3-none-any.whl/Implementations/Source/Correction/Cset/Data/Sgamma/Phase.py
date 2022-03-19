from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, phase_1: List[float], phase_n: float = None) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:SGAMma:PHASe \n
		Snippet: driver.source.correction.cset.data.sgamma.phase.set(phase_1 = [1.1, 2.2, 3.3], phase_n = 1.0) \n
		No command help available \n
			:param phase_1: No help available
			:param phase_n: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('phase_1', phase_1, DataType.FloatList, None), ArgSingle('phase_n', phase_n, DataType.Float, None, is_optional=True))
		self._core.io.write(f'SOURce<HwInstance>:CORRection:CSET:DATA:SGAMma:PHASe {param}'.rstrip())

	# noinspection PyTypeChecker
	class PhaseStruct(StructBase):
		"""Response structure. Fields: \n
			- Phase_1: List[float]: No parameter help available
			- Phase_N: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Phase_1', DataType.FloatList, None, False, True, 1),
			ArgStruct.scalar_float('Phase_N')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Phase_1: List[float] = None
			self.Phase_N: float = None

	def get(self) -> PhaseStruct:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:SGAMma:PHASe \n
		Snippet: value: PhaseStruct = driver.source.correction.cset.data.sgamma.phase.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PhaseStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:CORRection:CSET:DATA:SGAMma:PHASe?', self.__class__.PhaseStruct())

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:SGAMma:PHASe:POINts \n
		Snippet: value: int = driver.source.correction.cset.data.sgamma.phase.get_points() \n
		No command help available \n
			:return: points: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:CSET:DATA:SGAMma:PHASe:POINts?')
		return Conversions.str_to_int(response)
