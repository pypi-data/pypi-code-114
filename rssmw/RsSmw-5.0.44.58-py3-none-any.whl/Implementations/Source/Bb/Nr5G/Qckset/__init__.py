from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qckset:
	"""Qckset commands group definition. 29 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qckset", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def discard(self):
		"""discard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_discard'):
			from .Discard import Discard
			self._discard = Discard(self._core, self._cmd_group)
		return self._discard

	@property
	def frmFormat(self):
		"""frmFormat commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_frmFormat'):
			from .FrmFormat import FrmFormat
			self._frmFormat = FrmFormat(self._core, self._cmd_group)
		return self._frmFormat

	@property
	def general(self):
		"""general commands group. 1 Sub-classes, 9 commands."""
		if not hasattr(self, '_general'):
			from .General import General
			self._general = General(self._core, self._cmd_group)
		return self._general

	def set_state(self, qck_set_state: enums.QuickSetStateAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:STATe \n
		Snippet: driver.source.bb.nr5G.qckset.set_state(qck_set_state = enums.QuickSetStateAll.DIS) \n
		No command help available \n
			:param qck_set_state: No help available
		"""
		param = Conversions.enum_scalar_to_str(qck_set_state, enums.QuickSetStateAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:STATe {param}')

	def clone(self) -> 'Qckset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qckset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
