from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class A:
	"""A commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def get_number(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:A:NUMBer \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.eon.af.a.get_number() \n
		Defines the number of alternative frequencies. \n
			:return: eon_afa_num_freq: integer Range: 0 to 25
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:A:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, eon_afa_num_freq: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:A:NUMBer \n
		Snippet: driver.source.bb.radio.fm.rds.eon.af.a.set_number(eon_afa_num_freq = 1) \n
		Defines the number of alternative frequencies. \n
			:param eon_afa_num_freq: integer Range: 0 to 25
		"""
		param = Conversions.decimal_value_to_str(eon_afa_num_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:A:NUMBer {param}')

	def clone(self) -> 'A':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = A(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
