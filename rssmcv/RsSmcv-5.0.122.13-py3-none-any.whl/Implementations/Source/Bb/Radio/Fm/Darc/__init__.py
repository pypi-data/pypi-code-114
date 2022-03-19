from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Darc:
	"""Darc commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("darc", core, parent)

	@property
	def bic(self):
		"""bic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bic'):
			from .Bic import Bic
			self._bic = Bic(self._core, self._cmd_group)
		return self._bic

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:DEViation \n
		Snippet: value: float = driver.source.bb.radio.fm.darc.get_deviation() \n
		No command help available \n
			:return: freq_dev_darc: float Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:DARC:DEViation?')
		return Conversions.str_to_float(response)

	def set_deviation(self, freq_dev_darc: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:DEViation \n
		Snippet: driver.source.bb.radio.fm.darc.set_deviation(freq_dev_darc = 1.0) \n
		No command help available \n
			:param freq_dev_darc: float Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(freq_dev_darc)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:DARC:DEViation {param}')

	# noinspection PyTypeChecker
	def get_information(self) -> enums.AudioBcFmDarcInformation:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:INFormation \n
		Snippet: value: enums.AudioBcFmDarcInformation = driver.source.bb.radio.fm.darc.get_information() \n
		No command help available \n
			:return: darc_inf: OFF| PRBS| DATa
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:DARC:INFormation?')
		return Conversions.str_to_scalar_enum(response, enums.AudioBcFmDarcInformation)

	def set_information(self, darc_inf: enums.AudioBcFmDarcInformation) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:INFormation \n
		Snippet: driver.source.bb.radio.fm.darc.set_information(darc_inf = enums.AudioBcFmDarcInformation.DATa) \n
		No command help available \n
			:param darc_inf: OFF| PRBS| DATa
		"""
		param = Conversions.enum_scalar_to_str(darc_inf, enums.AudioBcFmDarcInformation)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:DARC:INFormation {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:[STATe] \n
		Snippet: value: bool = driver.source.bb.radio.fm.darc.get_state() \n
		No command help available \n
			:return: darc: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:DARC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, darc: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:[STATe] \n
		Snippet: driver.source.bb.radio.fm.darc.set_state(darc = False) \n
		No command help available \n
			:param darc: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(darc)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:DARC:STATe {param}')

	def clone(self) -> 'Darc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Darc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
