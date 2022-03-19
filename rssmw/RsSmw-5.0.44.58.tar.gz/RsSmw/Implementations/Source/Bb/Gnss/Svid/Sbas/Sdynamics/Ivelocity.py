from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ivelocity:
	"""Ivelocity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ivelocity", core, parent)

	def set(self, initial_velocity: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SDYNamics:IVELocity \n
		Snippet: driver.source.bb.gnss.svid.sbas.sdynamics.ivelocity.set(initial_velocity = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates the initial velocity, used at the beginning of the profile. \n
			:param initial_velocity: float Range: -19042 to 19042
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(initial_velocity)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SDYNamics:IVELocity {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SDYNamics:IVELocity \n
		Snippet: value: float = driver.source.bb.gnss.svid.sbas.sdynamics.ivelocity.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates the initial velocity, used at the beginning of the profile. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: initial_velocity: float Range: -19042 to 19042"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SDYNamics:IVELocity?')
		return Conversions.str_to_float(response)
