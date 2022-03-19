from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> enums.Cdma2KchanTypeDn:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TYPE \n
		Snippet: value: enums.Cdma2KchanTypeDn = driver.source.bb.c2K.bstation.cgroup.coffset.typePy.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		Queries the channel type. The channel type is firmly fixed for channel numbers 0-1 to 0-14 (CGR0:COFF1 to CGR0:COFF14) ,
		i.e. for the special channels (control and packet channels) . The remaining channel numbers are assigned to the
		individual code channels of the eight possible traffic channels. In this case, the first traffic channel occupies the
		range 1-1 to 1-8 (CGR1:COFF1 to CGR1:COFF8) , the second occupies the range 2-1 to 2-8 (CGR2:COFF1 to CGR2:COFF8) , etc.
		Since the type and number of code channels depends on the radio configuration of the channel, the channels x-2 to x-8 are
		variously occupied. X-1 is always the fundamental channel (F-FCH) of the traffic channel. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: type_py: F-PICH| F-SYNC| F-PCH| F-TDPICH| F-APICH| F-ATDPICH| F-BCH| F-QPCH| F-CPCCH| F-CACH| F-CCCH| F-DCCH| F-FCH| F-SCH| F-PDCCH| F-PDCH"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KchanTypeDn)
