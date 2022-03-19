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

	def set(self, data_list: str, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:DLISt \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.pmch.dlist.set(data_list = '1', indexNull = repcap.IndexNull.Default) \n
		Sets the data list of the data source for the selected PMCH/MTCH. \n
			:param data_list: string
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
		"""
		param = Conversions.value_to_quoted_str(data_list)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:DLISt {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:DLISt \n
		Snippet: value: str = driver.source.bb.eutra.downlink.mbsfn.pmch.dlist.get(indexNull = repcap.IndexNull.Default) \n
		Sets the data list of the data source for the selected PMCH/MTCH. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
			:return: data_list: string"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:DLISt?')
		return trim_str_response(response)
