from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interval:
	"""Interval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interval", core, parent)

	def set(self, subslice_interval: int, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TYPE:SUBSlice:[INTerval] \n
		Snippet: driver.source.bb.a3Tsc.plp.typePy.subslice.interval.set(subslice_interval = 1, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the difference between the lowest data cell index allocated to a subslice and the highest data cell index
		allocated to the immediately preceding subslice within a dispersed PLP. \n
			:param subslice_interval: integer Range: 0 to 16777215
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.decimal_value_to_str(subslice_interval)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TYPE:SUBSlice:INTerval {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TYPE:SUBSlice:[INTerval] \n
		Snippet: value: int = driver.source.bb.a3Tsc.plp.typePy.subslice.interval.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the difference between the lowest data cell index allocated to a subslice and the highest data cell index
		allocated to the immediately preceding subslice within a dispersed PLP. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: subslice_interval: integer Range: 0 to 16777215"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TYPE:SUBSlice:INTerval?')
		return Conversions.str_to_int(response)
