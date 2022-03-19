from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Band:
	"""Band commands group definition. 5 total commands, 3 Subgroups, 1 group commands
	Repeated Capability: Band, default value after init: Band.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_band_get', 'repcap_band_set', repcap.Band.Nr1)

	def repcap_band_set(self, band: repcap.Band) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Band.Default
		Default value after init: Band.Nr1"""
		self._cmd_group.set_repcap_enum_value(band)

	def repcap_band_get(self) -> repcap.Band:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def config(self):
		"""config commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_config'):
			from .Config import Config
			self._config = Config(self._core, self._cmd_group)
		return self._config

	@property
	def lower(self):
		"""lower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import Lower
			self._lower = Lower(self._core, self._cmd_group)
		return self._lower

	@property
	def upper(self):
		"""upper commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import Upper
			self._upper = Upper(self._core, self._cmd_group)
		return self._upper

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:EFRontend:FREQuency:BAND:COUNt \n
		Snippet: value: int = driver.source.efrontend.frequency.band.get_count() \n
		Queries the number of frequency bands available at the connected external frontend. \n
			:return: fe_freq_count: integer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:FREQuency:BAND:COUNt?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Band':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Band(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
