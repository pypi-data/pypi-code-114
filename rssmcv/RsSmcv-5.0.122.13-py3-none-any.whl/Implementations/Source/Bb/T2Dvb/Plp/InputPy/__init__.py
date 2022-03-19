from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def stuffing(self):
		"""stuffing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stuffing'):
			from .Stuffing import Stuffing
			self._stuffing = Stuffing(self._core, self._cmd_group)
		return self._stuffing

	@property
	def testSignal(self):
		"""testSignal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_testSignal'):
			from .TestSignal import TestSignal
			self._testSignal = TestSignal(self._core, self._cmd_group)
		return self._testSignal

	@property
	def dataRate(self):
		"""dataRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dataRate'):
			from .DataRate import DataRate
			self._dataRate = DataRate(self._core, self._cmd_group)
		return self._dataRate

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
