from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmodel:
	"""Pmodel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmodel", core, parent)

	def set(self, model: enums.ObscPhysModel, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:RPL:PMODel \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.rpl.pmodel.set(model = enums.ObscPhysModel.OBSCuration, vehicle = repcap.Vehicle.Default) \n
		Selects the physical effects to be simulated on the GNSS signal. \n
			:param model: OBSCuration| OMPath OBSCuration Simulates obscuration effects. OMPath Simulates obscuration and multipath propagation effects.
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(model, enums.ObscPhysModel)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:RPL:PMODel {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.ObscPhysModel:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:RPL:PMODel \n
		Snippet: value: enums.ObscPhysModel = driver.source.bb.gnss.receiver.v.environment.rpl.pmodel.get(vehicle = repcap.Vehicle.Default) \n
		Selects the physical effects to be simulated on the GNSS signal. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: model: No help available"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:RPL:PMODel?')
		return Conversions.str_to_scalar_enum(response, enums.ObscPhysModel)
