from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cil:
	"""Cil commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cil", core, parent)

	def set(self, cell_interleaver: bool, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:CIL \n
		Snippet: driver.source.bb.a3Tsc.plp.til.cil.set(cell_interleaver = False, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Enables or disables the interleaver operating at the cell level. \n
			:param cell_interleaver: 1| ON| 0| OFF
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.bool_to_str(cell_interleaver)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:CIL {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:CIL \n
		Snippet: value: bool = driver.source.bb.a3Tsc.plp.til.cil.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Enables or disables the interleaver operating at the cell level. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: cell_interleaver: 1| ON| 0| OFF"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:CIL?')
		return Conversions.str_to_bool(response)
