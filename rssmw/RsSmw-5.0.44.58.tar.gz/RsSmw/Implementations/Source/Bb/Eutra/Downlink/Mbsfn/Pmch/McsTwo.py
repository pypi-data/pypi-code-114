from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsTwo:
	"""McsTwo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsTwo", core, parent)

	def set(self, pmch_mcs_two: bool, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:MCSTwo \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.pmch.mcsTwo.set(pmch_mcs_two = False, indexNull = repcap.IndexNull.Default) \n
		Defines which of the two tables defined in is used to specify the used modulation and coding scheme. \n
			:param pmch_mcs_two: 1| ON| 0| OFF 0 Table 7.1.7.1-1 is used 1 Table 7.1.7.1-1A is used
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
		"""
		param = Conversions.bool_to_str(pmch_mcs_two)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:MCSTwo {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:MCSTwo \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.mbsfn.pmch.mcsTwo.get(indexNull = repcap.IndexNull.Default) \n
		Defines which of the two tables defined in is used to specify the used modulation and coding scheme. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
			:return: pmch_mcs_two: 1| ON| 0| OFF 0 Table 7.1.7.1-1 is used 1 Table 7.1.7.1-1A is used"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:MCSTwo?')
		return Conversions.str_to_bool(response)
