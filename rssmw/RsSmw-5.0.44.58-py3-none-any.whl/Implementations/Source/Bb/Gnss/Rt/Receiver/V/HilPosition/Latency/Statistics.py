from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Statistics:
	"""Statistics commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistics", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Last_Latency: List[float]: float Time delay between the time specified with the parameter ElapsedTime in a HIL command and the time this command is executed in the R&S SMW. Unit: s
			- Max_Latency: float: float The largest latency value since the last time this query was sent. Unit: s
			- Min_Latency: float: float The smallest latency value since the last time this query was sent. Unit: s
			- No_Zero_Values: int: integer Number of non-zero latency values since the last time this query was sent.
			- Total_Values: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Last_Latency', DataType.FloatList, None, False, True, 1),
			ArgStruct.scalar_float('Max_Latency'),
			ArgStruct.scalar_float('Min_Latency'),
			ArgStruct.scalar_int('No_Zero_Values'),
			ArgStruct.scalar_int('Total_Values')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Last_Latency: List[float] = None
			self.Max_Latency: float = None
			self.Min_Latency: float = None
			self.No_Zero_Values: int = None
			self.Total_Values: int = None

	def get(self, vehicle=repcap.Vehicle.Default) -> GetStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RT:RECeiver:[V<ST>]:HILPosition:LATency:STATistics \n
		Snippet: value: GetStruct = driver.source.bb.gnss.rt.receiver.v.hilPosition.latency.statistics.get(vehicle = repcap.Vehicle.Default) \n
		Queries the current latency tcal.latency,i and statistics on the latency values. This command returns also information on
		the minimum and maximal deviation from zero latency and the number of non-zero latency values measured since the last
		time this query was sent.
			INTRO_CMD_HELP: The following terms are used: \n
			- HIL command refers to the command [:SOURce<hw>]:BB:GNSS:RT:RECeiver[:V<st>]:HILPosition:MODE:A or
			- Dropped commands are commands that are evaluated, buffered but not applied because they become outdated as more up-to-date information is received
			- Returned values apply for the period from the last time the query was sent.
		See also 'Latency calibration'. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GNSS:RT:RECeiver:V{vehicle_cmd_val}:HILPosition:LATency:STATistics?', self.__class__.GetStruct())
