from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class List5:
	"""List5 commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("list5", core, parent)

	@property
	def desc(self):
		"""desc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_desc'):
			from .Desc import Desc
			self._desc = Desc(self._core, self._cmd_group)
		return self._desc

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def get_number(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST5:NUMBer \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.af.b.list5.get_number() \n
		Sets the number of frequencies of a list in AF method B. \n
			:return: afb_list_5_no_freq: integer Range: 0 to 12
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST5:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, afb_list_5_no_freq: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST5:NUMBer \n
		Snippet: driver.source.bb.radio.fm.rds.af.b.list5.set_number(afb_list_5_no_freq = 1) \n
		Sets the number of frequencies of a list in AF method B. \n
			:param afb_list_5_no_freq: integer Range: 0 to 12
		"""
		param = Conversions.decimal_value_to_str(afb_list_5_no_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST5:NUMBer {param}')

	def get_tfrequency(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST5:TFRequency \n
		Snippet: value: float = driver.source.bb.radio.fm.rds.af.b.list5.get_tfrequency() \n
		Sets the tuning frequency of a list in AF method B. \n
			:return: af_list_5_tun_freq: float Range: 87.6 to 107.9, Unit: MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST5:TFRequency?')
		return Conversions.str_to_float(response)

	def set_tfrequency(self, af_list_5_tun_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST5:TFRequency \n
		Snippet: driver.source.bb.radio.fm.rds.af.b.list5.set_tfrequency(af_list_5_tun_freq = 1.0) \n
		Sets the tuning frequency of a list in AF method B. \n
			:param af_list_5_tun_freq: float Range: 87.6 to 107.9, Unit: MHz
		"""
		param = Conversions.decimal_value_to_str(af_list_5_tun_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST5:TFRequency {param}')

	def clone(self) -> 'List5':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = List5(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
