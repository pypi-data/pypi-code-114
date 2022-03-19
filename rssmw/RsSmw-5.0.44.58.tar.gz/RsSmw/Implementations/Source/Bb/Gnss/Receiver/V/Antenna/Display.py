from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Display:
	"""Display commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	def set(self, antenna_view: enums.AntViewType, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ANTenna:DISPlay \n
		Snippet: driver.source.bb.gnss.receiver.v.antenna.display.set(antenna_view = enums.AntViewType.AATTenuation, vehicle = repcap.Vehicle.Default) \n
		Select the antenna characteristics that are currently visualized. \n
			:param antenna_view: APOWer| APHase| BODY| POSition
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(antenna_view, enums.AntViewType)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ANTenna:DISPlay {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.AntViewType:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ANTenna:DISPlay \n
		Snippet: value: enums.AntViewType = driver.source.bb.gnss.receiver.v.antenna.display.get(vehicle = repcap.Vehicle.Default) \n
		Select the antenna characteristics that are currently visualized. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: antenna_view: APOWer| APHase| BODY| POSition"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ANTenna:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.AntViewType)
