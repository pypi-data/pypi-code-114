from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Velocity:
	"""Velocity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("velocity", core, parent)

	def set(self, velocity: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SDYNamics:VELocity \n
		Snippet: driver.source.bb.gnss.svid.navic.sdynamics.velocity.set(velocity = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the constant velocity. \n
			:param velocity: float Range: -19030 to 19030
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(velocity)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SDYNamics:VELocity {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SDYNamics:VELocity \n
		Snippet: value: float = driver.source.bb.gnss.svid.navic.sdynamics.velocity.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the constant velocity. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: velocity: float Range: -19030 to 19030"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SDYNamics:VELocity?')
		return Conversions.str_to_float(response)
