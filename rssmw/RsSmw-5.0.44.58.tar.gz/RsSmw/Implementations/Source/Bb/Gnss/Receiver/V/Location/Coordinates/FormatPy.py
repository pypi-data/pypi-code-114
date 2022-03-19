from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, position_format: enums.PositionFormat, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:COORdinates:FORMat \n
		Snippet: driver.source.bb.gnss.receiver.v.location.coordinates.formatPy.set(position_format = enums.PositionFormat.DECimal, vehicle = repcap.Vehicle.Default) \n
		Sets the format in which the latitude and longitude are set. \n
			:param position_format: DMS| DECimal
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(position_format, enums.PositionFormat)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:COORdinates:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.PositionFormat:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:COORdinates:FORMat \n
		Snippet: value: enums.PositionFormat = driver.source.bb.gnss.receiver.v.location.coordinates.formatPy.get(vehicle = repcap.Vehicle.Default) \n
		Sets the format in which the latitude and longitude are set. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: position_format: DMS| DECimal"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:COORdinates:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.PositionFormat)
