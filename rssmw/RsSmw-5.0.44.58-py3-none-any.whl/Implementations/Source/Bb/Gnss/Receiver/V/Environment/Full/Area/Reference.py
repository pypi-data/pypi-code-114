from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, reference: float, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:REFerence \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.full.area.reference.set(reference = 1.0, vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Defines the reference starting position (in km) or time stamp (in s) of a specific obscured zone. \n
			:param reference: float Range: 0 to 1E4
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
		"""
		param = Conversions.decimal_value_to_str(reference)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:REFerence {param}')

	def get(self, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:REFerence \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.environment.full.area.reference.get(vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Defines the reference starting position (in km) or time stamp (in s) of a specific obscured zone. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: reference: float Range: 0 to 1E4"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:REFerence?')
		return Conversions.str_to_float(response)
