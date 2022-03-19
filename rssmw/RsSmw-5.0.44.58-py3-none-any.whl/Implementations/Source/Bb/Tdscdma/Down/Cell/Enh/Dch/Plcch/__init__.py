from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plcch:
	"""Plcch commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plcch", core, parent)

	@property
	def ssPattern(self):
		"""ssPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssPattern'):
			from .SsPattern import SsPattern
			self._ssPattern = SsPattern(self._core, self._cmd_group)
		return self._ssPattern

	@property
	def tpcPattern(self):
		"""tpcPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpcPattern'):
			from .TpcPattern import TpcPattern
			self._tpcPattern = TpcPattern(self._core, self._cmd_group)
		return self._tpcPattern

	@property
	def ttInterval(self):
		"""ttInterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttInterval'):
			from .TtInterval import TtInterval
			self._ttInterval = TtInterval(self._core, self._cmd_group)
		return self._ttInterval

	def clone(self) -> 'Plcch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Plcch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
