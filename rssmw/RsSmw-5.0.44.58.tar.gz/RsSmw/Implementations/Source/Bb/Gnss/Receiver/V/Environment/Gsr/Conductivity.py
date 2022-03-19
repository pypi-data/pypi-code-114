from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Conductivity:
	"""Conductivity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conductivity", core, parent)

	def set(self, conductivity: float, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:GSR:CONDuctivity \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.gsr.conductivity.set(conductivity = 1.0, vehicle = repcap.Vehicle.Default) \n
		Sets the surface conductivity. \n
			:param conductivity: float Range: 1E-6 to 20
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.decimal_value_to_str(conductivity)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:GSR:CONDuctivity {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:GSR:CONDuctivity \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.environment.gsr.conductivity.get(vehicle = repcap.Vehicle.Default) \n
		Sets the surface conductivity. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: conductivity: float Range: 1E-6 to 20"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:GSR:CONDuctivity?')
		return Conversions.str_to_float(response)
