from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tap:
	"""Tap commands group definition. 377 total commands, 5 Subgroups, 1 group commands
	Repeated Capability: MimoTap, default value after init: MimoTap.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tap", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_mimoTap_get', 'repcap_mimoTap_set', repcap.MimoTap.Nr1)

	def repcap_mimoTap_set(self, mimoTap: repcap.MimoTap) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MimoTap.Default
		Default value after init: MimoTap.Nr1"""
		self._cmd_group.set_repcap_enum_value(mimoTap)

	def repcap_mimoTap_get(self) -> repcap.MimoTap:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def antenna(self):
		"""antenna commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def gvector(self):
		"""gvector commands group. 66 Sub-classes, 1 commands."""
		if not hasattr(self, '_gvector'):
			from .Gvector import Gvector
			self._gvector = Gvector(self._core, self._cmd_group)
		return self._gvector

	@property
	def kronecker(self):
		"""kronecker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_kronecker'):
			from .Kronecker import Kronecker
			self._kronecker = Kronecker(self._core, self._cmd_group)
		return self._kronecker

	@property
	def matrix(self):
		"""matrix commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_matrix'):
			from .Matrix import Matrix
			self._matrix = Matrix(self._core, self._cmd_group)
		return self._matrix

	@property
	def tgn(self):
		"""tgn commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tgn'):
			from .Tgn import Tgn
			self._tgn = Tgn(self._core, self._cmd_group)
		return self._tgn

	# noinspection PyTypeChecker
	def get_value(self) -> enums.FadMimoTap:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP \n
		Snippet: value: enums.FadMimoTap = driver.source.fsimulator.mimo.tap.get_value() \n
		Sets the current tap. \n
			:return: tap: TAP1| TAP2| TAP3| TAP4| TAP5| TAP6| TAP7| TAP8| TAP9| TAP10| TAP11| TAP12| TAP13| TAP14| TAP15| TAP16| TAP17| TAP18| TAP19| TAP20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:TAP?')
		return Conversions.str_to_scalar_enum(response, enums.FadMimoTap)

	def set_value(self, tap: enums.FadMimoTap) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP \n
		Snippet: driver.source.fsimulator.mimo.tap.set_value(tap = enums.FadMimoTap.TAP1) \n
		Sets the current tap. \n
			:param tap: TAP1| TAP2| TAP3| TAP4| TAP5| TAP6| TAP7| TAP8| TAP9| TAP10| TAP11| TAP12| TAP13| TAP14| TAP15| TAP16| TAP17| TAP18| TAP19| TAP20
		"""
		param = Conversions.enum_scalar_to_str(tap, enums.FadMimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP {param}')

	def clone(self) -> 'Tap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
