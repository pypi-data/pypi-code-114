from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flength:
	"""Flength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flength", core, parent)

	def set(self, flength: enums.Cdma2KframLen, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:FLENgth \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.flength.set(flength = enums.Cdma2KframLen._10, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the frame length of the selected channel. The value range is channel specific. For the traffic channels,
		this value is specific for the selected radio configuration. The value range of the frame length depends on the channel
		type and the selected radio configuration. The frame length affects the data rates that are possible within a channel.
		Changing the frame length can lead to a change of data rate and this in turn can bring about a change of Walsh code. \n
			:param flength: 5| 10| 20| 26.6| 40| 80| 160| NUSed 26 ms Frame length of 26.6. Also all inputs 26.6 ms and 26.7 ms are allowed.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = Conversions.enum_scalar_to_str(flength, enums.Cdma2KframLen)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:FLENgth {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.Cdma2KframLen:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:FLENgth \n
		Snippet: value: enums.Cdma2KframLen = driver.source.bb.c2K.bstation.cgroup.coffset.flength.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the frame length of the selected channel. The value range is channel specific. For the traffic channels,
		this value is specific for the selected radio configuration. The value range of the frame length depends on the channel
		type and the selected radio configuration. The frame length affects the data rates that are possible within a channel.
		Changing the frame length can lead to a change of data rate and this in turn can bring about a change of Walsh code. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: flength: 5| 10| 20| 26.6| 40| 80| 160| NUSed 26 ms Frame length of 26.6. Also all inputs 26.6 ms and 26.7 ms are allowed."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:FLENgth?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KframLen)
