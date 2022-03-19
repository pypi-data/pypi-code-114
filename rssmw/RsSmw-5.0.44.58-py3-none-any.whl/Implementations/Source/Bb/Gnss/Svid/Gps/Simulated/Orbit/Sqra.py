from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sqra:
	"""Sqra commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sqra", core, parent)

	def set(self, sqrt_a: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SIMulated:ORBit:SQRA \n
		Snippet: driver.source.bb.gnss.svid.gps.simulated.orbit.sqra.set(sqrt_a = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the square root of semi-major axis. \n
			:param sqrt_a: integer Range: 0.190735 to 8192
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(sqrt_a)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SIMulated:ORBit:SQRA {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SIMulated:ORBit:SQRA \n
		Snippet: value: int = driver.source.bb.gnss.svid.gps.simulated.orbit.sqra.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the square root of semi-major axis. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: sqrt_a: integer Range: 0.190735 to 8192"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SIMulated:ORBit:SQRA?')
		return Conversions.str_to_int(response)
