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

	def set(self, toc: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:CCORrection:TOC:UNSCaled \n
		Snippet: driver.source.bb.gnss.svid.galileo.nmessage.inav.ccorrection.toc.unscaled.set(toc = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference time of clock. \n
			:param toc: integer
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(toc)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:CCORrection:TOC:UNSCaled {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:CCORrection:TOC:UNSCaled \n
		Snippet: value: int = driver.source.bb.gnss.svid.galileo.nmessage.inav.ccorrection.toc.unscaled.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference time of clock. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: toc: integer"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:CCORrection:TOC:UNSCaled?')
		return Conversions.str_to_int(response)
