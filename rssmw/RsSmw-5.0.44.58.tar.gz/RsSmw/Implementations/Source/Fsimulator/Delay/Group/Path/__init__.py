from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 22 total commands, 16 Subgroups, 0 group commands
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
	def adelay(self):
		"""adelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adelay'):
			from .Adelay import Adelay
			self._adelay = Adelay(self._core, self._cmd_group)
		return self._adelay

	@property
	def bdelay(self):
		"""bdelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdelay'):
			from .Bdelay import Bdelay
			self._bdelay = Bdelay(self._core, self._cmd_group)
		return self._bdelay

	@property
	def correlation(self):
		"""correlation commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_correlation'):
			from .Correlation import Correlation
			self._correlation = Correlation(self._core, self._cmd_group)
		return self._correlation

	@property
	def cphase(self):
		"""cphase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cphase'):
			from .Cphase import Cphase
			self._cphase = Cphase(self._core, self._cmd_group)
		return self._cphase

	@property
	def custom(self):
		"""custom commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_custom'):
			from .Custom import Custom
			self._custom = Custom(self._core, self._cmd_group)
		return self._custom

	@property
	def fdoppler(self):
		"""fdoppler commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdoppler'):
			from .Fdoppler import Fdoppler
			self._fdoppler = Fdoppler(self._core, self._cmd_group)
		return self._fdoppler

	@property
	def fratio(self):
		"""fratio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fratio'):
			from .Fratio import Fratio
			self._fratio = Fratio(self._core, self._cmd_group)
		return self._fratio

	@property
	def fshift(self):
		"""fshift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fshift'):
			from .Fshift import Fshift
			self._fshift = Fshift(self._core, self._cmd_group)
		return self._fshift

	@property
	def fspread(self):
		"""fspread commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fspread'):
			from .Fspread import Fspread
			self._fspread = Fspread(self._core, self._cmd_group)
		return self._fspread

	@property
	def logNormal(self):
		"""logNormal commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_logNormal'):
			from .LogNormal import LogNormal
			self._logNormal = LogNormal(self._core, self._cmd_group)
		return self._logNormal

	@property
	def loss(self):
		"""loss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loss'):
			from .Loss import Loss
			self._loss = Loss(self._core, self._cmd_group)
		return self._loss

	@property
	def pratio(self):
		"""pratio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pratio'):
			from .Pratio import Pratio
			self._pratio = Pratio(self._core, self._cmd_group)
		return self._pratio

	@property
	def profile(self):
		"""profile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_profile'):
			from .Profile import Profile
			self._profile = Profile(self._core, self._cmd_group)
		return self._profile

	@property
	def rdelay(self):
		"""rdelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rdelay'):
			from .Rdelay import Rdelay
			self._rdelay = Rdelay(self._core, self._cmd_group)
		return self._rdelay

	@property
	def speed(self):
		"""speed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_speed'):
			from .Speed import Speed
			self._speed = Speed(self._core, self._cmd_group)
		return self._speed

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Path':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Path(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
