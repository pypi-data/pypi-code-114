from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Healthy:
	"""Healthy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("healthy", core, parent)

	def set(self, healthy_state: bool, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:HEALthy \n
		Snippet: driver.source.bb.gnss.svid.beidou.healthy.set(healthy_state = False, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates if the selected SV ID is healthy or not. \n
			:param healthy_state: 1| ON| 0| OFF 1 = healthy satellite The healthy state reflects the value of the corresponding healthy flag in the navigation message: [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:LNAV:EPHemeris:HEALth [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L1Health [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L2Health [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L5Health [:SOURcehw]:BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BDVS [:SOURcehw]:BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BHS [:SOURcehw]:BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E5BHS [:SOURcehw]:BB:GNSS:SVIDch:BEIDou:NMESsage:DNAV:EPHemeris:HEALth [:SOURcehw]:BB:GNSS:SVIDch:GLONass:NMESsage:NAV:EPHemeris:HEALth [:SOURcehw]:BB:GNSS:SVIDch:QZSS:NMESsage:NAV:EPHemeris:HEALth The values are interdependent; changing one of them changes the other.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.bool_to_str(healthy_state)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:HEALthy {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:HEALthy \n
		Snippet: value: bool = driver.source.bb.gnss.svid.beidou.healthy.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates if the selected SV ID is healthy or not. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: healthy_state: 1| ON| 0| OFF 1 = healthy satellite The healthy state reflects the value of the corresponding healthy flag in the navigation message: [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:LNAV:EPHemeris:HEALth [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L1Health [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L2Health [:SOURcehw]:BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L5Health [:SOURcehw]:BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BDVS [:SOURcehw]:BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BHS [:SOURcehw]:BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E5BHS [:SOURcehw]:BB:GNSS:SVIDch:BEIDou:NMESsage:DNAV:EPHemeris:HEALth [:SOURcehw]:BB:GNSS:SVIDch:GLONass:NMESsage:NAV:EPHemeris:HEALth [:SOURcehw]:BB:GNSS:SVIDch:QZSS:NMESsage:NAV:EPHemeris:HEALth The values are interdependent; changing one of them changes the other."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:HEALthy?')
		return Conversions.str_to_bool(response)
