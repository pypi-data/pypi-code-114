from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BurstIndex:
	"""BurstIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burstIndex", core, parent)

	def set(self, burst_index: List[int], slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:MFRame:SLOT<ST0>:BURStindex \n
		Snippet: driver.source.bb.gsm.mframe.slot.burstIndex.set(burst_index = [1, 2, 3], slotNull = repcap.SlotNull.Default) \n
		No command help available \n
			:param burst_index: No help available
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.list_to_csv_str(burst_index)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:MFRame:SLOT{slotNull_cmd_val}:BURStindex {param}')

	def get(self, slotNull=repcap.SlotNull.Default) -> List[int]:
		"""SCPI: [SOURce<HW>]:BB:GSM:MFRame:SLOT<ST0>:BURStindex \n
		Snippet: value: List[int] = driver.source.bb.gsm.mframe.slot.burstIndex.get(slotNull = repcap.SlotNull.Default) \n
		No command help available \n
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: burst_index: No help available"""
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_bin_or_ascii_int_list(f'SOURce<HwInstance>:BB:GSM:MFRame:SLOT{slotNull_cmd_val}:BURStindex?')
		return response
