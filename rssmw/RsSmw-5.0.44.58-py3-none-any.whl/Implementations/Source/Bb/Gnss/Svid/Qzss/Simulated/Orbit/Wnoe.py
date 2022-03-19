from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wnoe:
	"""Wnoe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wnoe", core, parent)

	def set(self, sim_toe: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIMulated:ORBit:WNOE \n
		Snippet: driver.source.bb.gnss.svid.qzss.simulated.orbit.wnoe.set(sim_toe = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference week. \n
			:param sim_toe: integer Range: 0 to 10000
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(sim_toe)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIMulated:ORBit:WNOE {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIMulated:ORBit:WNOE \n
		Snippet: value: int = driver.source.bb.gnss.svid.qzss.simulated.orbit.wnoe.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference week. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: sim_toe: integer Range: 0 to 10000"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIMulated:ORBit:WNOE?')
		return Conversions.str_to_int(response)
