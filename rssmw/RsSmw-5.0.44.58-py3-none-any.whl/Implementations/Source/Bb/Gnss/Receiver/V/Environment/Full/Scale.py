from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scale:
	"""Scale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	def set(self, reference_scale: enums.RefScale, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:SCALe \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.full.scale.set(reference_scale = enums.RefScale.DISTance, vehicle = repcap.Vehicle.Default) \n
		Defines whether the obstacles' positions are defined as distance (in km) or as time (in s) . \n
			:param reference_scale: TIME| DISTance
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(reference_scale, enums.RefScale)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:SCALe {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.RefScale:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:SCALe \n
		Snippet: value: enums.RefScale = driver.source.bb.gnss.receiver.v.environment.full.scale.get(vehicle = repcap.Vehicle.Default) \n
		Defines whether the obstacles' positions are defined as distance (in km) or as time (in s) . \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: reference_scale: TIME| DISTance"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:SCALe?')
		return Conversions.str_to_scalar_enum(response, enums.RefScale)
