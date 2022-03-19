from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pgenerator:
	"""Pgenerator commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pgenerator", core, parent)

	@property
	def output(self):
		"""output commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:PGENerator:STATe \n
		Snippet: value: bool = driver.source.pgenerator.get_state() \n
		Enables the output of the video/sync signal. If the pulse generator is the current modulation source, activating the
		pulse modulation automatically activates the signal output and the pulse generator. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PGENerator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:PGENerator:STATe \n
		Snippet: driver.source.pgenerator.set_state(state = False) \n
		Enables the output of the video/sync signal. If the pulse generator is the current modulation source, activating the
		pulse modulation automatically activates the signal output and the pulse generator. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:PGENerator:STATe {param}')

	def clone(self) -> 'Pgenerator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pgenerator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
