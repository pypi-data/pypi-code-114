from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L2Cphasing:
	"""L2Cphasing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l2Cphasing", core, parent)

	def set(self, l_2_cphasing: bool, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:CNAV:EPHemeris:L2CPhasing \n
		Snippet: driver.source.bb.gnss.svid.gps.nmessage.cnav.ephemeris.l2Cphasing.set(l_2_cphasing = False, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the L2C phasing. \n
			:param l_2_cphasing: 1| ON| 0| OFF
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.bool_to_str(l_2_cphasing)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:CNAV:EPHemeris:L2CPhasing {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:CNAV:EPHemeris:L2CPhasing \n
		Snippet: value: bool = driver.source.bb.gnss.svid.gps.nmessage.cnav.ephemeris.l2Cphasing.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the L2C phasing. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: l_2_cphasing: 1| ON| 0| OFF"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:CNAV:EPHemeris:L2CPhasing?')
		return Conversions.str_to_bool(response)
