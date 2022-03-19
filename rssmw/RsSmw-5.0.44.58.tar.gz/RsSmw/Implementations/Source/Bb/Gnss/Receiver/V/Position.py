from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Position:
	"""Position commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def set(self, positioning: enums.LocationModel, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:POSition \n
		Snippet: driver.source.bb.gnss.receiver.v.position.set(positioning = enums.LocationModel.HIL, vehicle = repcap.Vehicle.Default) \n
		Sets what kind of receiver is simulated. \n
			:param positioning: STATic| MOVing| HIL
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(positioning, enums.LocationModel)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:POSition {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.LocationModel:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:POSition \n
		Snippet: value: enums.LocationModel = driver.source.bb.gnss.receiver.v.position.get(vehicle = repcap.Vehicle.Default) \n
		Sets what kind of receiver is simulated. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: positioning: STATic| MOVing| HIL"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:POSition?')
		return Conversions.str_to_scalar_enum(response, enums.LocationModel)
