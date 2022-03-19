from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbfCounter:
	"""BbfCounter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbfCounter", core, parent)

	def set(self, bb_frame_counter: bool, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:BBFCounter \n
		Snippet: driver.source.bb.a3Tsc.plp.bbfCounter.set(bb_frame_counter = False, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Enables/disables the baseband frame counter. The counter is initialized to 0 and increments linearly by one for each
		baseband packet of the current PLP. \n
			:param bb_frame_counter: 1| ON| 0| OFF
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.bool_to_str(bb_frame_counter)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:BBFCounter {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:BBFCounter \n
		Snippet: value: bool = driver.source.bb.a3Tsc.plp.bbfCounter.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Enables/disables the baseband frame counter. The counter is initialized to 0 and increments linearly by one for each
		baseband packet of the current PLP. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: bb_frame_counter: 1| ON| 0| OFF"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:BBFCounter?')
		return Conversions.str_to_bool(response)
