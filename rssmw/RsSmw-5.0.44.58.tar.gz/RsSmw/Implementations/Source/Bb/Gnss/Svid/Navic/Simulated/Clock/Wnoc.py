from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wnoc:
	"""Wnoc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wnoc", core, parent)

	def set(self, toc: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SIMulated:CLOCk:WNOC \n
		Snippet: driver.source.bb.gnss.svid.navic.simulated.clock.wnoc.set(toc = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference week. \n
			:param toc: integer Range: 0 to 10000
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(toc)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SIMulated:CLOCk:WNOC {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SIMulated:CLOCk:WNOC \n
		Snippet: value: int = driver.source.bb.gnss.svid.navic.simulated.clock.wnoc.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference week. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: toc: integer Range: 0 to 10000"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SIMulated:CLOCk:WNOC?')
		return Conversions.str_to_int(response)
