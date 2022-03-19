from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fm:
	"""Fm commands group definition. 9 total commands, 4 Subgroups, 3 group commands
	Repeated Capability: GeneratorIx, default value after init: GeneratorIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fm", core, parent)
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
	def get_mode(self) -> enums.FmMode:
		"""SCPI: [SOURce<HW>]:FM:MODE \n
		Snippet: value: enums.FmMode = driver.source.fm.get_mode() \n
		Selects the mode for the frequency modulation. \n
			:return: mode: NORMal| LNOise NORMal The maximum range for modulation bandwidth and FM deviation is available. LNOise Frequency modulation with phase noise and spurious characteristics close to CW mode. The range for modulation bandwidth and FM deviation is reduced (see data sheet) .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FmMode)

	def set_mode(self, mode: enums.FmMode) -> None:
		"""SCPI: [SOURce<HW>]:FM:MODE \n
		Snippet: driver.source.fm.set_mode(mode = enums.FmMode.LNOise) \n
		Selects the mode for the frequency modulation. \n
			:param mode: NORMal| LNOise NORMal The maximum range for modulation bandwidth and FM deviation is available. LNOise Frequency modulation with phase noise and spurious characteristics close to CW mode. The range for modulation bandwidth and FM deviation is reduced (see data sheet) .
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FmMode)
		self._core.io.write(f'SOURce<HwInstance>:FM:MODE {param}')

	def get_ratio(self) -> float:
		"""SCPI: [SOURce<HW>]:FM:RATio \n
		Snippet: value: float = driver.source.fm.get_ratio() \n
		Sets the deviation ratio (path2 to path1) in percent. \n
			:return: ratio: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FM:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: [SOURce<HW>]:FM:RATio \n
		Snippet: driver.source.fm.set_ratio(ratio = 1.0) \n
		Sets the deviation ratio (path2 to path1) in percent. \n
			:param ratio: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SOURce<HwInstance>:FM:RATio {param}')

	def get_sensitivity(self) -> float:
		"""SCPI: [SOURce<HW>]:FM:SENSitivity \n
		Snippet: value: float = driver.source.fm.get_sensitivity() \n
		Queries the sensitivity of the externally supplied signal for frequency modulation. The sensitivity depends on the set
		modulation deviation. \n
			:return: sensitivity: float Sensitivity in Hz/V. It is assigned to the voltage value for full modulation of the input. Range: 0 to max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FM:SENSitivity?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Fm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
