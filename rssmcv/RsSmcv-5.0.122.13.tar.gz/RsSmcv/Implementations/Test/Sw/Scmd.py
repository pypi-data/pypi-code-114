from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scmd:
	"""Scmd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scmd", core, parent)

	def set(self, scmd: str, what_is_this: str) -> None:
		"""SCPI: TEST<HW>:SW:SCMD \n
		Snippet: driver.test.sw.scmd.set(scmd = '1', what_is_this = '1') \n
		No command help available \n
			:param scmd: No help available
			:param what_is_this: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('scmd', scmd, DataType.String), ArgSingle('what_is_this', what_is_this, DataType.String))
		self._core.io.write(f'TEST<HwInstance>:SW:SCMD {param}'.rstrip())

	# noinspection PyTypeChecker
	class ScmdStruct(StructBase):
		"""Response structure. Fields: \n
			- Scmd: str: No parameter help available
			- What_Is_This: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Scmd'),
			ArgStruct.scalar_str('What_Is_This')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scmd: str = None
			self.What_Is_This: str = None

	def get(self) -> ScmdStruct:
		"""SCPI: TEST<HW>:SW:SCMD \n
		Snippet: value: ScmdStruct = driver.test.sw.scmd.get() \n
		No command help available \n
			:return: structure: for return value, see the help for ScmdStruct structure arguments."""
		return self._core.io.query_struct(f'TEST<HwInstance>:SW:SCMD?', self.__class__.ScmdStruct())
