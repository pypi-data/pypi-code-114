from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tinterval:
	"""Tinterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tinterval", core, parent)

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:TINTerval \n
		Snippet: value: str = driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.tinterval.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Queries the Tb-interval. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: tb_interval: string"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:TINTerval?')
		return trim_str_response(response)
