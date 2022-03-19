from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Variable:
	"""Variable commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("variable", core, parent)

	@property
	def symbol(self):
		"""symbol commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import Symbol
			self._symbol = Symbol(self._core, self._cmd_group)
		return self._symbol

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DmFskModType:
		"""SCPI: [SOURce<HW>]:BB:DM:FSK:VARiable:TYPE \n
		Snippet: value: enums.DmFskModType = driver.source.bb.dm.fsk.variable.get_type_py() \n
		The command selects the modulation type for Variable FSK. \n
			:return: type_py: FSK4| FSK8| FSK16
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FSK:VARiable:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DmFskModType)

	def set_type_py(self, type_py: enums.DmFskModType) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FSK:VARiable:TYPE \n
		Snippet: driver.source.bb.dm.fsk.variable.set_type_py(type_py = enums.DmFskModType.FSK16) \n
		The command selects the modulation type for Variable FSK. \n
			:param type_py: FSK4| FSK8| FSK16
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DmFskModType)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FSK:VARiable:TYPE {param}')

	def clone(self) -> 'Variable':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Variable(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
