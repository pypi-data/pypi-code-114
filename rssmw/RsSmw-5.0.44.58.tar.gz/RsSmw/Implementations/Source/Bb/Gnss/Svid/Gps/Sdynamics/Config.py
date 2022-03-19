from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	def set(self, predefined_config: enums.DopplerConfig, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SDYNamics:CONFig \n
		Snippet: driver.source.bb.gnss.svid.gps.sdynamics.config.set(predefined_config = enums.DopplerConfig.USER, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Selects between the predefined velocity profiles or a user-defined one. \n
			:param predefined_config: USER| VEL1| VEL2 USER User-defined Profile parametrs are configurable. VEL1 Low dynamics Profile parametrs are read-only. VEL2 High dynamics Profile parametrs are read-only.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(predefined_config, enums.DopplerConfig)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SDYNamics:CONFig {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.DopplerConfig:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SDYNamics:CONFig \n
		Snippet: value: enums.DopplerConfig = driver.source.bb.gnss.svid.gps.sdynamics.config.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Selects between the predefined velocity profiles or a user-defined one. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: predefined_config: USER| VEL1| VEL2 USER User-defined Profile parametrs are configurable. VEL1 Low dynamics Profile parametrs are read-only. VEL2 High dynamics Profile parametrs are read-only."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SDYNamics:CONFig?')
		return Conversions.str_to_scalar_enum(response, enums.DopplerConfig)
