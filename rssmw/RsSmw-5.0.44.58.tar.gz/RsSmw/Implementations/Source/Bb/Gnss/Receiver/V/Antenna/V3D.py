from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class V3D:
	"""V3D commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("v3D", core, parent)

	def set(self, visualize_3_d: bool, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ANTenna:V3D \n
		Snippet: driver.source.bb.gnss.receiver.v.antenna.v3D.set(visualize_3_d = False, vehicle = repcap.Vehicle.Default) \n
		Activates the interactive 3D representation of the body mask or the power/phase distribution the antenna. \n
			:param visualize_3_d: 1| ON| 0| OFF
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.bool_to_str(visualize_3_d)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ANTenna:V3D {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ANTenna:V3D \n
		Snippet: value: bool = driver.source.bb.gnss.receiver.v.antenna.v3D.get(vehicle = repcap.Vehicle.Default) \n
		Activates the interactive 3D representation of the body mask or the power/phase distribution the antenna. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: visualize_3_d: 1| ON| 0| OFF"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ANTenna:V3D?')
		return Conversions.str_to_bool(response)
