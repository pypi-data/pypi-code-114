from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def set(self, max_jerk: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SDYNamics:JERK:MAX \n
		Snippet: driver.source.bb.gnss.svid.qzss.sdynamics.jerk.max.set(max_jerk = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the maximum jerk. \n
			:param max_jerk: float Range: 0.1 to 7E4
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(max_jerk)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SDYNamics:JERK:MAX {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SDYNamics:JERK:MAX \n
		Snippet: value: float = driver.source.bb.gnss.svid.qzss.sdynamics.jerk.max.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the maximum jerk. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: max_jerk: float Range: 0.1 to 7E4"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SDYNamics:JERK:MAX?')
		return Conversions.str_to_float(response)
