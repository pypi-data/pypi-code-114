from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class B:
	"""B commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def get_number(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:B:NUMBer \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.eon.af.b.get_number() \n
		No command help available \n
			:return: eon_afb_num_freq: integer Range: 0 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:B:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, eon_afb_num_freq: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:B:NUMBer \n
		Snippet: driver.source.bb.radio.fm.rds.eon.af.b.set_number(eon_afb_num_freq = 1) \n
		No command help available \n
			:param eon_afb_num_freq: integer Range: 0 to 4
		"""
		param = Conversions.decimal_value_to_str(eon_afb_num_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:B:NUMBer {param}')

	def get_tfrequency(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:B:TFRequency \n
		Snippet: value: float = driver.source.bb.radio.fm.rds.eon.af.b.get_tfrequency() \n
		Sets the tuning frequency of in AF mapped frequencies method. \n
			:return: eon_aft_freq: float Range: 87.6 to 107.9, Unit: MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:B:TFRequency?')
		return Conversions.str_to_float(response)

	def set_tfrequency(self, eon_aft_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:B:TFRequency \n
		Snippet: driver.source.bb.radio.fm.rds.eon.af.b.set_tfrequency(eon_aft_freq = 1.0) \n
		Sets the tuning frequency of in AF mapped frequencies method. \n
			:param eon_aft_freq: float Range: 87.6 to 107.9, Unit: MHz
		"""
		param = Conversions.decimal_value_to_str(eon_aft_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:B:TFRequency {param}')

	def clone(self) -> 'B':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = B(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
