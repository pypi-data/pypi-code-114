from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, bandwidth: List[float], offset_freq: float, lower_cut_freq: float, upper_cut_freq: float, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:CUSTom:DATA \n
		Snippet: driver.source.fsimulator.delay.group.path.custom.data.set(bandwidth = [1.1, 2.2, 3.3], offset_freq = 1.0, lower_cut_freq = 1.0, upper_cut_freq = 1.0, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the parameters of the custom fading profile. \n
			:param bandwidth: float Range: 50 to 40000, Unit: Hz
			:param offset_freq: float Range: -23950 to 23950, Unit: Hz
			:param lower_cut_freq: float Range: -4000 to 3950, Unit: Hz
			:param upper_cut_freq: float Range: -3950 to 4000, Unit: Hz
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('bandwidth', bandwidth, DataType.FloatList, None), ArgSingle('offset_freq', offset_freq, DataType.Float), ArgSingle('lower_cut_freq', lower_cut_freq, DataType.Float), ArgSingle('upper_cut_freq', upper_cut_freq, DataType.Float))
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CUSTom:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Bandwidth: List[float]: float Range: 50 to 40000, Unit: Hz
			- Offset_Freq: float: float Range: -23950 to 23950, Unit: Hz
			- Lower_Cut_Freq: float: float Range: -4000 to 3950, Unit: Hz
			- Upper_Cut_Freq: float: float Range: -3950 to 4000, Unit: Hz"""
		__meta_args_list = [
			ArgStruct('Bandwidth', DataType.FloatList, None, False, True, 1),
			ArgStruct.scalar_float('Offset_Freq'),
			ArgStruct.scalar_float('Lower_Cut_Freq'),
			ArgStruct.scalar_float('Upper_Cut_Freq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bandwidth: List[float] = None
			self.Offset_Freq: float = None
			self.Lower_Cut_Freq: float = None
			self.Upper_Cut_Freq: float = None

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> DataStruct:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:CUSTom:DATA \n
		Snippet: value: DataStruct = driver.source.fsimulator.delay.group.path.custom.data.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the parameters of the custom fading profile. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		return self._core.io.query_struct(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CUSTom:DATA?', self.__class__.DataStruct())
