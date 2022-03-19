from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fsk:
	"""Fsk commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fsk", core, parent)

	@property
	def variable(self):
		"""variable commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_variable'):
			from .Variable import Variable
			self._variable = Variable(self._core, self._cmd_group)
		return self._variable

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:FSK:DEViation \n
		Snippet: value: float = driver.source.bb.dm.fsk.get_deviation() \n
		Sets the frequency deviation when FSK modulation is selected. \n
			:return: deviation: float The value range depends on the symbol rate. Range: 1 to 40E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FSK:DEViation?')
		return Conversions.str_to_float(response)

	def set_deviation(self, deviation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FSK:DEViation \n
		Snippet: driver.source.bb.dm.fsk.set_deviation(deviation = 1.0) \n
		Sets the frequency deviation when FSK modulation is selected. \n
			:param deviation: float The value range depends on the symbol rate. Range: 1 to 40E6
		"""
		param = Conversions.decimal_value_to_str(deviation)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FSK:DEViation {param}')

	def clone(self) -> 'Fsk':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fsk(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
