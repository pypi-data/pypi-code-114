from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 10 total commands, 7 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	@property
	def conflict(self):
		"""conflict commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conflict'):
			from .Conflict import Conflict
			self._conflict = Conflict(self._core, self._cmd_group)
		return self._conflict

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier:COUNt \n
		Snippet: value: int = driver.source.bb.arbitrary.mcarrier.carrier.get_count() \n
		Sets the number of carriers in the ARB multi-carrier waveform. \n
			:return: count: integer Range: 1 to 512
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier:COUNt \n
		Snippet: driver.source.bb.arbitrary.mcarrier.carrier.set_count(count = 1) \n
		Sets the number of carriers in the ARB multi-carrier waveform. \n
			:param count: integer Range: 1 to 512
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier:COUNt {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbMultCarrSpacMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier:MODE \n
		Snippet: value: enums.ArbMultCarrSpacMode = driver.source.bb.arbitrary.mcarrier.carrier.get_mode() \n
		The command sets the carrier frequency mode. \n
			:return: mode: EQUidistant| ARBitrary
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbMultCarrSpacMode)

	def set_mode(self, mode: enums.ArbMultCarrSpacMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier:MODE \n
		Snippet: driver.source.bb.arbitrary.mcarrier.carrier.set_mode(mode = enums.ArbMultCarrSpacMode.ARBitrary) \n
		The command sets the carrier frequency mode. \n
			:param mode: EQUidistant| ARBitrary
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbMultCarrSpacMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier:MODE {param}')

	def get_spacing(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier:SPACing \n
		Snippet: value: float = driver.source.bb.arbitrary.mcarrier.carrier.get_spacing() \n
		Sets the frequency spacing between adjacent carriers of the multi-carrier waveform (see 'Defining the carrier frequency')
		. \n
			:return: spacing: float Range: 0.0 to depends on the installed options, e.g. 120E6 (R&S SMW-B10) , Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier:SPACing?')
		return Conversions.str_to_float(response)

	def set_spacing(self, spacing: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier:SPACing \n
		Snippet: driver.source.bb.arbitrary.mcarrier.carrier.set_spacing(spacing = 1.0) \n
		Sets the frequency spacing between adjacent carriers of the multi-carrier waveform (see 'Defining the carrier frequency')
		. \n
			:param spacing: float Range: 0.0 to depends on the installed options, e.g. 120E6 (R&S SMW-B10) , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(spacing)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier:SPACing {param}')

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
