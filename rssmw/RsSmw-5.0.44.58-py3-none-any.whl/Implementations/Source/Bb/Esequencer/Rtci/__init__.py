from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtci:
	"""Rtci commands group definition. 24 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtci", core, parent)

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
		"""sequencer commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._cmd_group)
		return self._sequencer

	# noinspection PyTypeChecker
	def get_pdw_format(self) -> enums.ExtSeqPdwVariant:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:PDWFormat \n
		Snippet: value: enums.ExtSeqPdwVariant = driver.source.bb.esequencer.rtci.get_pdw_format() \n
		Selects the PDW format. \n
			:return: format_py: BASic| EXPert
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:RTCI:PDWFormat?')
		return Conversions.str_to_scalar_enum(response, enums.ExtSeqPdwVariant)

	def set_pdw_format(self, format_py: enums.ExtSeqPdwVariant) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:PDWFormat \n
		Snippet: driver.source.bb.esequencer.rtci.set_pdw_format(format_py = enums.ExtSeqPdwVariant.BASic) \n
		Selects the PDW format. \n
			:param format_py: BASic| EXPert
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.ExtSeqPdwVariant)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:PDWFormat {param}')

	def clone(self) -> 'Rtci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rtci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
