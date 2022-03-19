from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Matrix:
	"""Matrix commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("matrix", core, parent)

	@property
	def row(self):
		"""row commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:STATe \n
		Snippet: value: bool = driver.source.fsimulator.mimo.antenna.inverse.matrix.get_state() \n
		Applies the inverse channel matrix to compensate for chamber effects. To set the matrix values, use the commands
		[:SOURce<hw>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW<st>:COLumn<ch>:REAL and
		[:SOURce<hw>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW<st>:COLumn<ch>:IMAGin. \n
			:return: ant_mod_inv_matrix: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:INVerse:MATRix:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, ant_mod_inv_matrix: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:STATe \n
		Snippet: driver.source.fsimulator.mimo.antenna.inverse.matrix.set_state(ant_mod_inv_matrix = False) \n
		Applies the inverse channel matrix to compensate for chamber effects. To set the matrix values, use the commands
		[:SOURce<hw>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW<st>:COLumn<ch>:REAL and
		[:SOURce<hw>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW<st>:COLumn<ch>:IMAGin. \n
			:param ant_mod_inv_matrix: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ant_mod_inv_matrix)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:INVerse:MATRix:STATe {param}')

	def clone(self) -> 'Matrix':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Matrix(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
