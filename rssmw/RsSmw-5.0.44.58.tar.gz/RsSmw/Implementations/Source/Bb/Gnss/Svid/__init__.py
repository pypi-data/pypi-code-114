from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Svid:
	"""Svid commands group definition. 1306 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: SatelliteSvid, default value after init: SatelliteSvid.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("svid", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_satelliteSvid_get', 'repcap_satelliteSvid_set', repcap.SatelliteSvid.Nr1)

	def repcap_satelliteSvid_set(self, satelliteSvid: repcap.SatelliteSvid) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SatelliteSvid.Default
		Default value after init: SatelliteSvid.Nr1"""
		self._cmd_group.set_repcap_enum_value(satelliteSvid)

	def repcap_satelliteSvid_get(self) -> repcap.SatelliteSvid:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def beidou(self):
		"""beidou commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_beidou'):
			from .Beidou import Beidou
			self._beidou = Beidou(self._core, self._cmd_group)
		return self._beidou

	@property
	def galileo(self):
		"""galileo commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_galileo'):
			from .Galileo import Galileo
			self._galileo = Galileo(self._core, self._cmd_group)
		return self._galileo

	@property
	def glonass(self):
		"""glonass commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_glonass'):
			from .Glonass import Glonass
			self._glonass = Glonass(self._core, self._cmd_group)
		return self._glonass

	@property
	def gps(self):
		"""gps commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_gps'):
			from .Gps import Gps
			self._gps = Gps(self._core, self._cmd_group)
		return self._gps

	@property
	def navic(self):
		"""navic commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_navic'):
			from .Navic import Navic
			self._navic = Navic(self._core, self._cmd_group)
		return self._navic

	@property
	def qzss(self):
		"""qzss commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_qzss'):
			from .Qzss import Qzss
			self._qzss = Qzss(self._core, self._cmd_group)
		return self._qzss

	@property
	def sbas(self):
		"""sbas commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_sbas'):
			from .Sbas import Sbas
			self._sbas = Sbas(self._core, self._cmd_group)
		return self._sbas

	def clone(self) -> 'Svid':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Svid(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
