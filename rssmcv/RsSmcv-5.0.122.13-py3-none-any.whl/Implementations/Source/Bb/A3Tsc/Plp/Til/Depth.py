from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Depth:
	"""Depth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("depth", core, parent)

	def set(self, depth: enums.Atsc30Depth, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:DEPTh \n
		Snippet: driver.source.bb.a3Tsc.plp.til.depth.set(depth = enums.Atsc30Depth.D1024, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the time interleaving depths. \n
			:param depth: D512| D724| D887| D1024| D1254| D1448 D1448|D1254 Require extended interleaving, e.g. for PLP 1: SOURce1:BB:A3TSc:PLP1:TIL:EXTended ON
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(depth, enums.Atsc30Depth)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:DEPTh {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30Depth:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:DEPTh \n
		Snippet: value: enums.Atsc30Depth = driver.source.bb.a3Tsc.plp.til.depth.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the time interleaving depths. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: depth: D512| D724| D887| D1024| D1254| D1448 D1448|D1254 Require extended interleaving, e.g. for PLP 1: SOURce1:BB:A3TSc:PLP1:TIL:EXTended ON"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:DEPTh?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30Depth)
