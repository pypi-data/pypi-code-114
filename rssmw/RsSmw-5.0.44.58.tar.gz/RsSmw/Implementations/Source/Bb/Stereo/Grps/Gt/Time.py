from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, time: enums.FmStereoTimeCfgSel, groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:TIME \n
		Snippet: driver.source.bb.stereo.grps.gt.time.set(time = enums.FmStereoTimeCfgSel.SYSTime, groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param time: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
		"""
		param = Conversions.enum_scalar_to_str(time, enums.FmStereoTimeCfgSel)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:TIME {param}')

	# noinspection PyTypeChecker
	def get(self, groupNull=repcap.GroupNull.Default) -> enums.FmStereoTimeCfgSel:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:TIME \n
		Snippet: value: enums.FmStereoTimeCfgSel = driver.source.bb.stereo.grps.gt.time.get(groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:return: time: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:TIME?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoTimeCfgSel)
