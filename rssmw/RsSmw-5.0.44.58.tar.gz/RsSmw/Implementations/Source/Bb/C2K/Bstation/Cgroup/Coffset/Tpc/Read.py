from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	def set(self, read: enums.TpcReadMode, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:READ \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.tpc.read.set(read = enums.TpcReadMode.CONTinuous, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the read out mode for the bit pattern of the power control bits. The bit pattern is defined with the
		commands BB:C2K:BST<n>:CGRoup<n>:COFFset<n>:TPC.... Power control is available for sub channel types F-DCCH and F-FCH.
		F-DCCH is only generated for radio configurations 3, 4 and 5. For the traffic channels, this value is specific for the
		selected radio configuration. \n
			:param read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the power control bit sequence continues with 0 bits. S1A The bit pattern is used once, then the power control bit sequence continues with 1 bit. S01A The bit pattern is used once and then the power control bit sequence is continued with 0 bits and 1 bit alternately. S10A The bit pattern is used once and then the power control bit sequence is continued with 1 bit and 0 bits alternately.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = Conversions.enum_scalar_to_str(read, enums.TpcReadMode)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:READ {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.TpcReadMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:READ \n
		Snippet: value: enums.TpcReadMode = driver.source.bb.c2K.bstation.cgroup.coffset.tpc.read.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the read out mode for the bit pattern of the power control bits. The bit pattern is defined with the
		commands BB:C2K:BST<n>:CGRoup<n>:COFFset<n>:TPC.... Power control is available for sub channel types F-DCCH and F-FCH.
		F-DCCH is only generated for radio configurations 3, 4 and 5. For the traffic channels, this value is specific for the
		selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the power control bit sequence continues with 0 bits. S1A The bit pattern is used once, then the power control bit sequence continues with 1 bit. S01A The bit pattern is used once and then the power control bit sequence is continued with 0 bits and 1 bit alternately. S10A The bit pattern is used once and then the power control bit sequence is continued with 1 bit and 0 bits alternately."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:READ?')
		return Conversions.str_to_scalar_enum(response, enums.TpcReadMode)
