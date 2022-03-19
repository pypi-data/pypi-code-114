from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tbsi:
	"""Tbsi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbsi", core, parent)

	def set(self, chan_cod_tbs_index: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:TBSI \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.ccoding.tbsi.set(chan_cod_tbs_index = 1, allocationNull = repcap.AllocationNull.Default) \n
		Queries the resulting transport block size index. \n
			:param chan_cod_tbs_index: integer Range: 34 to 34
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(chan_cod_tbs_index)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:TBSI {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:TBSI \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.alloc.ccoding.tbsi.get(allocationNull = repcap.AllocationNull.Default) \n
		Queries the resulting transport block size index. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: chan_cod_tbs_index: integer Range: 34 to 34"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:TBSI?')
		return Conversions.str_to_int(response)
