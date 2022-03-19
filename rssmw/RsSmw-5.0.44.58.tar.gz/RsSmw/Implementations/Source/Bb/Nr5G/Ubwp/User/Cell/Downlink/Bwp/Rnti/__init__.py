from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rnti:
	"""Rnti commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rnti", core, parent)

	@property
	def aiRnti(self):
		"""aiRnti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aiRnti'):
			from .AiRnti import AiRnti
			self._aiRnti = AiRnti(self._core, self._cmd_group)
		return self._aiRnti

	@property
	def ciRnti(self):
		"""ciRnti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ciRnti'):
			from .CiRnti import CiRnti
			self._ciRnti = CiRnti(self._core, self._cmd_group)
		return self._ciRnti

	@property
	def int(self):
		"""int commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_int'):
			from .Int import Int
			self._int = Int(self._core, self._cmd_group)
		return self._int

	@property
	def psRnti(self):
		"""psRnti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psRnti'):
			from .PsRnti import PsRnti
			self._psRnti = PsRnti(self._core, self._cmd_group)
		return self._psRnti

	@property
	def pucch(self):
		"""pucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import Pucch
			self._pucch = Pucch(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

	@property
	def srs(self):
		"""srs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import Srs
			self._srs = Srs(self._core, self._cmd_group)
		return self._srs

	def clone(self) -> 'Rnti':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rnti(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
