from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spuncture:
	"""Spuncture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spuncture", core, parent)

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.Cdma2KchanCodSymbPunc:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:CCODing:SPUNcture \n
		Snippet: value: enums.Cdma2KchanCodSymbPunc = driver.source.bb.c2K.bstation.cgroup.coffset.ccoding.spuncture.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command queries the symbol puncture rate. This value is only available for channel coding modes 'Complete' and
		'Without Interleaving' (SOURce:BB:C2K:BST<n>:CGRoup<n>:COFFset<n>:CCODing:MODE COMP | NOIN) . For the traffic channels,
		this value is specific for the selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: spuncture: 8OF24| 1OF5| 1OF9| 4OF12| 2OF18| 2OF6| T2OF18| T4OF12| NONE xOFy a symbol puncture rate of x out of y is used TxOFy a symbol puncture rate of x out of y Turbo is used"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:CCODing:SPUNcture?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KchanCodSymbPunc)
