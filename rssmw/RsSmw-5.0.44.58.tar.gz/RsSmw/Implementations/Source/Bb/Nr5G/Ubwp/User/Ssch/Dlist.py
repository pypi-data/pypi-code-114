from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlist:
	"""Dlist commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlist", core, parent)

	def set(self, ssch_data_list: str, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:SSCH:DLISt \n
		Snippet: driver.source.bb.nr5G.ubwp.user.ssch.dlist.set(ssch_data_list = '1', userNull = repcap.UserNull.Default) \n
		No command help available \n
			:param ssch_data_list: No help available
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.value_to_quoted_str(ssch_data_list)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:SSCH:DLISt {param}')

	def get(self, userNull=repcap.UserNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:SSCH:DLISt \n
		Snippet: value: str = driver.source.bb.nr5G.ubwp.user.ssch.dlist.get(userNull = repcap.UserNull.Default) \n
		No command help available \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: ssch_data_list: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:SSCH:DLISt?')
		return trim_str_response(response)
