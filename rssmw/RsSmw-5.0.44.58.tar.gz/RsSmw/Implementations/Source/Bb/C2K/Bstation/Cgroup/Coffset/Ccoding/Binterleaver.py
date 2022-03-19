from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Binterleaver:
	"""Binterleaver commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("binterleaver", core, parent)

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.Cdma2KchanCodBlkIlea:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:CCODing:BINTerleaver \n
		Snippet: value: enums.Cdma2KchanCodBlkIlea = driver.source.bb.c2K.bstation.cgroup.coffset.ccoding.binterleaver.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command queries the number of symbols per block which are processed by the interleaver. This value is only available
		for channel coding modes 'Complete' and 'Without Interleaving' (SOURce:BB:C2K:BST<n>:CGRoup<n>:COFFset<n>:CCODing:MODE
		COMP | NOIN) . For the traffic channels, this value is specific for the selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: binterleaver: 48| 96| 128| 144| 192| 288| 384| 576| 768| 1152| 1536| 2304| 3072| 4608| 6144| 9216| 12288| 18432| 36864| NONE"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:CCODing:BINTerleaver?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KchanCodBlkIlea)
