from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Misuse:
	"""Misuse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("misuse", core, parent)

	def set(self, misuse: bool, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:MISuse \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.tpc.misuse.set(misuse = False, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command activates 'mis-' use of the power control bits of the selected F-DCCH or F- FCH for controlling the channel
		powers of these channels. Power control is available for sub channel types F-DCCH and F-FCH. F-DCCH is only generated for
		radio configurations 3, 4 and 5. The bit pattern (see commands BB:C2K:BSTation<n>:CGRoup<n>:COFFset<n>:TPC...) of the
		power control bits of each channel is used to control the channel power. A '1' leads to an increase of channel powers, a
		'0' to a reduction of channel powers. Channel power is limited to the range 0 dB to -80 dB. The step width of the change
		is defined with the command [:SOURce<hw>]:BB:C2K:BSTation<st>:CGRoup<di0>:COFFset<ch>:TPC:PSTep. For the traffic channels,
		this value is specific for the selected radio configuration. \n
			:param misuse: 1| ON| 0| OFF
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = Conversions.bool_to_str(misuse)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:MISuse {param}')

	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:MISuse \n
		Snippet: value: bool = driver.source.bb.c2K.bstation.cgroup.coffset.tpc.misuse.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command activates 'mis-' use of the power control bits of the selected F-DCCH or F- FCH for controlling the channel
		powers of these channels. Power control is available for sub channel types F-DCCH and F-FCH. F-DCCH is only generated for
		radio configurations 3, 4 and 5. The bit pattern (see commands BB:C2K:BSTation<n>:CGRoup<n>:COFFset<n>:TPC...) of the
		power control bits of each channel is used to control the channel power. A '1' leads to an increase of channel powers, a
		'0' to a reduction of channel powers. Channel power is limited to the range 0 dB to -80 dB. The step width of the change
		is defined with the command [:SOURce<hw>]:BB:C2K:BSTation<st>:CGRoup<di0>:COFFset<ch>:TPC:PSTep. For the traffic channels,
		this value is specific for the selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: misuse: 1| ON| 0| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:MISuse?')
		return Conversions.str_to_bool(response)
