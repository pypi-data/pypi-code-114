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

	def set(self, bgd: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:CCORrection:BGDA:UNSCaled \n
		Snippet: driver.source.bb.gnss.svid.galileo.nmessage.inav.ccorrection.bgda.unscaled.set(bgd = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the broadcast group delay. \n
			:param bgd: integer Range: -512 to 511
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(bgd)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:CCORrection:BGDA:UNSCaled {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:CCORrection:BGDA:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.svid.galileo.nmessage.inav.ccorrection.bgda.unscaled.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the broadcast group delay. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: bgd: integer Range: -512 to 511"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:CCORrection:BGDA:UNSCaled?')
		return Conversions.str_to_float(response)
