from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RuSelection:
	"""RuSelection commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Station, default value after init: Station.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ruSelection", core, parent)
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

	def set(self, ru_sel_ch_1: enums.WlannFbPpduRuSel, frameBlock=repcap.FrameBlock.Default, station=repcap.Station.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CCH1:RUSelection<ST> \n
		Snippet: driver.source.bb.wlnn.fblock.cch1.ruSelection.set(ru_sel_ch_1 = enums.WlannFbPpduRuSel.RU0, frameBlock = repcap.FrameBlock.Default, station = repcap.Station.Default) \n
		For HE frames. Sets the resource unit allocation of the first content channel for the respective channel and station. \n
			:param ru_sel_ch_1: RU0| RU1| RU2| RU3| RU4| RU5| RU6| RU7| RU8| RU9| RU10| RU11| RU12| RU13| RU14| RU15| RU18| RU19| RU20| RU21| RU22| RU23| RU24| RU25| RU34| RU35| RU36| RU37| RU38| RU16| RU17| RU26| RU27| RU28| RU29| RU30| RU31| RU32| RU33
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RuSelection')
		"""
		param = Conversions.enum_scalar_to_str(ru_sel_ch_1, enums.WlannFbPpduRuSel)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CCH1:RUSelection{station_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default, station=repcap.Station.Default) -> enums.WlannFbPpduRuSel:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CCH1:RUSelection<ST> \n
		Snippet: value: enums.WlannFbPpduRuSel = driver.source.bb.wlnn.fblock.cch1.ruSelection.get(frameBlock = repcap.FrameBlock.Default, station = repcap.Station.Default) \n
		For HE frames. Sets the resource unit allocation of the first content channel for the respective channel and station. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RuSelection')
			:return: ru_sel_ch_1: RU0| RU1| RU2| RU3| RU4| RU5| RU6| RU7| RU8| RU9| RU10| RU11| RU12| RU13| RU14| RU15| RU18| RU19| RU20| RU21| RU22| RU23| RU24| RU25| RU34| RU35| RU36| RU37| RU38| RU16| RU17| RU26| RU27| RU28| RU29| RU30| RU31| RU32| RU33"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CCH1:RUSelection{station_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPpduRuSel)

	def clone(self) -> 'RuSelection':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RuSelection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
