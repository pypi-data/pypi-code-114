from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ttime:
	"""Ttime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttime", core, parent)

	def set(self, ttime: int, groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:TTIMe \n
		Snippet: driver.source.bb.stereo.grps.gt.ttime.set(ttime = 1, groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param ttime: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
		"""
		param = Conversions.decimal_value_to_str(ttime)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:TTIMe {param}')

	def get(self, groupNull=repcap.GroupNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:TTIMe \n
		Snippet: value: int = driver.source.bb.stereo.grps.gt.ttime.get(groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:return: ttime: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:TTIMe?')
		return Conversions.str_to_int(response)
