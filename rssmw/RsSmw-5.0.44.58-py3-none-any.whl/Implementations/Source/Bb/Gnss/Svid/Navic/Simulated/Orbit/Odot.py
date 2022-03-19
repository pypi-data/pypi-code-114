from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Odot:
	"""Odot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("odot", core, parent)

	def set(self, omega_dot: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SIMulated:ORBit:ODOT \n
		Snippet: driver.source.bb.gnss.svid.navic.simulated.orbit.odot.set(omega_dot = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the rate of right ascension. \n
			:param omega_dot: float
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(omega_dot)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SIMulated:ORBit:ODOT {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SIMulated:ORBit:ODOT \n
		Snippet: value: float = driver.source.bb.gnss.svid.navic.simulated.orbit.odot.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the rate of right ascension. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: omega_dot: float"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SIMulated:ORBit:ODOT?')
		return Conversions.str_to_float(response)
