from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 4 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: Path, default value after init: Path.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_path_get', 'repcap_path_set', repcap.Path.Nr1)

	def repcap_path_set(self, path: repcap.Path) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Path.Default
		Default value after init: Path.Nr1"""
		self._cmd_group.set_repcap_enum_value(path)

	def repcap_path_get(self) -> repcap.Path:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def fdoppler(self):
		"""fdoppler commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdoppler'):
			from .Fdoppler import Fdoppler
			self._fdoppler = Fdoppler(self._core, self._cmd_group)
		return self._fdoppler

	@property
	def loss(self):
		"""loss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loss'):
			from .Loss import Loss
			self._loss = Loss(self._core, self._cmd_group)
		return self._loss

	@property
	def profile(self):
		"""profile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_profile'):
			from .Profile import Profile
			self._profile = Profile(self._core, self._cmd_group)
		return self._profile

	def clone(self) -> 'Path':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Path(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
