from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LtpData:
	"""LtpData commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ltpData", core, parent)

	def set(self, l_2_p: bool, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:NAV:EPHemeris:LTPData \n
		Snippet: driver.source.bb.gnss.svid.qzss.nmessage.nav.ephemeris.ltpData.set(l_2_p = False, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the L2 P data flag. \n
			:param l_2_p: 1| ON| 0| OFF
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.bool_to_str(l_2_p)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:NAV:EPHemeris:LTPData {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:NAV:EPHemeris:LTPData \n
		Snippet: value: bool = driver.source.bb.gnss.svid.qzss.nmessage.nav.ephemeris.ltpData.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the L2 P data flag. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: l_2_p: 1| ON| 0| OFF"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:NAV:EPHemeris:LTPData?')
		return Conversions.str_to_bool(response)
