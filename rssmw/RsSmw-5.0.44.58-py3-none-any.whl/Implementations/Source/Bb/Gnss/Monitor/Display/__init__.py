from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Display:
	"""Display commands group definition. 39 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def channels(self):
		"""channels commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channels'):
			from .Channels import Channels
			self._channels = Channels(self._core, self._cmd_group)
		return self._channels

	@property
	def map(self):
		"""map commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_map'):
			from .Map import Map
			self._map = Map(self._core, self._cmd_group)
		return self._map

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def stream(self):
		"""stream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import Stream
			self._stream = Stream(self._core, self._cmd_group)
		return self._stream

	@property
	def tracks(self):
		"""tracks commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tracks'):
			from .Tracks import Tracks
			self._tracks = Tracks(self._core, self._cmd_group)
		return self._tracks

	@property
	def trajectory(self):
		"""trajectory commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trajectory'):
			from .Trajectory import Trajectory
			self._trajectory = Trajectory(self._core, self._cmd_group)
		return self._trajectory

	@property
	def vehicle(self):
		"""vehicle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vehicle'):
			from .Vehicle import Vehicle
			self._vehicle = Vehicle(self._core, self._cmd_group)
		return self._vehicle

	def set(self, display_type: enums.MonitorDisplayType, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay \n
		Snippet: driver.source.bb.gnss.monitor.display.set(display_type = enums.MonitorDisplayType.ATTitude, monitorPane = repcap.MonitorPane.Default) \n
		Switches between the available views. \n
			:param display_type: SKY| MAP| POWer| TRAJectory| ATTitude| TRACks| CHANnels
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.enum_scalar_to_str(display_type, enums.MonitorDisplayType)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay {param}')

	# noinspection PyTypeChecker
	def get(self, monitorPane=repcap.MonitorPane.Default) -> enums.MonitorDisplayType:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay \n
		Snippet: value: enums.MonitorDisplayType = driver.source.bb.gnss.monitor.display.get(monitorPane = repcap.MonitorPane.Default) \n
		Switches between the available views. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: display_type: SKY| MAP| POWer| TRAJectory| ATTitude| TRACks| CHANnels"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.MonitorDisplayType)

	def clone(self) -> 'Display':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Display(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
