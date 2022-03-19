from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class A:
	"""A commands group definition. 9 total commands, 9 Subgroups, 0 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antenna_get', 'repcap_antenna_set', repcap.Antenna.Nr1)

	def repcap_antenna_set(self, antenna: repcap.Antenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Antenna.Default
		Default value after init: Antenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(antenna)

	def repcap_antenna_get(self) -> repcap.Antenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apattern(self):
		"""apattern commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apattern'):
			from .Apattern import Apattern
			self._apattern = Apattern(self._core, self._cmd_group)
		return self._apattern

	@property
	def body(self):
		"""body commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_body'):
			from .Body import Body
			self._body = Body(self._core, self._cmd_group)
		return self._body

	@property
	def dbank(self):
		"""dbank commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbank'):
			from .Dbank import Dbank
			self._dbank = Dbank(self._core, self._cmd_group)
		return self._dbank

	@property
	def delevation(self):
		"""delevation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delevation'):
			from .Delevation import Delevation
			self._delevation = Delevation(self._core, self._cmd_group)
		return self._delevation

	@property
	def dheading(self):
		"""dheading commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dheading'):
			from .Dheading import Dheading
			self._dheading = Dheading(self._core, self._cmd_group)
		return self._dheading

	@property
	def dx(self):
		"""dx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dx'):
			from .Dx import Dx
			self._dx = Dx(self._core, self._cmd_group)
		return self._dx

	@property
	def dy(self):
		"""dy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dy'):
			from .Dy import Dy
			self._dy = Dy(self._core, self._cmd_group)
		return self._dy

	@property
	def dz(self):
		"""dz commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dz'):
			from .Dz import Dz
			self._dz = Dz(self._core, self._cmd_group)
		return self._dz

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'A':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = A(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
