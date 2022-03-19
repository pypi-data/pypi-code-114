from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcs:
	"""Mcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcs", core, parent)

	def set(self, mcs: int, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:MCS \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.pmch.mcs.set(mcs = 1, indexNull = repcap.IndexNull.Default) \n
		Sets the modulation and coding scheme (MCS) applicable for the subframes of the (P) MCH. \n
			:param mcs: integer Range: 0 to 28
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
		"""
		param = Conversions.decimal_value_to_str(mcs)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:MCS {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:MCS \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.pmch.mcs.get(indexNull = repcap.IndexNull.Default) \n
		Sets the modulation and coding scheme (MCS) applicable for the subframes of the (P) MCH. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
			:return: mcs: integer Range: 0 to 28"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:MCS?')
		return Conversions.str_to_int(response)
