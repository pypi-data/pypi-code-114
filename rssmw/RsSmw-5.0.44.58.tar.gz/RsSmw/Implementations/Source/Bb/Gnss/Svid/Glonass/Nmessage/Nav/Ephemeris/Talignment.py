from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Talignment:
	"""Talignment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("talignment", core, parent)

	def set(self, tb_alignment: enums.TbAlign, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:TALignment \n
		Snippet: driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.talignment.set(tb_alignment = enums.TbAlign.EVEN, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the tb alignment - P2. \n
			:param tb_alignment: EVEN| ODD
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(tb_alignment, enums.TbAlign)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:TALignment {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.TbAlign:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:TALignment \n
		Snippet: value: enums.TbAlign = driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.talignment.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the tb alignment - P2. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: tb_alignment: EVEN| ODD"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:TALignment?')
		return Conversions.str_to_scalar_enum(response, enums.TbAlign)
