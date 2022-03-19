from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............Internal.Utilities import trim_str_response
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, dselect: str, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:DSELect \n
		Snippet: driver.source.bb.gnss.svid.qzss.signal.l1Band.l1C.data.nmessage.dselect.set(dselect = '1', satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param dselect: No help available
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.value_to_quoted_str(dselect)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:DSELect {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:DSELect \n
		Snippet: value: str = driver.source.bb.gnss.svid.qzss.signal.l1Band.l1C.data.nmessage.dselect.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: dselect: No help available"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:DSELect?')
		return trim_str_response(response)
