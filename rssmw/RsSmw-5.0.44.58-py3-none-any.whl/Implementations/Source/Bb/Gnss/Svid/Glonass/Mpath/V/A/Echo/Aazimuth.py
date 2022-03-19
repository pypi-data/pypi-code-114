from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aazimuth:
	"""Aazimuth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aazimuth", core, parent)

	def set(self, aoa_azimuth: float, satelliteSvid=repcap.SatelliteSvid.Default, vehicle=repcap.Vehicle.Default, antenna=repcap.Antenna.Default, echo=repcap.Echo.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:MPATh:[V<US>]:[A<GR>]:ECHO<S2US0>:AAZimuth \n
		Snippet: driver.source.bb.gnss.svid.glonass.mpath.v.a.echo.aazimuth.set(aoa_azimuth = 1.0, satelliteSvid = repcap.SatelliteSvid.Default, vehicle = repcap.Vehicle.Default, antenna = repcap.Antenna.Default, echo = repcap.Echo.Default) \n
		Sets the angle of arrival azimuth. \n
			:param aoa_azimuth: float Range: 0 to 6.28, Unit: rad
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
			:param echo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Echo')
		"""
		param = Conversions.decimal_value_to_str(aoa_azimuth)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		echo_cmd_val = self._cmd_group.get_repcap_cmd_value(echo, repcap.Echo)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:MPATh:V{vehicle_cmd_val}:A{antenna_cmd_val}:ECHO{echo_cmd_val}:AAZimuth {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, vehicle=repcap.Vehicle.Default, antenna=repcap.Antenna.Default, echo=repcap.Echo.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:MPATh:[V<US>]:[A<GR>]:ECHO<S2US0>:AAZimuth \n
		Snippet: value: float = driver.source.bb.gnss.svid.glonass.mpath.v.a.echo.aazimuth.get(satelliteSvid = repcap.SatelliteSvid.Default, vehicle = repcap.Vehicle.Default, antenna = repcap.Antenna.Default, echo = repcap.Echo.Default) \n
		Sets the angle of arrival azimuth. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
			:param echo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Echo')
			:return: aoa_azimuth: float Range: 0 to 6.28, Unit: rad"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		echo_cmd_val = self._cmd_group.get_repcap_cmd_value(echo, repcap.Echo)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:MPATh:V{vehicle_cmd_val}:A{antenna_cmd_val}:ECHO{echo_cmd_val}:AAZimuth?')
		return Conversions.str_to_float(response)
