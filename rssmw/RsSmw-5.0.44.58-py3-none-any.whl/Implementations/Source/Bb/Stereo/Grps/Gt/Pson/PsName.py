from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsName:
	"""PsName commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psName", core, parent)

	def set(self, ps_name: str, groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:PSON:PSName \n
		Snippet: driver.source.bb.stereo.grps.gt.pson.psName.set(ps_name = '1', groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param ps_name: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
		"""
		param = Conversions.value_to_quoted_str(ps_name)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:PSON:PSName {param}')

	def get(self, groupNull=repcap.GroupNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:PSON:PSName \n
		Snippet: value: str = driver.source.bb.stereo.grps.gt.pson.psName.get(groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:return: ps_name: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:PSON:PSName?')
		return trim_str_response(response)
