from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detail:
	"""Detail commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detail", core, parent)

	@property
	def additional(self):
		"""additional commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_additional'):
			from .Additional import Additional
			self._additional = Additional(self._core, self._cmd_group)
		return self._additional

	# noinspection PyTypeChecker
	def get_fec_type(self) -> enums.Atsc30TimeInfoL1BasicFecType:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:DETail:FECType \n
		Snippet: value: enums.Atsc30TimeInfoL1BasicFecType = driver.source.bb.a3Tsc.lpy.detail.get_fec_type() \n
		Defines the protection level of L1 detail signaling. \n
			:return: l_1_detail_fec_type: MOD1| MOD2| MOD3| MOD4| MOD5| MOD6| MOD7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:L:DETail:FECType?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TimeInfoL1BasicFecType)

	def set_fec_type(self, l_1_detail_fec_type: enums.Atsc30TimeInfoL1BasicFecType) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:DETail:FECType \n
		Snippet: driver.source.bb.a3Tsc.lpy.detail.set_fec_type(l_1_detail_fec_type = enums.Atsc30TimeInfoL1BasicFecType.MOD1) \n
		Defines the protection level of L1 detail signaling. \n
			:param l_1_detail_fec_type: MOD1| MOD2| MOD3| MOD4| MOD5| MOD6| MOD7
		"""
		param = Conversions.enum_scalar_to_str(l_1_detail_fec_type, enums.Atsc30TimeInfoL1BasicFecType)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:L:DETail:FECType {param}')

	def get_version(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:DETail:VERSion \n
		Snippet: value: int = driver.source.bb.a3Tsc.lpy.detail.get_version() \n
		Sets the version of the L1 detail signaling structure that is used for the current frame. \n
			:return: l_1_detail_vers: integer Range: 0 to 15
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:L:DETail:VERSion?')
		return Conversions.str_to_int(response)

	def set_version(self, l_1_detail_vers: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:DETail:VERSion \n
		Snippet: driver.source.bb.a3Tsc.lpy.detail.set_version(l_1_detail_vers = 1) \n
		Sets the version of the L1 detail signaling structure that is used for the current frame. \n
			:param l_1_detail_vers: integer Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(l_1_detail_vers)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:L:DETail:VERSion {param}')

	def clone(self) -> 'Detail':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Detail(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
