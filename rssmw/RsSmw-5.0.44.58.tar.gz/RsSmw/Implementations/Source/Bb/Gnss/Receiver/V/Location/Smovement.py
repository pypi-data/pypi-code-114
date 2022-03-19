from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smovement:
	"""Smovement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smovement", core, parent)

	def set(self, smooth_movement: bool, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:SMOVement \n
		Snippet: driver.source.bb.gnss.receiver.v.location.smovement.set(smooth_movement = False, vehicle = repcap.Vehicle.Default) \n
		Applies an internal algorithm to smooth the trajectory. \n
			:param smooth_movement: 1| ON| 0| OFF
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.bool_to_str(smooth_movement)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:SMOVement {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:SMOVement \n
		Snippet: value: bool = driver.source.bb.gnss.receiver.v.location.smovement.get(vehicle = repcap.Vehicle.Default) \n
		Applies an internal algorithm to smooth the trajectory. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: smooth_movement: 1| ON| 0| OFF"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:SMOVement?')
		return Conversions.str_to_bool(response)
