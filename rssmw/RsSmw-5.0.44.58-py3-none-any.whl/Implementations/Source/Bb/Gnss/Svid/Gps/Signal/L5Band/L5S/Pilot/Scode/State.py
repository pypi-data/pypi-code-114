from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SIGNal:L5Band:L5S:PILot:SCODe:[STATe] \n
		Snippet: driver.source.bb.gnss.svid.gps.signal.l5Band.l5S.pilot.scode.state.set(state = False, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Activates the secondary code in the data/pilot channel. \n
			:param state: 1| ON| 0| OFF
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.bool_to_str(state)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SIGNal:L5Band:L5S:PILot:SCODe:STATe {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SIGNal:L5Band:L5S:PILot:SCODe:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.svid.gps.signal.l5Band.l5S.pilot.scode.state.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Activates the secondary code in the data/pilot channel. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: state: 1| ON| 0| OFF"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SIGNal:L5Band:L5S:PILot:SCODe:STATe?')
		return Conversions.str_to_bool(response)
