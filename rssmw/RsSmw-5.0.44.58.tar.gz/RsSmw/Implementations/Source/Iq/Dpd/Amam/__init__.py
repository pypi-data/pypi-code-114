from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amam:
	"""Amam commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amam", core, parent)

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_value'):
			from .Value import Value
			self._value = Value(self._core, self._cmd_group)
		return self._value

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DPD:AMAM:STATe \n
		Snippet: value: bool = driver.source.iq.dpd.amam.get_state() \n
		Enabels/disables the AM/AM and AM/PM digital predistortion. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:AMAM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:AMAM:STATe \n
		Snippet: driver.source.iq.dpd.amam.set_state(state = False) \n
		Enabels/disables the AM/AM and AM/PM digital predistortion. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:AMAM:STATe {param}')

	def clone(self) -> 'Amam':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Amam(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
