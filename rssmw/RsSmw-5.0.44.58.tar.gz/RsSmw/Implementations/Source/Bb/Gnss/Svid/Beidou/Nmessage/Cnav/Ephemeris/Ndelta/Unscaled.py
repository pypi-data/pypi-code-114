from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unscaled:
	"""Unscaled commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unscaled", core, parent)

	def set(self, delta_n: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:NMESsage:CNAV:EPHemeris:NDELta:UNSCaled \n
		Snippet: driver.source.bb.gnss.svid.beidou.nmessage.cnav.ephemeris.ndelta.unscaled.set(delta_n = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the mean motion difference delta. \n
			:param delta_n: integer
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(delta_n)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:NMESsage:CNAV:EPHemeris:NDELta:UNSCaled {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:BEIDou:NMESsage:CNAV:EPHemeris:NDELta:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.svid.beidou.nmessage.cnav.ephemeris.ndelta.unscaled.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the mean motion difference delta. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: delta_n: integer"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:BEIDou:NMESsage:CNAV:EPHemeris:NDELta:UNSCaled?')
		return Conversions.str_to_float(response)
