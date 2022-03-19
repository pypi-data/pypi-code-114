from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbfPadding:
	"""BbfPadding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbfPadding", core, parent)

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:BBFPadding \n
		Snippet: value: bool = driver.source.bb.a3Tsc.plp.bbfPadding.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries, if baseband frame padding is enabled/disabled for the current . \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: bb_frame_padding: 1| ON| 0| OFF"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:BBFPadding?')
		return Conversions.str_to_bool(response)
