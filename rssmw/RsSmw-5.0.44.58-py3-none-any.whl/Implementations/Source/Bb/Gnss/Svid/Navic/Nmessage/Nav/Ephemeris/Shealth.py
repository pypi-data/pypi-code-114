from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Shealth:
	"""Shealth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shealth", core, parent)

	def set(self, shealth: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:NMESsage:NAV:EPHemeris:SHEalth \n
		Snippet: driver.source.bb.gnss.svid.navic.nmessage.nav.ephemeris.shealth.set(shealth = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the S health flag in the NavIC NAV message. \n
			:param shealth: 0| 1| OFF| ON
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(shealth)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:NMESsage:NAV:EPHemeris:SHEalth {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:NMESsage:NAV:EPHemeris:SHEalth \n
		Snippet: value: int = driver.source.bb.gnss.svid.navic.nmessage.nav.ephemeris.shealth.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the S health flag in the NavIC NAV message. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: shealth: 0| 1| OFF| ON"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:NMESsage:NAV:EPHemeris:SHEalth?')
		return Conversions.str_to_int(response)
