from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rconfiguration:
	"""Rconfiguration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rconfiguration", core, parent)

	def set(self, rconfiguration: enums.Cdma2KradioConf, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:RCONfiguration \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.rconfiguration.set(rconfiguration = enums.Cdma2KradioConf._1, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default) \n
		Selects the radio configuration for the traffic channel. The settings of the channel table parameters are specific for
		the selected radio configuration. \n
			:param rconfiguration: 1| 2| 3| 4| 5
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
		"""
		param = Conversions.enum_scalar_to_str(rconfiguration, enums.Cdma2KradioConf)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:RCONfiguration {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default) -> enums.Cdma2KradioConf:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:RCONfiguration \n
		Snippet: value: enums.Cdma2KradioConf = driver.source.bb.c2K.bstation.cgroup.rconfiguration.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default) \n
		Selects the radio configuration for the traffic channel. The settings of the channel table parameters are specific for
		the selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:return: rconfiguration: 1| 2| 3| 4| 5"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:RCONfiguration?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KradioConf)
