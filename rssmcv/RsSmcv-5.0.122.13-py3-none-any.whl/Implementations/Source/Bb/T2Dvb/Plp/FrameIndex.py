from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrameIndex:
	"""FrameIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frameIndex", core, parent)

	def set(self, ff_index: int, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:FRAMeindex \n
		Snippet: driver.source.bb.t2Dvb.plp.frameIndex.set(ff_index = 1, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the index of the first frame of the super frame, in that the current PLP occurs. \n
			:param ff_index: integer Range: 0 to 255
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.decimal_value_to_str(ff_index)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:FRAMeindex {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:FRAMeindex \n
		Snippet: value: int = driver.source.bb.t2Dvb.plp.frameIndex.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the index of the first frame of the super frame, in that the current PLP occurs. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: ff_index: integer Range: 0 to 255"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:FRAMeindex?')
		return Conversions.str_to_int(response)
