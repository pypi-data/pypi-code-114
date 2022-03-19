from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sf1Reserved:
	"""Sf1Reserved commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sf1Reserved", core, parent)

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:NAV:EPHemeris:SF1Reserved \n
		Snippet: value: int = driver.source.bb.gnss.svid.qzss.nmessage.nav.ephemeris.sf1Reserved.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the subframe 1 (reserved 1 to 4) . \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: subfr_1_reserved: integer Range: 0 to 67108864"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:NAV:EPHemeris:SF1Reserved?')
		return Conversions.str_to_int(response)
