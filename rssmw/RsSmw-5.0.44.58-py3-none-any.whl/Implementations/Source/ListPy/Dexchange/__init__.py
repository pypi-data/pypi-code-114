from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dexchange:
	"""Dexchange commands group definition. 8 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dexchange", core, parent)

	@property
	def afile(self):
		"""afile commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_afile'):
			from .Afile import Afile
			self._afile = Afile(self._core, self._cmd_group)
		return self._afile

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DexchMode:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:MODE \n
		Snippet: value: enums.DexchMode = driver.source.listPy.dexchange.get_mode() \n
		Determines the import or export of a list. Specify the source or destination file with the command
		[:SOURce<hw>]:LIST:DEXChange:SELect. \n
			:return: mode: IMPort| EXPort
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:DEXChange:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DexchMode)

	def set_mode(self, mode: enums.DexchMode) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:MODE \n
		Snippet: driver.source.listPy.dexchange.set_mode(mode = enums.DexchMode.EXPort) \n
		Determines the import or export of a list. Specify the source or destination file with the command
		[:SOURce<hw>]:LIST:DEXChange:SELect. \n
			:param mode: IMPort| EXPort
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DexchMode)
		self._core.io.write(f'SOURce<HwInstance>:LIST:DEXChange:MODE {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:SELect \n
		Snippet: value: str = driver.source.listPy.dexchange.get_select() \n
		Selects the ASCII file for import or export, containing a list. \n
			:return: filename: string Filename or complete file path; file extension can be omitted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:DEXChange:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:SELect \n
		Snippet: driver.source.listPy.dexchange.set_select(filename = '1') \n
		Selects the ASCII file for import or export, containing a list. \n
			:param filename: string Filename or complete file path; file extension can be omitted.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:LIST:DEXChange:SELect {param}')

	def clone(self) -> 'Dexchange':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dexchange(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
