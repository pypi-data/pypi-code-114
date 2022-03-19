from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pwr:
	"""Pwr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pwr", core, parent)

	def get(self, allocationNull=repcap.AllocationNull.Default, layerNull=repcap.LayerNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SCMA:LAYer<ST0>:PWR \n
		Snippet: value: float = driver.source.bb.ofdm.alloc.scma.layer.pwr.get(allocationNull = repcap.AllocationNull.Default, layerNull = repcap.LayerNull.Default) \n
		Applies a power offset to the selected layer relative to the others. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
			:return: power: float Range: -80 to 10"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SCMA:LAYer{layerNull_cmd_val}:PWR?')
		return Conversions.str_to_float(response)
