from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fint:
	"""Fint commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fint", core, parent)

	def set(self, frame_interval: int, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:TIL:FINT \n
		Snippet: driver.source.bb.t2Dvb.plp.til.fint.set(frame_interval = 1, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the time interleaver frame interval (IJump) . For limitations, see specification . \n
			:param frame_interval: integer Range: 1 to 255
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.decimal_value_to_str(frame_interval)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:TIL:FINT {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:TIL:FINT \n
		Snippet: value: int = driver.source.bb.t2Dvb.plp.til.fint.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the time interleaver frame interval (IJump) . For limitations, see specification . \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: frame_interval: integer Range: 1 to 255"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:TIL:FINT?')
		return Conversions.str_to_int(response)
