from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Galileo:
	"""Galileo commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("galileo", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	def get_ud_source(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:IMPort:GALileo:UDSource \n
		Snippet: value: bool = driver.source.bb.gnss.sv.importPy.galileo.get_ud_source() \n
		Enables loading the dedicated files as source for the navigation data. \n
			:return: use_diff_src_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:IMPort:GALileo:UDSource?')
		return Conversions.str_to_bool(response)

	def set_ud_source(self, use_diff_src_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:IMPort:GALileo:UDSource \n
		Snippet: driver.source.bb.gnss.sv.importPy.galileo.set_ud_source(use_diff_src_state = False) \n
		Enables loading the dedicated files as source for the navigation data. \n
			:param use_diff_src_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(use_diff_src_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:IMPort:GALileo:UDSource {param}')

	def clone(self) -> 'Galileo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Galileo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
