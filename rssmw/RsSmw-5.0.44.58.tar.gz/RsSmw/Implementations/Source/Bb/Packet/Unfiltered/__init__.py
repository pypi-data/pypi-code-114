from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unfiltered:
	"""Unfiltered commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unfiltered", core, parent)

	@property
	def nibble(self):
		"""nibble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nibble'):
			from .Nibble import Nibble
			self._nibble = Nibble(self._core, self._cmd_group)
		return self._nibble

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PACKet:UNFiltered:STATe \n
		Snippet: value: bool = driver.source.bb.packet.unfiltered.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PACKet:UNFiltered:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PACKet:UNFiltered:STATe \n
		Snippet: driver.source.bb.packet.unfiltered.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:PACKet:UNFiltered:STATe {param}')

	def clone(self) -> 'Unfiltered':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Unfiltered(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
