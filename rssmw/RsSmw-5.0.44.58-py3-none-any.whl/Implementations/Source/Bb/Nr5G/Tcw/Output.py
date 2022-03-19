from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SignalOutputs:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:OUTPut:MODE \n
		Snippet: value: enums.SignalOutputs = driver.source.bb.nr5G.tcw.output.get_mode() \n
		Selects the signal outputs used for the test case.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a performance characteristics test case (3GPP 38.141-1 / -2, chapter 8) . \n
			:return: signal_outputs: ALL| HSAL ALL Analog & digital output on the digital I/Q interface. HSAL Analog & digital output on the high speed digital I/Q interface.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:OUTPut:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SignalOutputs)

	def set_mode(self, signal_outputs: enums.SignalOutputs) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:OUTPut:MODE \n
		Snippet: driver.source.bb.nr5G.tcw.output.set_mode(signal_outputs = enums.SignalOutputs.ALL) \n
		Selects the signal outputs used for the test case.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a performance characteristics test case (3GPP 38.141-1 / -2, chapter 8) . \n
			:param signal_outputs: ALL| HSAL ALL Analog & digital output on the digital I/Q interface. HSAL Analog & digital output on the high speed digital I/Q interface.
		"""
		param = Conversions.enum_scalar_to_str(signal_outputs, enums.SignalOutputs)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:OUTPut:MODE {param}')
