from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stype:
	"""Stype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stype", core, parent)

	def set(self, surface_type: enums.ReflMaterial, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:GSR:STYPe \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.gsr.stype.set(surface_type = enums.ReflMaterial.DRY, vehicle = repcap.Vehicle.Default) \n
		Defines the type of surface. \n
			:param surface_type: SEA| WATER| WET| MDRY| DRY| USER
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(surface_type, enums.ReflMaterial)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:GSR:STYPe {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.ReflMaterial:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:GSR:STYPe \n
		Snippet: value: enums.ReflMaterial = driver.source.bb.gnss.receiver.v.environment.gsr.stype.get(vehicle = repcap.Vehicle.Default) \n
		Defines the type of surface. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: surface_type: SEA| WATER| WET| MDRY| DRY| USER"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:GSR:STYPe?')
		return Conversions.str_to_scalar_enum(response, enums.ReflMaterial)
