from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Yaw:
	"""Yaw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("yaw", core, parent)

	def set(self, yaw: float, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ATTitude:YAW \n
		Snippet: driver.source.bb.gnss.receiver.v.attitude.yaw.set(yaw = 1.0, vehicle = repcap.Vehicle.Default) \n
		Sets the attitude parameters relative to the local horizon. \n
			:param yaw: float Range: -180 to 180
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.decimal_value_to_str(yaw)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ATTitude:YAW {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ATTitude:YAW \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.attitude.yaw.get(vehicle = repcap.Vehicle.Default) \n
		Sets the attitude parameters relative to the local horizon. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: yaw: No help available"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ATTitude:YAW?')
		return Conversions.str_to_float(response)
