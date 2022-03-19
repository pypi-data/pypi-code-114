from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Extended:
	"""Extended commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extended", core, parent)

	def set(self, extended_inter: bool, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:EXTended \n
		Snippet: driver.source.bb.a3Tsc.plp.til.extended.set(extended_inter = False, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		If enabled, increases the time interleaving depth. \n
			:param extended_inter: 1| ON| 0| OFF
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.bool_to_str(extended_inter)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:EXTended {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:EXTended \n
		Snippet: value: bool = driver.source.bb.a3Tsc.plp.til.extended.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		If enabled, increases the time interleaving depth. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: extended_inter: 1| ON| 0| OFF"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:EXTended?')
		return Conversions.str_to_bool(response)
