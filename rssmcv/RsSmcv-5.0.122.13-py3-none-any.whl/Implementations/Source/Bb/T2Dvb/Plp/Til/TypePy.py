from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, til_type: int, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:TIL:TYPE \n
		Snippet: driver.source.bb.t2Dvb.plp.til.typePy.set(til_type = 1, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the time interleaver type. \n
			:param til_type: integer 0 Maps each interleaving frame directly to a T2 frame. 1 Maps each interleaving frame to more than one T2 frame. Range: 0 to 1
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.decimal_value_to_str(til_type)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:TIL:TYPE {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:TIL:TYPE \n
		Snippet: value: int = driver.source.bb.t2Dvb.plp.til.typePy.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the time interleaver type. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: til_type: integer 0 Maps each interleaving frame directly to a T2 frame. 1 Maps each interleaving frame to more than one T2 frame. Range: 0 to 1"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:TIL:TYPE?')
		return Conversions.str_to_int(response)
