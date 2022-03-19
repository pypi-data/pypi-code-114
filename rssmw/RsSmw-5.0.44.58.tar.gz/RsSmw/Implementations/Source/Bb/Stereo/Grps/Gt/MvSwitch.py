from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MvSwitch:
	"""MvSwitch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mvSwitch", core, parent)

	def set(self, mv_switch: enums.FmStereoMscVce, groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:MVSWitch \n
		Snippet: driver.source.bb.stereo.grps.gt.mvSwitch.set(mv_switch = enums.FmStereoMscVce.MUSic, groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param mv_switch: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
		"""
		param = Conversions.enum_scalar_to_str(mv_switch, enums.FmStereoMscVce)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:MVSWitch {param}')

	# noinspection PyTypeChecker
	def get(self, groupNull=repcap.GroupNull.Default) -> enums.FmStereoMscVce:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:MVSWitch \n
		Snippet: value: enums.FmStereoMscVce = driver.source.bb.stereo.grps.gt.mvSwitch.get(groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:return: mv_switch: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:MVSWitch?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoMscVce)
