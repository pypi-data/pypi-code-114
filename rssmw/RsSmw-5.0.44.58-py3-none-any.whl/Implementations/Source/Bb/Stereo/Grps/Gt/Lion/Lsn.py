from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lsn:
	"""Lsn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lsn", core, parent)

	def set(self, lsn: List[str], groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:LION:LSN \n
		Snippet: driver.source.bb.stereo.grps.gt.lion.lsn.set(lsn = ['raw1', 'raw2', 'raw3'], groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param lsn: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
		"""
		param = Conversions.list_to_csv_str(lsn)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:LION:LSN {param}')

	def get(self, groupNull=repcap.GroupNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:LION:LSN \n
		Snippet: value: List[str] = driver.source.bb.stereo.grps.gt.lion.lsn.get(groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:return: lsn: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:LION:LSN?')
		return Conversions.str_to_str_list(response)
