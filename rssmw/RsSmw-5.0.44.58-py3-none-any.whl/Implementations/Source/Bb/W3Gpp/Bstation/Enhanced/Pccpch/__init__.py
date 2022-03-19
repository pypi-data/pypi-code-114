from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pccpch:
	"""Pccpch commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pccpch", core, parent)

	@property
	def ccoding(self):
		"""ccoding commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:PCCPch:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.enhanced.pccpch.get_state() \n
		The command activates or deactivates the enhanced state of the P-CCPCH (BCH) . \n
			:return: state: ON| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:PCCPch:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:PCCPch:STATe \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.pccpch.set_state(state = False) \n
		The command activates or deactivates the enhanced state of the P-CCPCH (BCH) . \n
			:param state: ON| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:PCCPch:STATe {param}')

	def clone(self) -> 'Pccpch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pccpch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
