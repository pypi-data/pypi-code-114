from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, power_offset: float, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SIGNal:L5Band:EL5S<US>:POWer:OFFset \n
		Snippet: driver.source.bb.gnss.svid.sbas.signal.l5Band.el5S.power.offset.set(power_offset = 1.0, satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Sets a power offset for the selected signal. \n
			:param power_offset: float Range: -6 to 0
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'El5S')
		"""
		param = Conversions.decimal_value_to_str(power_offset)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SIGNal:L5Band:EL5S{index_cmd_val}:POWer:OFFset {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SIGNal:L5Band:EL5S<US>:POWer:OFFset \n
		Snippet: value: float = driver.source.bb.gnss.svid.sbas.signal.l5Band.el5S.power.offset.get(satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Sets a power offset for the selected signal. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'El5S')
			:return: power_offset: float Range: -6 to 0"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SIGNal:L5Band:EL5S{index_cmd_val}:POWer:OFFset?')
		return Conversions.str_to_float(response)
