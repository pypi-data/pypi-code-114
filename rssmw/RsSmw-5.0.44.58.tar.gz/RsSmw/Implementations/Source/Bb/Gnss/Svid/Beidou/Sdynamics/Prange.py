from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prange:
	"""Prange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prange", core, parent)

	def set(self, prange: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:SDYNamics:PRANge \n
		Snippet: driver.source.bb.gnss.svid.beidou.sdynamics.prange.set(prange = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the initial pseudorange. \n
			:param prange: float Range: 0 to 119900000
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(prange)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:SDYNamics:PRANge {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:SDYNamics:PRANge \n
		Snippet: value: float = driver.source.bb.gnss.svid.beidou.sdynamics.prange.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the initial pseudorange. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: prange: float Range: 0 to 119900000"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:SDYNamics:PRANge?')
		return Conversions.str_to_float(response)
