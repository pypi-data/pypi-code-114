from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ozero:
	"""Ozero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ozero", core, parent)

	def set(self, omega_0: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:SIMulated:ORBit:OZERo \n
		Snippet: driver.source.bb.gnss.svid.galileo.simulated.orbit.ozero.set(omega_0 = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the longitude of ascending node. \n
			:param omega_0: float
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(omega_0)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:SIMulated:ORBit:OZERo {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:SIMulated:ORBit:OZERo \n
		Snippet: value: float = driver.source.bb.gnss.svid.galileo.simulated.orbit.ozero.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the longitude of ascending node. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: omega_0: float"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:SIMulated:ORBit:OZERo?')
		return Conversions.str_to_float(response)
