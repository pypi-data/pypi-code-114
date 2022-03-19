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

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, vehicle=repcap.Vehicle.Default, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:MPATh:[V<US>]:[A<GR>]:LOS:AAZimuth \n
		Snippet: value: float = driver.source.bb.gnss.svid.sbas.mpath.v.a.los.aazimuth.get(satelliteSvid = repcap.SatelliteSvid.Default, vehicle = repcap.Vehicle.Default, antenna = repcap.Antenna.Default) \n
		Sets the angle of arrival azimuth. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
			:return: aoa_azimuth: float Range: 0 to 6.28, Unit: rad"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:MPATh:V{vehicle_cmd_val}:A{antenna_cmd_val}:LOS:AAZimuth?')
		return Conversions.str_to_float(response)
