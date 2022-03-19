from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def dataRate(self):
		"""dataRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dataRate'):
			from .DataRate import DataRate
			self._dataRate = DataRate(self._core, self._cmd_group)
		return self._dataRate

	# noinspection PyTypeChecker
	def get_test_signal(self) -> enums.Atsc30InputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP:INPut:TESTsignal \n
		Snippet: value: enums.Atsc30InputSignalTestSignal = driver.source.bb.a3Tsc.plp.inputPy.get_test_signal() \n
		Defines the test signal data. \n
			:return: test_signal: TTSP| TIPP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:PLP:INPut:TESTsignal?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30InputSignalTestSignal)

	def set_test_signal(self, test_signal: enums.Atsc30InputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP:INPut:TESTsignal \n
		Snippet: driver.source.bb.a3Tsc.plp.inputPy.set_test_signal(test_signal = enums.Atsc30InputSignalTestSignal.TIPP) \n
		Defines the test signal data. \n
			:param test_signal: TTSP| TIPP
		"""
		param = Conversions.enum_scalar_to_str(test_signal, enums.Atsc30InputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP:INPut:TESTsignal {param}')

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
