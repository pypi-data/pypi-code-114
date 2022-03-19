from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Asequencing:
	"""Asequencing commands group definition. 17 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asequencing", core, parent)

	@property
	def qsfp(self):
		"""qsfp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qsfp'):
			from .Qsfp import Qsfp
			self._qsfp = Qsfp(self._core, self._cmd_group)
		return self._qsfp

	@property
	def wave(self):
		"""wave commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wave'):
			from .Wave import Wave
			self._wave = Wave(self._core, self._cmd_group)
		return self._wave

	@property
	def wlist(self):
		"""wlist commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_wlist'):
			from .Wlist import Wlist
			self._wlist = Wlist(self._core, self._cmd_group)
		return self._wlist

	@property
	def sequencer(self):
		"""sequencer commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._cmd_group)
		return self._sequencer

	# noinspection PyTypeChecker
	def get_omode(self) -> enums.ExtSeqAdwMode:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:OMODe \n
		Snippet: value: enums.ExtSeqAdwMode = driver.source.bb.esequencer.asequencing.get_omode() \n
		No command help available \n
			:return: operation_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:OMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ExtSeqAdwMode)

	def set_omode(self, operation_mode: enums.ExtSeqAdwMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:OMODe \n
		Snippet: driver.source.bb.esequencer.asequencing.set_omode(operation_mode = enums.ExtSeqAdwMode.DETerministic) \n
		No command help available \n
			:param operation_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(operation_mode, enums.ExtSeqAdwMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:OMODe {param}')

	def clone(self) -> 'Asequencing':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Asequencing(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
