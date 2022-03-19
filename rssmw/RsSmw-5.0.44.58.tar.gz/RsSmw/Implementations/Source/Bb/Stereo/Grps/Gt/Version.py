from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Version:
	"""Version commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("version", core, parent)

	def set(self, version: enums.MappingType, groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:VERSion \n
		Snippet: driver.source.bb.stereo.grps.gt.version.set(version = enums.MappingType.A, groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param version: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
		"""
		param = Conversions.enum_scalar_to_str(version, enums.MappingType)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:VERSion {param}')

	# noinspection PyTypeChecker
	def get(self, groupNull=repcap.GroupNull.Default) -> enums.MappingType:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:VERSion \n
		Snippet: value: enums.MappingType = driver.source.bb.stereo.grps.gt.version.get(groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:return: version: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:VERSion?')
		return Conversions.str_to_scalar_enum(response, enums.MappingType)
