from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Notch:
	"""Notch commands group definition. 8 total commands, 4 Subgroups, 3 group commands
	Repeated Capability: NotchFilter, default value after init: NotchFilter.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("notch", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_notchFilter_get', 'repcap_notchFilter_set', repcap.NotchFilter.Nr1)

	def repcap_notchFilter_set(self, notchFilter: repcap.NotchFilter) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to NotchFilter.Default
		Default value after init: NotchFilter.Nr1"""
		self._cmd_group.set_repcap_enum_value(notchFilter)

	def repcap_notchFilter_get(self) -> repcap.NotchFilter:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def bandwidth(self):
		"""bandwidth commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def get_clock(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh:CLOCk \n
		Snippet: value: int = driver.source.bb.eutra.notch.get_clock() \n
		Queries the current clock frequency of the waveform signal. \n
			:return: clock_freq: integer Range: 400 to 2000E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOTCh:CLOCk?')
		return Conversions.str_to_int(response)

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh:COUNt \n
		Snippet: value: int = driver.source.bb.eutra.notch.get_count() \n
		Sets the number of notches. \n
			:return: num_of_notch: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOTCh:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, num_of_notch: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh:COUNt \n
		Snippet: driver.source.bb.eutra.notch.set_count(num_of_notch = 1) \n
		Sets the number of notches. \n
			:param num_of_notch: integer Range: 1 to 25
		"""
		param = Conversions.decimal_value_to_str(num_of_notch)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOTCh:COUNt {param}')

	def get_value(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh \n
		Snippet: value: bool = driver.source.bb.eutra.notch.get_value() \n
		Enables or disables the notch filter. \n
			:return: notch_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOTCh?')
		return Conversions.str_to_bool(response)

	def set_value(self, notch_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh \n
		Snippet: driver.source.bb.eutra.notch.set_value(notch_state = False) \n
		Enables or disables the notch filter. \n
			:param notch_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(notch_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOTCh {param}')

	def clone(self) -> 'Notch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Notch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
