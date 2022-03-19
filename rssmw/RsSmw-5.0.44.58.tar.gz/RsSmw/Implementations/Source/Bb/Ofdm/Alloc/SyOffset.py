from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyOffset:
	"""SyOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("syOffset", core, parent)

	def set(self, sym_offset: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SYOFfset \n
		Snippet: driver.source.bb.ofdm.alloc.syOffset.set(sym_offset = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the start symbol of the selected allocation. \n
			:param sym_offset: integer Range: 0 to 999
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(sym_offset)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SYOFfset {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SYOFfset \n
		Snippet: value: int = driver.source.bb.ofdm.alloc.syOffset.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the start symbol of the selected allocation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: sym_offset: integer Range: 0 to 999"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SYOFfset?')
		return Conversions.str_to_int(response)
