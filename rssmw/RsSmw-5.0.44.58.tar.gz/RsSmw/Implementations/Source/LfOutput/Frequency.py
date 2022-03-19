from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, lfOutput=repcap.LfOutput.Default) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:FREQuency \n
		Snippet: driver.source.lfOutput.frequency.set(frequency = 1.0, lfOutput = repcap.LfOutput.Default) \n
		Sets the frequency of the LF signal in [:SOURce<hw>]:LFOutput:FREQuency:MODE CW|FIXed mode.
			INTRO_CMD_HELP: Note: \n
			- If the LF generator is used as a signal source, the instrument performs the analog modulations (AM/FM/ΦM/PM) with this frequency.
			- In sweep mode ([:SOURce<hw>]:LFOutput:FREQuency:MODE SWE) , the frequency is coupled with the sweep frequency. \n
			:param frequency: float Range: 0.1 to depends on the installed options (R&S SMW-K24) , Unit: Hz
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:FREQuency {param}')

	def get(self, lfOutput=repcap.LfOutput.Default) -> float:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:FREQuency \n
		Snippet: value: float = driver.source.lfOutput.frequency.get(lfOutput = repcap.LfOutput.Default) \n
		Sets the frequency of the LF signal in [:SOURce<hw>]:LFOutput:FREQuency:MODE CW|FIXed mode.
			INTRO_CMD_HELP: Note: \n
			- If the LF generator is used as a signal source, the instrument performs the analog modulations (AM/FM/ΦM/PM) with this frequency.
			- In sweep mode ([:SOURce<hw>]:LFOutput:FREQuency:MODE SWE) , the frequency is coupled with the sweep frequency. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: frequency: float Range: 0.1 to depends on the installed options (R&S SMW-K24) , Unit: Hz"""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)

	def get_manual(self) -> float:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:MANual \n
		Snippet: value: float = driver.source.lfOutput.frequency.get_manual() \n
		Sets the frequency of the subsequent sweep step if LFO:SWE:MODE MAN. Use a separate command for each sweep step. \n
			:return: manual: float You can select any value within the setting range, where: STARt is set with [:SOURcehw]:LFOutput:FREQuency:STARt STOP is set with [:SOURcehw]:LFOutput:FREQuency:STOP Range: STARt to STOP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:FREQuency:MANual?')
		return Conversions.str_to_float(response)

	def set_manual(self, manual: float) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:MANual \n
		Snippet: driver.source.lfOutput.frequency.set_manual(manual = 1.0) \n
		Sets the frequency of the subsequent sweep step if LFO:SWE:MODE MAN. Use a separate command for each sweep step. \n
			:param manual: float You can select any value within the setting range, where: STARt is set with [:SOURcehw]:LFOutput:FREQuency:STARt STOP is set with [:SOURcehw]:LFOutput:FREQuency:STOP Range: STARt to STOP
		"""
		param = Conversions.decimal_value_to_str(manual)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:FREQuency:MANual {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.LfFreqMode:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:MODE \n
		Snippet: value: enums.LfFreqMode = driver.source.lfOutput.frequency.get_mode() \n
		Sets the mode for the output of the LF generator frequency, and determines the commands to be used for frequency settings. \n
			:return: mode: CW| FIXed| SWEep CW|FIXed Sets the fixed-frequency mode. CW and FIXed are synonyms. To set the output frequency, use command [:SOURcehw]:LFOutputch:FREQuency SWEep Sets sweep mode. To set the frequency, use the commands: [:SOURcehw]:LFOutput:FREQuency:STARt and [:SOURcehw]:LFOutput:FREQuency:STOP Or [:SOURcehw]:LFOutput:FREQuency:MANual
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:FREQuency:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.LfFreqMode)

	def set_mode(self, mode: enums.LfFreqMode) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:MODE \n
		Snippet: driver.source.lfOutput.frequency.set_mode(mode = enums.LfFreqMode.CW) \n
		Sets the mode for the output of the LF generator frequency, and determines the commands to be used for frequency settings. \n
			:param mode: CW| FIXed| SWEep CW|FIXed Sets the fixed-frequency mode. CW and FIXed are synonyms. To set the output frequency, use command [:SOURcehw]:LFOutputch:FREQuency SWEep Sets sweep mode. To set the frequency, use the commands: [:SOURcehw]:LFOutput:FREQuency:STARt and [:SOURcehw]:LFOutput:FREQuency:STOP Or [:SOURcehw]:LFOutput:FREQuency:MANual
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.LfFreqMode)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:FREQuency:MODE {param}')

	def get_start(self) -> float:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:STARt \n
		Snippet: value: float = driver.source.lfOutput.frequency.get_start() \n
		Sets the start/stop frequency for [:SOURce<hw>]:LFOutput:FREQuency:MODE SWEep. \n
			:return: start: float Range: 0.1 Hz to 1 MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:FREQuency:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start: float) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:STARt \n
		Snippet: driver.source.lfOutput.frequency.set_start(start = 1.0) \n
		Sets the start/stop frequency for [:SOURce<hw>]:LFOutput:FREQuency:MODE SWEep. \n
			:param start: float Range: 0.1 Hz to 1 MHz
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:FREQuency:STARt {param}')

	def get_stop(self) -> float:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:STOP \n
		Snippet: value: float = driver.source.lfOutput.frequency.get_stop() \n
		Sets the start/stop frequency for [:SOURce<hw>]:LFOutput:FREQuency:MODE SWEep. \n
			:return: stop: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:FREQuency:STOP?')
		return Conversions.str_to_float(response)

	def set_stop(self, stop: float) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:FREQuency:STOP \n
		Snippet: driver.source.lfOutput.frequency.set_stop(stop = 1.0) \n
		Sets the start/stop frequency for [:SOURce<hw>]:LFOutput:FREQuency:MODE SWEep. \n
			:param stop: float Range: 0.1 Hz to 1 MHz
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:FREQuency:STOP {param}')
