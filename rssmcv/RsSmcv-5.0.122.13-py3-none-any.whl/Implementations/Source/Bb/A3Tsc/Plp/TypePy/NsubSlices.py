from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NsubSlices:
	"""NsubSlices commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsubSlices", core, parent)

	def set(self, number_subslices: int, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TYPE:NSUBslices \n
		Snippet: driver.source.bb.a3Tsc.plp.typePy.nsubSlices.set(number_subslices = 1, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the number of subslices for a dispersed PLP. \n
			:param number_subslices: integer Range: 1 to 16384
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.decimal_value_to_str(number_subslices)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TYPE:NSUBslices {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TYPE:NSUBslices \n
		Snippet: value: int = driver.source.bb.a3Tsc.plp.typePy.nsubSlices.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the number of subslices for a dispersed PLP. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: number_subslices: integer Range: 1 to 16384"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TYPE:NSUBslices?')
		return Conversions.str_to_int(response)
