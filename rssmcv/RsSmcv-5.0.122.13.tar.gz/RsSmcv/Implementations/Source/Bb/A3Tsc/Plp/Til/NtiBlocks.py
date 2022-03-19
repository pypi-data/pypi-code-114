from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NtiBlocks:
	"""NtiBlocks commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntiBlocks", core, parent)

	def set(self, number_ti_blocks: int, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:NTIBlocks \n
		Snippet: driver.source.bb.a3Tsc.plp.til.ntiBlocks.set(number_ti_blocks = 1, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the number of time interleaver blocks or the number of subframes.
			INTRO_CMD_HELP: The behavior depends on the setting of [:SOURce<hw>]:BB:A3TSc:PLP<ch>:TIL:INTer?: \n
			- If enabled, defines the number of subframes over which cells from one time interleaver (TI) block are carried.
			- If disabled, defines the number of time interleaver blocks. \n
			:param number_ti_blocks: integer Range: 1 to 16
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.decimal_value_to_str(number_ti_blocks)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:NTIBlocks {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:NTIBlocks \n
		Snippet: value: int = driver.source.bb.a3Tsc.plp.til.ntiBlocks.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the number of time interleaver blocks or the number of subframes.
			INTRO_CMD_HELP: The behavior depends on the setting of [:SOURce<hw>]:BB:A3TSc:PLP<ch>:TIL:INTer?: \n
			- If enabled, defines the number of subframes over which cells from one time interleaver (TI) block are carried.
			- If disabled, defines the number of time interleaver blocks. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: number_ti_blocks: integer Range: 1 to 16"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:NTIBlocks?')
		return Conversions.str_to_int(response)
