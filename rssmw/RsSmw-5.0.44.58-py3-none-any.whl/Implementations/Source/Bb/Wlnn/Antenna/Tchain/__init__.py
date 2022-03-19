from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tchain:
	"""Tchain commands group definition. 6 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: TransmissionChain, default value after init: TransmissionChain.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tchain", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_transmissionChain_get', 'repcap_transmissionChain_set', repcap.TransmissionChain.Nr1)

	def repcap_transmissionChain_set(self, transmissionChain: repcap.TransmissionChain) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TransmissionChain.Default
		Default value after init: TransmissionChain.Nr1"""
		self._cmd_group.set_repcap_enum_value(transmissionChain)

	def repcap_transmissionChain_get(self) -> repcap.TransmissionChain:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def output(self):
		"""output commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def tx(self):
		"""tx commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import Tx
			self._tx = Tx(self._core, self._cmd_group)
		return self._tx

	def clone(self) -> 'Tchain':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tchain(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
