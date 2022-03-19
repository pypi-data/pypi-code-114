from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MapCoordinates:
	"""MapCoordinates commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mapCoordinates", core, parent)

	def set(self, map_coord: enums.CoordMapMode, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:APM:MAPCoordinates \n
		Snippet: driver.source.bb.v5G.downlink.user.apm.mapCoordinates.set(map_coord = enums.CoordMapMode.CARTesian, userIx = repcap.UserIx.Default) \n
		Switches between the Cartesian (real/imaginary) and cylindrical (magnitude/phase) coordinates representation. \n
			:param map_coord: CARTesian| CYLindrical
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(map_coord, enums.CoordMapMode)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:APM:MAPCoordinates {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.CoordMapMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:APM:MAPCoordinates \n
		Snippet: value: enums.CoordMapMode = driver.source.bb.v5G.downlink.user.apm.mapCoordinates.get(userIx = repcap.UserIx.Default) \n
		Switches between the Cartesian (real/imaginary) and cylindrical (magnitude/phase) coordinates representation. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: map_coord: CARTesian| CYLindrical"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:APM:MAPCoordinates?')
		return Conversions.str_to_scalar_enum(response, enums.CoordMapMode)
