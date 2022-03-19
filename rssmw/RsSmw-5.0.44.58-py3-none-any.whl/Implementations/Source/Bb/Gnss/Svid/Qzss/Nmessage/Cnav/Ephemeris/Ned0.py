from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ned0:
	"""Ned0 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ned0", core, parent)

	def set(self, ned_0: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:CNAV:EPHemeris:NED0 \n
		Snippet: driver.source.bb.gnss.svid.qzss.nmessage.cnav.ephemeris.ned0.set(ned_0 = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the NED accuracy index (NED0) , accuracy change indexs (NED1) and accuracy change rate index (NED2) . \n
			:param ned_0: integer Range: 0 to 7
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(ned_0)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:CNAV:EPHemeris:NED0 {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:CNAV:EPHemeris:NED0 \n
		Snippet: value: int = driver.source.bb.gnss.svid.qzss.nmessage.cnav.ephemeris.ned0.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the NED accuracy index (NED0) , accuracy change indexs (NED1) and accuracy change rate index (NED2) . \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: ned_0: integer Range: 0 to 7"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:CNAV:EPHemeris:NED0?')
		return Conversions.str_to_int(response)
