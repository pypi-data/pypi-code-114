from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CvPeriod:
	"""CvPeriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cvPeriod", core, parent)

	def set(self, const_vel_period: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SDYNamics:CVPeriod \n
		Snippet: driver.source.bb.gnss.svid.glonass.sdynamics.cvPeriod.set(const_vel_period = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the time period during that the velocity is kept constant. \n
			:param const_vel_period: float Range: 0.1 to 10800
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(const_vel_period)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SDYNamics:CVPeriod {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SDYNamics:CVPeriod \n
		Snippet: value: float = driver.source.bb.gnss.svid.glonass.sdynamics.cvPeriod.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the time period during that the velocity is kept constant. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: const_vel_period: float Range: 0.1 to 10800"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SDYNamics:CVPeriod?')
		return Conversions.str_to_float(response)
