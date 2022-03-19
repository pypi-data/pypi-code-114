from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TestSignal:
	"""TestSignal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("testSignal", core, parent)

	def set(self, test_signal: enums.CodingInputSignalTestSignal, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:INPut:TESTsignal \n
		Snippet: driver.source.bb.t2Dvb.plp.inputPy.testSignal.set(test_signal = enums.CodingInputSignalTestSignal.TTSP, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the test signal data. \n
			:param test_signal: TTSP
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(test_signal, enums.CodingInputSignalTestSignal)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:INPut:TESTsignal {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.CodingInputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:INPut:TESTsignal \n
		Snippet: value: enums.CodingInputSignalTestSignal = driver.source.bb.t2Dvb.plp.inputPy.testSignal.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the test signal data. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: test_signal: TTSP"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:INPut:TESTsignal?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalTestSignal)
