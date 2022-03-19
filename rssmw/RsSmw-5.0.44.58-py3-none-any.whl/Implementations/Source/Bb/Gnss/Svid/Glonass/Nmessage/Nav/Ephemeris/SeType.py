from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeType:
	"""SeType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seType", core, parent)

	def set(self, sat_type: enums.EphSatType, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:SEType \n
		Snippet: driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.seType.set(sat_type = enums.EphSatType.GLO, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the satellite ephemeris type - M parameter. \n
			:param sat_type: GLO| GLOM
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(sat_type, enums.EphSatType)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:SEType {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.EphSatType:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:NMESsage:NAV:EPHemeris:SEType \n
		Snippet: value: enums.EphSatType = driver.source.bb.gnss.svid.glonass.nmessage.nav.ephemeris.seType.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the satellite ephemeris type - M parameter. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: sat_type: GLO| GLOM"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:NMESsage:NAV:EPHemeris:SEType?')
		return Conversions.str_to_scalar_enum(response, enums.EphSatType)
