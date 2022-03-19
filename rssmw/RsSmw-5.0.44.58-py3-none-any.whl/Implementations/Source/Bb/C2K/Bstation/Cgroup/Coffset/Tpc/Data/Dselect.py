from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, dselect: str, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:DATA:DSELect \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.tpc.data.dselect.set(dselect = '1', baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command selects the data list for the DLISt data source selection. Power control is available for sub channel types
		F-DCCH and F-FCH. F-DCCH is only generated for radio configurations 3, 4 and 5. The lists are stored as files with the
		fixed file extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the following commands is
		defined with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have
		to give the file name, without the path and the file extension. For the traffic channels, this value is specific for the
		selected radio configuration. \n
			:param dselect: string
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = Conversions.value_to_quoted_str(dselect)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:DATA:DSELect {param}')

	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:DATA:DSELect \n
		Snippet: value: str = driver.source.bb.c2K.bstation.cgroup.coffset.tpc.data.dselect.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		The command selects the data list for the DLISt data source selection. Power control is available for sub channel types
		F-DCCH and F-FCH. F-DCCH is only generated for radio configurations 3, 4 and 5. The lists are stored as files with the
		fixed file extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the following commands is
		defined with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have
		to give the file name, without the path and the file extension. For the traffic channels, this value is specific for the
		selected radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: dselect: string"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:DATA:DSELect?')
		return trim_str_response(response)
