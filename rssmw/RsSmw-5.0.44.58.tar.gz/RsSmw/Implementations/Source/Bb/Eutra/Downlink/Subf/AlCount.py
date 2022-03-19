from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlCount:
	"""AlCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alCount", core, parent)

	def set(self, alloc_count: int, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ALCount \n
		Snippet: driver.source.bb.eutra.downlink.subf.alCount.set(alloc_count = 1, subframeNull = repcap.SubframeNull.Default) \n
		Sets the number of scheduled allocations in the selected subframe. The maximum number of allocations that can be
		scheduled depends on the number of the selected resource blocks. \n
			:param alloc_count: integer Range: 0 to dynamic
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.decimal_value_to_str(alloc_count)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ALCount {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ALCount \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.alCount.get(subframeNull = repcap.SubframeNull.Default) \n
		Sets the number of scheduled allocations in the selected subframe. The maximum number of allocations that can be
		scheduled depends on the number of the selected resource blocks. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: alloc_count: integer Range: 0 to dynamic"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ALCount?')
		return Conversions.str_to_int(response)
