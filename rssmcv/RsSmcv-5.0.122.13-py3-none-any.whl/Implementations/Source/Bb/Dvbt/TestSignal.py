from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TestSignal:
	"""TestSignal commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("testSignal", core, parent)

	# noinspection PyTypeChecker
	def get_low(self) -> enums.InputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TESTsignal:LOW \n
		Snippet: value: enums.InputSignalTestSignal = driver.source.bb.dvbt.testSignal.get_low() \n
		Defines the test signal data. \n
			:return: test_signal_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:TESTsignal:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalTestSignal)

	def set_low(self, test_signal_lp: enums.InputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TESTsignal:LOW \n
		Snippet: driver.source.bb.dvbt.testSignal.set_low(test_signal_lp = enums.InputSignalTestSignal.PAFC) \n
		Defines the test signal data. \n
			:param test_signal_lp: TTSP| PBEC| PAFC TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBEC PRBS before convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the convolutional encoder. PRBS data conforms with specification. PAFC PRBS after convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted after the convolutional encoder.
		"""
		param = Conversions.enum_scalar_to_str(test_signal_lp, enums.InputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:TESTsignal:LOW {param}')

	# noinspection PyTypeChecker
	def get_high(self) -> enums.InputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TESTsignal:[HIGH] \n
		Snippet: value: enums.InputSignalTestSignal = driver.source.bb.dvbt.testSignal.get_high() \n
		Defines the test signal data. \n
			:return: test_signal_hp: TTSP| PBEC| PAFC TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBEC PRBS before convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the convolutional encoder. PRBS data conforms with specification. PAFC PRBS after convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted after the convolutional encoder.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:TESTsignal:HIGH?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalTestSignal)

	def set_high(self, test_signal_hp: enums.InputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TESTsignal:[HIGH] \n
		Snippet: driver.source.bb.dvbt.testSignal.set_high(test_signal_hp = enums.InputSignalTestSignal.PAFC) \n
		Defines the test signal data. \n
			:param test_signal_hp: TTSP| PBEC| PAFC TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBEC PRBS before convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the convolutional encoder. PRBS data conforms with specification. PAFC PRBS after convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted after the convolutional encoder.
		"""
		param = Conversions.enum_scalar_to_str(test_signal_hp, enums.InputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:TESTsignal:HIGH {param}')
