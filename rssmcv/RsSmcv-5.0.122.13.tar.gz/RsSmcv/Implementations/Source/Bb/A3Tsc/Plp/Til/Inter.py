from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Inter:
	"""Inter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inter", core, parent)

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:INTer \n
		Snippet: value: bool = driver.source.bb.a3Tsc.plp.til.inter.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the interleaving frame content and mapping. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: inter_subframe: 1| ON| 0| OFF ON Each interleaving frame contains one time interleaver block and is mapped to multiple subframes. OFF Each interleaving frame is mapped directly to one subframe, and the interleaving frame is composed of one or more time interleaver blocks."""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:INTer?')
		return Conversions.str_to_bool(response)
