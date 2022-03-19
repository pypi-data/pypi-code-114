from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Latency:
	"""Latency commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("latency", core, parent)

	@property
	def statistics(self):
		"""statistics commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import Statistics
			self._statistics = Statistics(self._core, self._cmd_group)
		return self._statistics

	def get(self, vehicle=repcap.Vehicle.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RT:RECeiver:[V<ST>]:HILPosition:LATency \n
		Snippet: value: float = driver.source.bb.gnss.rt.receiver.v.hilPosition.latency.get(vehicle = repcap.Vehicle.Default) \n
		Queries the time delay (or prediction latency) between the time specified with the parameter <ElapsedTime> in the HIL
		mode A position data command and the time this command is executed in the R&S SMW. You can use the retrieved value for
		latency calibration, see 'Latency calibration'. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: latency: float Range: min to max, Unit: s"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RT:RECeiver:V{vehicle_cmd_val}:HILPosition:LATency?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Latency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Latency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
