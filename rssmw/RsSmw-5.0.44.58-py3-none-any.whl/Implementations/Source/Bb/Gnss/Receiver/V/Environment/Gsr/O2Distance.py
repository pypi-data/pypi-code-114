from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class O2Distance:
	"""O2Distance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("o2Distance", core, parent)

	def set(self, distance: float, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:GSR:O2Distance \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.gsr.o2Distance.set(distance = 1.0, vehicle = repcap.Vehicle.Default) \n
		Sets the distance between the receiver and the left/right obstacles. \n
			:param distance: float Range: 0 to 1E4
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.decimal_value_to_str(distance)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:GSR:O2Distance {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:GSR:O2Distance \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.environment.gsr.o2Distance.get(vehicle = repcap.Vehicle.Default) \n
		Sets the distance between the receiver and the left/right obstacles. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: distance: float Range: 0 to 1E4"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:GSR:O2Distance?')
		return Conversions.str_to_float(response)
