from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Am:
	"""Am commands group definition. 6 total commands, 3 Subgroups, 2 group commands
	Repeated Capability: GeneratorIx, default value after init: GeneratorIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("am", core, parent)
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
	def depth(self):
		"""depth commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_depth'):
			from .Depth import Depth
			self._depth = Depth(self._core, self._cmd_group)
		return self._depth

	@property
	def deviation(self):
		"""deviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deviation'):
			from .Deviation import Deviation
			self._deviation = Deviation(self._core, self._cmd_group)
		return self._deviation

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def get_ratio(self) -> float:
		"""SCPI: [SOURce<HW>]:AM:RATio \n
		Snippet: value: float = driver.source.am.get_ratio() \n
		Sets the deviation ratio (path#2 to path#1) in percent. \n
			:return: ratio: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AM:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: [SOURce<HW>]:AM:RATio \n
		Snippet: driver.source.am.set_ratio(ratio = 1.0) \n
		Sets the deviation ratio (path#2 to path#1) in percent. \n
			:param ratio: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SOURce<HwInstance>:AM:RATio {param}')

	def get_sensitivity(self) -> float:
		"""SCPI: [SOURce<HW>]:AM:SENSitivity \n
		Snippet: value: float = driver.source.am.get_sensitivity() \n
		Sets the sensitivity of the external signal source for amplitude modulation in %/V. \n
			:return: sensitivity: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AM:SENSitivity?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Am':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Am(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
