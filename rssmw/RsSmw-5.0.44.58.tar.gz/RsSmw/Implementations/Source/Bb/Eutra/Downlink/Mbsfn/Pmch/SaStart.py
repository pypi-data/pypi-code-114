from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SaStart:
	"""SaStart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("saStart", core, parent)

	def set(self, alloc_start: int, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:SASTart \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.pmch.saStart.set(alloc_start = 1, indexNull = repcap.IndexNull.Default) \n
		Defines the first/last subframe allocated to this (P) MCH within a period identified by field commonSF-Alloc. \n
			:param alloc_start: integer Range: 0 to 1535
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
		"""
		param = Conversions.decimal_value_to_str(alloc_start)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:SASTart {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:SASTart \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.pmch.saStart.get(indexNull = repcap.IndexNull.Default) \n
		Defines the first/last subframe allocated to this (P) MCH within a period identified by field commonSF-Alloc. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
			:return: alloc_start: No help available"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:SASTart?')
		return Conversions.str_to_int(response)
