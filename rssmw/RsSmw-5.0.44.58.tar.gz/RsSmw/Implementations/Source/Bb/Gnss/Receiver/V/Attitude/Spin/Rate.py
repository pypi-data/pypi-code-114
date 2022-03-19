from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def set(self, rate: float, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ATTitude:SPIN:RATE \n
		Snippet: driver.source.bb.gnss.receiver.v.attitude.spin.rate.set(rate = 1.0, vehicle = repcap.Vehicle.Default) \n
		Sets the constant rate of change of the roll. \n
			:param rate: float Range: -400 to 400
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.decimal_value_to_str(rate)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ATTitude:SPIN:RATE {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ATTitude:SPIN:RATE \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.attitude.spin.rate.get(vehicle = repcap.Vehicle.Default) \n
		Sets the constant rate of change of the roll. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: rate: float Range: -400 to 400"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ATTitude:SPIN:RATE?')
		return Conversions.str_to_float(response)
