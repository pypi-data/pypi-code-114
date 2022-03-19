from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ilength:
	"""Ilength commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ilength", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:FILTer:ILENgth \n
		Snippet: value: int = driver.source.bb.evdo.filterPy.ilength.get_value() \n
		No command help available \n
			:return: ilength: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:FILTer:ILENgth?')
		return Conversions.str_to_int(response)

	def set_value(self, ilength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:FILTer:ILENgth \n
		Snippet: driver.source.bb.evdo.filterPy.ilength.set_value(ilength = 1) \n
		No command help available \n
			:param ilength: No help available
		"""
		param = Conversions.decimal_value_to_str(ilength)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:FILTer:ILENgth {param}')

	def clone(self) -> 'Ilength':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ilength(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
