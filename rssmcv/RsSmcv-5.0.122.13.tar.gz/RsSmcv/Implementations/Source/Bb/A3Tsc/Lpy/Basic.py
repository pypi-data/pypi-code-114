from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Basic:
	"""Basic commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("basic", core, parent)

	# noinspection PyTypeChecker
	def get_fec_type(self) -> enums.Atsc30TimeInfoL1BasicFecType:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:BASic:FECType \n
		Snippet: value: enums.Atsc30TimeInfoL1BasicFecType = driver.source.bb.a3Tsc.lpy.basic.get_fec_type() \n
		Defines the protection level of L1 basic signaling. \n
			:return: l_1_basic_fec_type: MOD1| MOD2| MOD3| MOD4| MOD5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:L:BASic:FECType?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TimeInfoL1BasicFecType)

	def set_fec_type(self, l_1_basic_fec_type: enums.Atsc30TimeInfoL1BasicFecType) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:BASic:FECType \n
		Snippet: driver.source.bb.a3Tsc.lpy.basic.set_fec_type(l_1_basic_fec_type = enums.Atsc30TimeInfoL1BasicFecType.MOD1) \n
		Defines the protection level of L1 basic signaling. \n
			:param l_1_basic_fec_type: MOD1| MOD2| MOD3| MOD4| MOD5
		"""
		param = Conversions.enum_scalar_to_str(l_1_basic_fec_type, enums.Atsc30TimeInfoL1BasicFecType)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:L:BASic:FECType {param}')

	def get_version(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:BASic:VERSion \n
		Snippet: value: int = driver.source.bb.a3Tsc.lpy.basic.get_version() \n
		Queries the version of the L1 basic signaling structure that is used for the current frame. \n
			:return: l_1_basic_version: integer Range: 0 to 7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:L:BASic:VERSion?')
		return Conversions.str_to_int(response)
