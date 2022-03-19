from typing import List

from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIGNal:L5Band:L3CDma<US>:DATA:NMESsage:PATTern \n
		Snippet: driver.source.bb.gnss.svid.glonass.signal.l5Band.l3Cdma.data.nmessage.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		No command help available \n
			:param pattern: No help available
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'L3Cdma')
		"""
		param = Conversions.list_to_csv_str(pattern)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIGNal:L5Band:L3CDma{index_cmd_val}:DATA:NMESsage:PATTern {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIGNal:L5Band:L3CDma<US>:DATA:NMESsage:PATTern \n
		Snippet: value: List[str] = driver.source.bb.gnss.svid.glonass.signal.l5Band.l3Cdma.data.nmessage.pattern.get(satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		No command help available \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'L3Cdma')
			:return: pattern: No help available"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIGNal:L5Band:L3CDma{index_cmd_val}:DATA:NMESsage:PATTern?')
		return Conversions.str_to_str_list(response)
