from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L1Health:
	"""L1Health commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l1Health", core, parent)

	def set(self, l_1_health: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:CNAV:EPHemeris:L1Health \n
		Snippet: driver.source.bb.gnss.svid.qzss.nmessage.cnav.ephemeris.l1Health.set(l_1_health = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the L1, L2 or L5 health flag in the GPS/QZSS CNAV message. \n
			:param l_1_health: 0| 1| OFF| ON
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(l_1_health)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:CNAV:EPHemeris:L1Health {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:CNAV:EPHemeris:L1Health \n
		Snippet: value: int = driver.source.bb.gnss.svid.qzss.nmessage.cnav.ephemeris.l1Health.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the L1, L2 or L5 health flag in the GPS/QZSS CNAV message. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: l_1_health: 0| 1| OFF| ON"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:CNAV:EPHemeris:L1Health?')
		return Conversions.str_to_int(response)
