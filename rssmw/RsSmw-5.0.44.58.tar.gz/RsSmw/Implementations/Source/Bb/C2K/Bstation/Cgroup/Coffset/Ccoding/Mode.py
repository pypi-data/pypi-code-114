from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.Cdma2KcodMode, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:CCODing:MODE \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.ccoding.mode.set(mode = enums.Cdma2KcodMode.COMPlete, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		Selects channel coding mode. For the traffic channels, this value is specific for the selected radio configuration. \n
			:param mode: OFF| COMPlete| NOINterleaving| OINTerleaving OFF Channel coding is deactivated. COMPlete The complete channel coding is performed. The channel coding procedure can slightly vary depending on channel type, frame length and data rate. OINTerleaving Except for the block interleaver, the whole channel coding procedure is carried out. In this mode, the frame structure and the convolutional coder of a receiver can be tested. NOINterleaving In this mode, only block interleaver is used for coding. This allows the deinterleaver in the receiver to be tested independently of the remaining (de-) coding process.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Cdma2KcodMode)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:CCODing:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.Cdma2KcodMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:CCODing:MODE \n
		Snippet: value: enums.Cdma2KcodMode = driver.source.bb.c2K.bstation.cgroup.coffset.ccoding.mode.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		Selects channel coding mode. For the traffic channels, this value is specific for the selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: mode: OFF| COMPlete| NOINterleaving| OINTerleaving OFF Channel coding is deactivated. COMPlete The complete channel coding is performed. The channel coding procedure can slightly vary depending on channel type, frame length and data rate. OINTerleaving Except for the block interleaver, the whole channel coding procedure is carried out. In this mode, the frame structure and the convolutional coder of a receiver can be tested. NOINterleaving In this mode, only block interleaver is used for coding. This allows the deinterleaver in the receiver to be tested independently of the remaining (de-) coding process."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:CCODing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KcodMode)
