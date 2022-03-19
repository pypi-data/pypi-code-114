from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def set(self, rate: enums.Cdma2KdataRate, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:DATA:RATE \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.data.rate.set(rate = enums.Cdma2KdataRate.DR1036K8, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the data rate for the specified channel. The value range depends on the channel type, the selected radio
		configuration and the frame length. Parameter NUSed is returned for channel 0-1 to 0-4. For the traffic channels, this
		value is specific for the selected radio configuration. The value range depends on the frame length. If the frame length
		is changed so that the set data rate becomes invalid, the next permissible value is automatically set. The data rate
		affects the Walsh code (spreading factor) that are possible within a channel. If a data rate is changed so that the
		selected Walsh code becomes invalid, the next permissible value is automatically set. \n
			:param rate: DR1K2| DR1K3| DR1K5| DR1K8| DR2K4| DR2K7| DR3K6| DR4K8| DR7K2| DR9K6| DR14K4| DR19K2| DR28K8| DR38K4| DR57K6| DR76K8| DR115K2| DR153K6| DR230K4| DR307K2| NUSed
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.Cdma2KdataRate)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:DATA:RATE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.Cdma2KdataRate:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:DATA:RATE \n
		Snippet: value: enums.Cdma2KdataRate = driver.source.bb.c2K.bstation.cgroup.coffset.data.rate.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the data rate for the specified channel. The value range depends on the channel type, the selected radio
		configuration and the frame length. Parameter NUSed is returned for channel 0-1 to 0-4. For the traffic channels, this
		value is specific for the selected radio configuration. The value range depends on the frame length. If the frame length
		is changed so that the set data rate becomes invalid, the next permissible value is automatically set. The data rate
		affects the Walsh code (spreading factor) that are possible within a channel. If a data rate is changed so that the
		selected Walsh code becomes invalid, the next permissible value is automatically set. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: rate: DR1K2| DR1K3| DR1K5| DR1K8| DR2K4| DR2K7| DR3K6| DR4K8| DR7K2| DR9K6| DR14K4| DR19K2| DR28K8| DR38K4| DR57K6| DR76K8| DR115K2| DR153K6| DR230K4| DR307K2| NUSed"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:DATA:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KdataRate)
