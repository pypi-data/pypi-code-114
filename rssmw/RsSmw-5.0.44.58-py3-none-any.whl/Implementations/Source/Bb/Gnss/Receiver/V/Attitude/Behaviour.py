from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Behaviour:
	"""Behaviour commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("behaviour", core, parent)

	def set(self, atitude_behaviour: enums.AttitMode, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ATTitude:[BEHaviour] \n
		Snippet: driver.source.bb.gnss.receiver.v.attitude.behaviour.set(atitude_behaviour = enums.AttitMode.CONStant, vehicle = repcap.Vehicle.Default) \n
		Defines how the attitude information is defined. \n
			:param atitude_behaviour: CONStant| FILE| MOTion| SPINning| REMote FILE enabled if smoothing is not used.
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(atitude_behaviour, enums.AttitMode)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ATTitude:BEHaviour {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.AttitMode:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ATTitude:[BEHaviour] \n
		Snippet: value: enums.AttitMode = driver.source.bb.gnss.receiver.v.attitude.behaviour.get(vehicle = repcap.Vehicle.Default) \n
		Defines how the attitude information is defined. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: atitude_behaviour: CONStant| FILE| MOTion| SPINning| REMote FILE enabled if smoothing is not used."""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ATTitude:BEHaviour?')
		return Conversions.str_to_scalar_enum(response, enums.AttitMode)
