from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unscaled:
	"""Unscaled commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unscaled", core, parent)

	def set(self, isc_l_5_q_5: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:CNAV:CCORection:ISC:L5Q:UNSCaled \n
		Snippet: driver.source.bb.gnss.svid.gps.nmessage.cnav.ccorrection.isc.l5Q.unscaled.set(isc_l_5_q_5 = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the inter-signal corrections (ISC) parameters of the GPS/QZSS CNAV message. \n
			:param isc_l_5_q_5: integer Range: -4096 to 4095
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(isc_l_5_q_5)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:CNAV:CCORection:ISC:L5Q:UNSCaled {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:CNAV:CCORection:ISC:L5Q:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.svid.gps.nmessage.cnav.ccorrection.isc.l5Q.unscaled.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the inter-signal corrections (ISC) parameters of the GPS/QZSS CNAV message. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: isc_l_5_q_5: No help available"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:CNAV:CCORection:ISC:L5Q:UNSCaled?')
		return Conversions.str_to_float(response)
