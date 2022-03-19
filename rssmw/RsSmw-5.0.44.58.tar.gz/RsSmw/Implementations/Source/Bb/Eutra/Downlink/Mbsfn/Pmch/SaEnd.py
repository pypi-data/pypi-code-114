from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SaEnd:
	"""SaEnd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("saEnd", core, parent)

	def set(self, alloc_end: int, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:SAENd \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.pmch.saEnd.set(alloc_end = 1, indexNull = repcap.IndexNull.Default) \n
		Defines the first/last subframe allocated to this (P) MCH within a period identified by field commonSF-Alloc. \n
			:param alloc_end: integer Range: 0 to 1535
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
		"""
		param = Conversions.decimal_value_to_str(alloc_end)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:SAENd {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:SAENd \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.pmch.saEnd.get(indexNull = repcap.IndexNull.Default) \n
		Defines the first/last subframe allocated to this (P) MCH within a period identified by field commonSF-Alloc. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
			:return: alloc_end: integer Range: 0 to 1535"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:SAENd?')
		return Conversions.str_to_int(response)
