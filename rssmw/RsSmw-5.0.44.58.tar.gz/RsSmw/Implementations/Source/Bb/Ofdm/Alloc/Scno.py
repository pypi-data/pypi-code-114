from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scno:
	"""Scno commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scno", core, parent)

	def set(self, no_of_subcarriers: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SCNO \n
		Snippet: driver.source.bb.ofdm.alloc.scno.set(no_of_subcarriers = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the number of allocated subcarriers. \n
			:param no_of_subcarriers: integer Range: 1 to 13107
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(no_of_subcarriers)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SCNO {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SCNO \n
		Snippet: value: int = driver.source.bb.ofdm.alloc.scno.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the number of allocated subcarriers. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: no_of_subcarriers: integer Range: 1 to 13107"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SCNO?')
		return Conversions.str_to_int(response)
