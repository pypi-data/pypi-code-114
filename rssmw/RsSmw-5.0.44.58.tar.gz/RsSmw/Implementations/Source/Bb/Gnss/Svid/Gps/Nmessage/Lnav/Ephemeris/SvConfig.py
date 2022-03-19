from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SvConfig:
	"""SvConfig commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("svConfig", core, parent)

	def set(self, as_flag: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:LNAV:EPHemeris:SVConfig \n
		Snippet: driver.source.bb.gnss.svid.gps.nmessage.lnav.ephemeris.svConfig.set(as_flag = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the SV config. \n
			:param as_flag: integer Range: 0 to 7
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(as_flag)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:LNAV:EPHemeris:SVConfig {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:LNAV:EPHemeris:SVConfig \n
		Snippet: value: int = driver.source.bb.gnss.svid.gps.nmessage.lnav.ephemeris.svConfig.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the SV config. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: as_flag: integer Range: 0 to 7"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:LNAV:EPHemeris:SVConfig?')
		return Conversions.str_to_int(response)
