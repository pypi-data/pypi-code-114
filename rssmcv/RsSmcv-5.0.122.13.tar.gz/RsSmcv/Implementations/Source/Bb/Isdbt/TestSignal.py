from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TestSignal:
	"""TestSignal commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("testSignal", core, parent)

	# noinspection PyTypeChecker
	def get_a(self) -> enums.InputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TESTsignal:A \n
		Snippet: value: enums.InputSignalTestSignal = driver.source.bb.isdbt.testSignal.get_a() \n
		Defines the test signal data. \n
			:return: test_signal_a: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:TESTsignal:A?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalTestSignal)

	def set_a(self, test_signal_a: enums.InputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TESTsignal:A \n
		Snippet: driver.source.bb.isdbt.testSignal.set_a(test_signal_a = enums.InputSignalTestSignal.PAFC) \n
		Defines the test signal data. \n
			:param test_signal_a: PAFC| PBEC| TTSP
		"""
		param = Conversions.enum_scalar_to_str(test_signal_a, enums.InputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:TESTsignal:A {param}')

	# noinspection PyTypeChecker
	def get_b(self) -> enums.InputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TESTsignal:B \n
		Snippet: value: enums.InputSignalTestSignal = driver.source.bb.isdbt.testSignal.get_b() \n
		Defines the test signal data. \n
			:return: test_signal_b: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:TESTsignal:B?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalTestSignal)

	def set_b(self, test_signal_b: enums.InputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TESTsignal:B \n
		Snippet: driver.source.bb.isdbt.testSignal.set_b(test_signal_b = enums.InputSignalTestSignal.PAFC) \n
		Defines the test signal data. \n
			:param test_signal_b: PAFC| PBEC| TTSP
		"""
		param = Conversions.enum_scalar_to_str(test_signal_b, enums.InputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:TESTsignal:B {param}')

	# noinspection PyTypeChecker
	def get_c(self) -> enums.InputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TESTsignal:C \n
		Snippet: value: enums.InputSignalTestSignal = driver.source.bb.isdbt.testSignal.get_c() \n
		Defines the test signal data. \n
			:return: test_signal_c: PAFC| PBEC| TTSP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:TESTsignal:C?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalTestSignal)

	def set_c(self, test_signal_c: enums.InputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TESTsignal:C \n
		Snippet: driver.source.bb.isdbt.testSignal.set_c(test_signal_c = enums.InputSignalTestSignal.PAFC) \n
		Defines the test signal data. \n
			:param test_signal_c: PAFC| PBEC| TTSP
		"""
		param = Conversions.enum_scalar_to_str(test_signal_c, enums.InputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:TESTsignal:C {param}')
