from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, allocationNull=repcap.AllocationNull.Default, layerNull=repcap.LayerNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SCMA:LAYer<ST0>:STATe \n
		Snippet: driver.source.bb.ofdm.alloc.scma.layer.state.set(state = False, allocationNull = repcap.AllocationNull.Default, layerNull = repcap.LayerNull.Default) \n
		Enables the layer (codebook) . \n
			:param state: 0| 1| OFF| ON
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
		"""
		param = Conversions.bool_to_str(state)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SCMA:LAYer{layerNull_cmd_val}:STATe {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default, layerNull=repcap.LayerNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SCMA:LAYer<ST0>:STATe \n
		Snippet: value: bool = driver.source.bb.ofdm.alloc.scma.layer.state.get(allocationNull = repcap.AllocationNull.Default, layerNull = repcap.LayerNull.Default) \n
		Enables the layer (codebook) . \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
			:return: state: 0| 1| OFF| ON"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SCMA:LAYer{layerNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
