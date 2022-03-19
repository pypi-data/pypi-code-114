from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iodc:
	"""Iodc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iodc", core, parent)

	def set(self, iodc: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:NMESsage:DNAV:EPHemeris:IODC \n
		Snippet: driver.source.bb.gnss.svid.beidou.nmessage.dnav.ephemeris.iodc.set(iodc = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the issue of data, clock (IODC) . \n
			:param iodc: integer Range: 0 to 1023
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(iodc)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:NMESsage:DNAV:EPHemeris:IODC {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:NMESsage:DNAV:EPHemeris:IODC \n
		Snippet: value: int = driver.source.bb.gnss.svid.beidou.nmessage.dnav.ephemeris.iodc.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the issue of data, clock (IODC) . \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: iodc: integer Range: 0 to 1023"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:NMESsage:DNAV:EPHemeris:IODC?')
		return Conversions.str_to_int(response)
