from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pm:
	"""Pm commands group definition. 9 total commands, 4 Subgroups, 3 group commands
	Repeated Capability: GeneratorIx, default value after init: GeneratorIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pm", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_generatorIx_get', 'repcap_generatorIx_set', repcap.GeneratorIx.Nr1)

	def repcap_generatorIx_set(self, generatorIx: repcap.GeneratorIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GeneratorIx.Default
		Default value after init: GeneratorIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(generatorIx)

	def repcap_generatorIx_get(self) -> repcap.GeneratorIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def deviation(self):
		"""deviation commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_deviation'):
			from .Deviation import Deviation
			self._deviation = Deviation(self._core, self._cmd_group)
		return self._deviation

	@property
	def internal(self):
		"""internal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_internal'):
			from .Internal import Internal
			self._internal = Internal(self._core, self._cmd_group)
		return self._internal

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PmMode:
		"""SCPI: [SOURce<HW>]:PM:MODE \n
		Snippet: value: enums.PmMode = driver.source.pm.get_mode() \n
		Selects the mode for the phase modulation. \n
			:return: mode: HBANdwidth| HDEViation| LNOise HBANdwidth Sets the maximum available bandwidth. HDEViation Sets the maximum range for ΦM deviation. LNOise Selects a phase modulation mode with phase noise and spurious characteristics close to CW mode.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PmMode)

	def set_mode(self, mode: enums.PmMode) -> None:
		"""SCPI: [SOURce<HW>]:PM:MODE \n
		Snippet: driver.source.pm.set_mode(mode = enums.PmMode.HBANdwidth) \n
		Selects the mode for the phase modulation. \n
			:param mode: HBANdwidth| HDEViation| LNOise HBANdwidth Sets the maximum available bandwidth. HDEViation Sets the maximum range for ΦM deviation. LNOise Selects a phase modulation mode with phase noise and spurious characteristics close to CW mode.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PmMode)
		self._core.io.write(f'SOURce<HwInstance>:PM:MODE {param}')

	def get_ratio(self) -> float:
		"""SCPI: [SOURce<HW>]:PM:RATio \n
		Snippet: value: float = driver.source.pm.get_ratio() \n
		Sets the deviation ratio (path2 to path1) in percent. \n
			:return: ratio: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PM:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: [SOURce<HW>]:PM:RATio \n
		Snippet: driver.source.pm.set_ratio(ratio = 1.0) \n
		Sets the deviation ratio (path2 to path1) in percent. \n
			:param ratio: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SOURce<HwInstance>:PM:RATio {param}')

	def get_sensitivity(self) -> float:
		"""SCPI: [SOURce<HW>]:PM:SENSitivity \n
		Snippet: value: float = driver.source.pm.get_sensitivity() \n
		Queries the sensitivity of the externally applied signal for phase modulation. The returned value reports the sensitivity
		in RAD/V. It is assigned to the voltage value for full modulation of the input. \n
			:return: sensitivity: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PM:SENSitivity?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Pm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
