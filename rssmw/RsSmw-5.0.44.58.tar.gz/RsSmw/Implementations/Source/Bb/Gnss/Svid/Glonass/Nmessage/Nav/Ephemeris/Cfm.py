from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfm:
	"""Cfm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfm", core, parent)

	def set(self, field_m: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:CFM \n
		Snippet: driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.cfm.set(field_m = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param field_m: No help available
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(field_m)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:CFM {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:CFM \n
		Snippet: value: int = driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.cfm.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: field_m: No help available"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:CFM?')
		return Conversions.str_to_int(response)
