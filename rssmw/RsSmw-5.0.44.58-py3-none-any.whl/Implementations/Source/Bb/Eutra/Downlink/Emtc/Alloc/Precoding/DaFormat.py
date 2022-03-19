from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DaFormat:
	"""DaFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("daFormat", core, parent)

	def set(self, coord_map_mode: enums.CoordMapMode, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:DAFormat \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.precoding.daFormat.set(coord_map_mode = enums.CoordMapMode.CARTesian, allocationNull = repcap.AllocationNull.Default) \n
		Switches between the cartesian and cylindrical coordinates representation. \n
			:param coord_map_mode: CARTesian| CYLindrical
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(coord_map_mode, enums.CoordMapMode)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:DAFormat {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.CoordMapMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:DAFormat \n
		Snippet: value: enums.CoordMapMode = driver.source.bb.eutra.downlink.emtc.alloc.precoding.daFormat.get(allocationNull = repcap.AllocationNull.Default) \n
		Switches between the cartesian and cylindrical coordinates representation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: coord_map_mode: CARTesian| CYLindrical"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:DAFormat?')
		return Conversions.str_to_scalar_enum(response, enums.CoordMapMode)
