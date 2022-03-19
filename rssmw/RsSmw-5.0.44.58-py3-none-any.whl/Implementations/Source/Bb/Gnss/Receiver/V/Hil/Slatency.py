from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slatency:
	"""Slatency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slatency", core, parent)

	def set(self, system_latency: float, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:HIL:SLATency \n
		Snippet: driver.source.bb.gnss.receiver.v.hil.slatency.set(system_latency = 1.0, vehicle = repcap.Vehicle.Default) \n
		Sets the time delay between the time specified with the parameter <ElapsedTime> in the HIL mode A position data command
		and the time this command is executed in the R&S SMW. See also 'System latency'. You can use the retrieved value for
		latency calibration, see 'Latency calibration'. \n
			:param system_latency: float Range: 0.002 to 0.15, Unit: s
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.decimal_value_to_str(system_latency)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:HIL:SLATency {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:HIL:SLATency \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.hil.slatency.get(vehicle = repcap.Vehicle.Default) \n
		Sets the time delay between the time specified with the parameter <ElapsedTime> in the HIL mode A position data command
		and the time this command is executed in the R&S SMW. See also 'System latency'. You can use the retrieved value for
		latency calibration, see 'Latency calibration'. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: system_latency: float Range: 0.002 to 0.15, Unit: s"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:HIL:SLATency?')
		return Conversions.str_to_float(response)
