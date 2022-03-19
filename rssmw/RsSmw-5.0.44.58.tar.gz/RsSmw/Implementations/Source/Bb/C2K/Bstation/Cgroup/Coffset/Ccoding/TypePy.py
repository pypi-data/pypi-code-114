from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.Cdma2KchanCoderType, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:CCODing:TYPE \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.ccoding.typePy.set(type_py = enums.Cdma2KchanCoderType.CON2, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the channel coding type. This value is only available for channel coding modes 'Complete' and 'Without
		Interleaving' (SOURce:BB:C2K:BST<n>:CGRoup<n>:COFFset<n>:CCODing:MODE COMP | NOIN) . For the traffic channels, this value
		is specific for the selected radio configuration. \n
			:param type_py: CON2| CON3| CON4| CON6| TUR2| TUR3| TUR4| TUR5| OFF| DEFault NONE No error protection TURx Turbo Coder of rate 1/x in accordance with the CDMA specifications. CONx Convolution Coder of rate 1/x with generator polynomials defined by CDMA.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.Cdma2KchanCoderType)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:CCODing:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.Cdma2KchanCoderType:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:CCODing:TYPE \n
		Snippet: value: enums.Cdma2KchanCoderType = driver.source.bb.c2K.bstation.cgroup.coffset.ccoding.typePy.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command sets the channel coding type. This value is only available for channel coding modes 'Complete' and 'Without
		Interleaving' (SOURce:BB:C2K:BST<n>:CGRoup<n>:COFFset<n>:CCODing:MODE COMP | NOIN) . For the traffic channels, this value
		is specific for the selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: type_py: CON2| CON3| CON4| CON6| TUR2| TUR3| TUR4| TUR5| OFF| DEFault NONE No error protection TURx Turbo Coder of rate 1/x in accordance with the CDMA specifications. CONx Convolution Coder of rate 1/x with generator polynomials defined by CDMA."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:CCODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KchanCoderType)
