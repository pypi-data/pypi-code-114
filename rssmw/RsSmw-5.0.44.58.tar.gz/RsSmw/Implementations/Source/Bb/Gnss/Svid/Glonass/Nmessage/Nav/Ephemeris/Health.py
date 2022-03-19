from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Health:
	"""Health commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("health", core, parent)

	def set(self, sv_healt: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:HEALth \n
		Snippet: driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.health.set(sv_healt = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the SV health. See also [:SOURce<hw>]:BB:GNSS:SVID<ch>:GPS:HEALthy. \n
			:param sv_healt: integer Range: 0 to 63
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(sv_healt)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:HEALth {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:HEALth \n
		Snippet: value: int = driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.health.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the SV health. See also [:SOURce<hw>]:BB:GNSS:SVID<ch>:GPS:HEALthy. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: sv_healt: integer Range: 0 to 63"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:HEALth?')
		return Conversions.str_to_int(response)
