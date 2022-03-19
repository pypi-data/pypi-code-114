from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Profile:
	"""Profile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profile", core, parent)

	def set(self, profile: enums.Doppler, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SDYNamics:PROFile \n
		Snippet: driver.source.bb.gnss.svid.gps.sdynamics.profile.set(profile = enums.Doppler.CONStant, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Selects the dynamics profile type. \n
			:param profile: CONStant| HIGH CONStant Constant velocity as set with the command [:SOURcehw]:BB:GNSS:SVIDch:GPS:SDYNamics:VELocity. HIGH Profiles with higher-order dynamics as set with the command [:SOURcehw]:BB:GNSS:SVIDch:GPS:SDYNamics:CONFig.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(profile, enums.Doppler)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SDYNamics:PROFile {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.Doppler:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SDYNamics:PROFile \n
		Snippet: value: enums.Doppler = driver.source.bb.gnss.svid.gps.sdynamics.profile.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Selects the dynamics profile type. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: profile: CONStant| HIGH CONStant Constant velocity as set with the command [:SOURcehw]:BB:GNSS:SVIDch:GPS:SDYNamics:VELocity. HIGH Profiles with higher-order dynamics as set with the command [:SOURcehw]:BB:GNSS:SVIDch:GPS:SDYNamics:CONFig."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SDYNamics:PROFile?')
		return Conversions.str_to_scalar_enum(response, enums.Doppler)
