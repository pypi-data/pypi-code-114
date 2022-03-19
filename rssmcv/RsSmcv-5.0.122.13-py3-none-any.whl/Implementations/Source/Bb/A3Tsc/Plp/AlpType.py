from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlpType:
	"""AlpType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpType", core, parent)

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30InputType:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:ALPType \n
		Snippet: value: enums.Atsc30InputType = driver.source.bb.a3Tsc.plp.alpType.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the input source type of encapsulation. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: alp_encaps_type: IP| TS IP Query result for IP-based input via SOURce1:BB:A3TSc:INPut:TYPe IP TS Query result for serial input via SOURce1:BB:A3TSc:INPut:TYPe TS"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:ALPType?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30InputType)
