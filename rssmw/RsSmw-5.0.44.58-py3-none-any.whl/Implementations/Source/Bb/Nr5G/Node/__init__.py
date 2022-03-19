from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Node:
	"""Node commands group definition. 140 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("node", core, parent)

	@property
	def carMapping(self):
		"""carMapping commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_carMapping'):
			from .CarMapping import CarMapping
			self._carMapping = CarMapping(self._core, self._cmd_group)
		return self._carMapping

	@property
	def cc(self):
		"""cc commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def cell(self):
		"""cell commands group. 24 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import Cell
			self._cell = Cell(self._core, self._cmd_group)
		return self._cell

	@property
	def rfPhase(self):
		"""rfPhase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfPhase'):
			from .RfPhase import RfPhase
			self._rfPhase = RfPhase(self._core, self._cmd_group)
		return self._rfPhase

	def get_ncarrier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:NCARrier \n
		Snippet: value: int = driver.source.bb.nr5G.node.get_ncarrier() \n
		Sets the number of simulated carriers. When used in a previously configured system, reconfigures the number of simulated
		carriers. \n
			:return: num_carrier: integer Range: 1 to 16
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:NODE:NCARrier?')
		return Conversions.str_to_int(response)

	def set_ncarrier(self, num_carrier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:NCARrier \n
		Snippet: driver.source.bb.nr5G.node.set_ncarrier(num_carrier = 1) \n
		Sets the number of simulated carriers. When used in a previously configured system, reconfigures the number of simulated
		carriers. \n
			:param num_carrier: integer Range: 1 to 16
		"""
		param = Conversions.decimal_value_to_str(num_carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:NCARrier {param}')

	def clone(self) -> 'Node':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Node(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
