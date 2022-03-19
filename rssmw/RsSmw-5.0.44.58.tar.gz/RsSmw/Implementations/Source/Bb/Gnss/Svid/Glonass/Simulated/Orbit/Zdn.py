from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zdn:
	"""Zdn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zdn", core, parent)

	def set(self, zn_dot: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIMulated:ORBit:ZDN \n
		Snippet: driver.source.bb.gnss.svid.glonass.simulated.orbit.zdn.set(zn_dot = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the velocity components X'n, Y'n and Z'n. \n
			:param zn_dot: float
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(zn_dot)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIMulated:ORBit:ZDN {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIMulated:ORBit:ZDN \n
		Snippet: value: float = driver.source.bb.gnss.svid.glonass.simulated.orbit.zdn.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the velocity components X'n, Y'n and Z'n. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: zn_dot: float"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIMulated:ORBit:ZDN?')
		return Conversions.str_to_float(response)
