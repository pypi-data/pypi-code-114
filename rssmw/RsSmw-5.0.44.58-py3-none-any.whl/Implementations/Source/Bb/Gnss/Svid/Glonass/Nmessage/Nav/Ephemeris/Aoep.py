from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aoep:
	"""Aoep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aoep", core, parent)

	def set(self, age_of_ephemeris: enums.EphAge, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:AOEP \n
		Snippet: driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.aoep.set(age_of_ephemeris = enums.EphAge.A30M, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the age of ephemeris page - P1 parameter. \n
			:param age_of_ephemeris: A30M| A45M| A60M
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(age_of_ephemeris, enums.EphAge)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:AOEP {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.EphAge:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:AOEP \n
		Snippet: value: enums.EphAge = driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.aoep.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the age of ephemeris page - P1 parameter. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: age_of_ephemeris: A30M| A45M| A60M"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:AOEP?')
		return Conversions.str_to_scalar_enum(response, enums.EphAge)
