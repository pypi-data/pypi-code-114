from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: float, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:LENGth \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.full.area.length.set(length = 1.0, vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Sets the length of the obscuring zone, defined in km or sec. \n
			:param length: float Range: 1E-3 to 50
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
		"""
		param = Conversions.decimal_value_to_str(length)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:LENGth {param}')

	def get(self, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:LENGth \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.environment.full.area.length.get(vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Sets the length of the obscuring zone, defined in km or sec. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: length: float Range: 1E-3 to 50"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:LENGth?')
		return Conversions.str_to_float(response)
