from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MuNum:
	"""MuNum commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Station, default value after init: Station.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("muNum", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_station_get', 'repcap_station_set', repcap.Station.Nr1)

	def repcap_station_set(self, station: repcap.Station) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Station.Default
		Default value after init: Station.Nr1"""
		self._cmd_group.set_repcap_enum_value(station)

	def repcap_station_get(self) -> repcap.Station:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, mu_num_ch_2: int, frameBlock=repcap.FrameBlock.Default, station=repcap.Station.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CCH2:MUNum<ST> \n
		Snippet: driver.source.bb.wlnn.fblock.cch2.muNum.set(mu_num_ch_2 = 1, frameBlock = repcap.FrameBlock.Default, station = repcap.Station.Default) \n
		Sets the number of MU-MIMO users for each RU and station of the second content channel. \n
			:param mu_num_ch_2: integer Range: 0 to 8
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'MuNum')
		"""
		param = Conversions.decimal_value_to_str(mu_num_ch_2)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CCH2:MUNum{station_cmd_val} {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, station=repcap.Station.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CCH2:MUNum<ST> \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.cch2.muNum.get(frameBlock = repcap.FrameBlock.Default, station = repcap.Station.Default) \n
		Sets the number of MU-MIMO users for each RU and station of the second content channel. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'MuNum')
			:return: mu_num_ch_2: integer Range: 0 to 8"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CCH2:MUNum{station_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'MuNum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MuNum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
