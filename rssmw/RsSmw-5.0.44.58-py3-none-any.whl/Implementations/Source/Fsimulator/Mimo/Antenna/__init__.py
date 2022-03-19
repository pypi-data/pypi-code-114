from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Antenna:
	"""Antenna commands group definition. 27 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)

	@property
	def inverse(self):
		"""inverse commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inverse'):
			from .Inverse import Inverse
			self._inverse = Inverse(self._core, self._cmd_group)
		return self._inverse

	@property
	def modeling(self):
		"""modeling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modeling'):
			from .Modeling import Modeling
			self._modeling = Modeling(self._core, self._cmd_group)
		return self._modeling

	@property
	def pattern(self):
		"""pattern commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def polarization(self):
		"""polarization commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_polarization'):
			from .Polarization import Polarization
			self._polarization = Polarization(self._core, self._cmd_group)
		return self._polarization

	@property
	def rx(self):
		"""rx commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_rx'):
			from .Rx import Rx
			self._rx = Rx(self._core, self._cmd_group)
		return self._rx

	@property
	def tx(self):
		"""tx commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import Tx
			self._tx = Tx(self._core, self._cmd_group)
		return self._tx

	def clone(self) -> 'Antenna':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Antenna(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
