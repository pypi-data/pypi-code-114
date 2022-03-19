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

	def set(self, usch_data_list: str, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:USCH:DLISt \n
		Snippet: driver.source.bb.nr5G.ubwp.user.usch.dlist.set(usch_data_list = '1', userNull = repcap.UserNull.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:param usch_data_list: string Filename incl. file extension or complete file path
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.value_to_quoted_str(usch_data_list)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:USCH:DLISt {param}')

	def get(self, userNull=repcap.UserNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:USCH:DLISt \n
		Snippet: value: str = driver.source.bb.nr5G.ubwp.user.usch.dlist.get(userNull = repcap.UserNull.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: usch_data_list: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:USCH:DLISt?')
		return trim_str_response(response)
