from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pulm:
	"""Pulm commands group definition. 14 total commands, 3 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulm", core, parent)

	@property
	def double(self):
		"""double commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_double'):
			from .Double import Double
			self._double = Double(self._core, self._cmd_group)
		return self._double

	@property
	def output(self):
		"""output commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def trigger(self):
		"""trigger commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:PULM:DELay \n
		Snippet: value: float = driver.source.pulm.get_delay() \n
		Sets the pulse delay. \n
			:return: delay: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:PULM:DELay \n
		Snippet: driver.source.pulm.set_delay(delay = 1.0) \n
		Sets the pulse delay. \n
			:param delay: float
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:PULM:DELay {param}')

	# noinspection PyTypeChecker
	def get_impedance(self) -> enums.ImpG50G1K:
		"""SCPI: [SOURce<HW>]:PULM:IMPedance \n
		Snippet: value: enums.ImpG50G1K = driver.source.pulm.get_impedance() \n
		Sets the impedance for the external pulse modulation input. \n
			:return: impedance: G50| G1K
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:IMPedance?')
		return Conversions.str_to_scalar_enum(response, enums.ImpG50G1K)

	def set_impedance(self, impedance: enums.ImpG50G1K) -> None:
		"""SCPI: [SOURce<HW>]:PULM:IMPedance \n
		Snippet: driver.source.pulm.set_impedance(impedance = enums.ImpG50G1K.G1K) \n
		Sets the impedance for the external pulse modulation input. \n
			:param impedance: G50| G1K
		"""
		param = Conversions.enum_scalar_to_str(impedance, enums.ImpG50G1K)
		self._core.io.write(f'SOURce<HwInstance>:PULM:IMPedance {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PulsMode:
		"""SCPI: [SOURce<HW>]:PULM:MODE \n
		Snippet: value: enums.PulsMode = driver.source.pulm.get_mode() \n
		Selects the mode for the pulse modulation. \n
			:return: mode: SINGle| DOUBle SINGle Generates a single pulse. DOUBle Generates two pulses within one pulse period.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PulsMode)

	def set_mode(self, mode: enums.PulsMode) -> None:
		"""SCPI: [SOURce<HW>]:PULM:MODE \n
		Snippet: driver.source.pulm.set_mode(mode = enums.PulsMode.DOUBle) \n
		Selects the mode for the pulse modulation. \n
			:param mode: SINGle| DOUBle SINGle Generates a single pulse. DOUBle Generates two pulses within one pulse period.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PulsMode)
		self._core.io.write(f'SOURce<HwInstance>:PULM:MODE {param}')

	def get_period(self) -> float:
		"""SCPI: [SOURce<HW>]:PULM:PERiod \n
		Snippet: value: float = driver.source.pulm.get_period() \n
		Sets the period of the generated pulse, that means the repetition frequency of the internally generated modulation signal. \n
			:return: period: float The minimum value depends on the installed options R&S SMW-K22 or R&S SMW-K23 Range: 20E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, period: float) -> None:
		"""SCPI: [SOURce<HW>]:PULM:PERiod \n
		Snippet: driver.source.pulm.set_period(period = 1.0) \n
		Sets the period of the generated pulse, that means the repetition frequency of the internally generated modulation signal. \n
			:param period: float The minimum value depends on the installed options R&S SMW-K22 or R&S SMW-K23 Range: 20E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(period)
		self._core.io.write(f'SOURce<HwInstance>:PULM:PERiod {param}')

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.NormalInverted:
		"""SCPI: [SOURce<HW>]:PULM:POLarity \n
		Snippet: value: enums.NormalInverted = driver.source.pulm.get_polarity() \n
		Sets the polarity of the externally applied modulation signal. \n
			:return: polarity: NORMal| INVerted NORMal Suppresses the RF signal during the pulse pause. INVerted Suppresses the RF signal during the pulse.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.NormalInverted)

	def set_polarity(self, polarity: enums.NormalInverted) -> None:
		"""SCPI: [SOURce<HW>]:PULM:POLarity \n
		Snippet: driver.source.pulm.set_polarity(polarity = enums.NormalInverted.INVerted) \n
		Sets the polarity of the externally applied modulation signal. \n
			:param polarity: NORMal| INVerted NORMal Suppresses the RF signal during the pulse pause. INVerted Suppresses the RF signal during the pulse.
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.NormalInverted)
		self._core.io.write(f'SOURce<HwInstance>:PULM:POLarity {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.SourceInt:
		"""SCPI: [SOURce<HW>]:PULM:SOURce \n
		Snippet: value: enums.SourceInt = driver.source.pulm.get_source() \n
		Selects between the internal (pulse generator) or an external pulse signal for the modulation. \n
			:return: source: INTernal| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)

	def set_source(self, source: enums.SourceInt) -> None:
		"""SCPI: [SOURce<HW>]:PULM:SOURce \n
		Snippet: driver.source.pulm.set_source(source = enums.SourceInt.EXTernal) \n
		Selects between the internal (pulse generator) or an external pulse signal for the modulation. \n
			:param source: INTernal| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceInt)
		self._core.io.write(f'SOURce<HwInstance>:PULM:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:PULM:STATe \n
		Snippet: value: bool = driver.source.pulm.get_state() \n
		Activates pulse modulation. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:PULM:STATe \n
		Snippet: driver.source.pulm.set_state(state = False) \n
		Activates pulse modulation. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:PULM:STATe {param}')

	# noinspection PyTypeChecker
	def get_ttype(self) -> enums.PulsTransType:
		"""SCPI: [SOURce<HW>]:PULM:TTYPe \n
		Snippet: value: enums.PulsTransType = driver.source.pulm.get_ttype() \n
		Sets the transition mode for the pulse signal. \n
			:return: source: SMOothed| FAST SMOothed flattens the slew rate, resulting in longer rise/fall times. FAST enables fast transitions with shortest rise and fall times.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:TTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.PulsTransType)

	def set_ttype(self, source: enums.PulsTransType) -> None:
		"""SCPI: [SOURce<HW>]:PULM:TTYPe \n
		Snippet: driver.source.pulm.set_ttype(source = enums.PulsTransType.FAST) \n
		Sets the transition mode for the pulse signal. \n
			:param source: SMOothed| FAST SMOothed flattens the slew rate, resulting in longer rise/fall times. FAST enables fast transitions with shortest rise and fall times.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.PulsTransType)
		self._core.io.write(f'SOURce<HwInstance>:PULM:TTYPe {param}')

	def get_width(self) -> float:
		"""SCPI: [SOURce<HW>]:PULM:WIDTh \n
		Snippet: value: float = driver.source.pulm.get_width() \n
		Sets the width of the generated pulse, that means the pulse length. It must be at least 20ns less than the set pulse
		period. \n
			:return: width: float Range: 20E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:WIDTh?')
		return Conversions.str_to_float(response)

	def set_width(self, width: float) -> None:
		"""SCPI: [SOURce<HW>]:PULM:WIDTh \n
		Snippet: driver.source.pulm.set_width(width = 1.0) \n
		Sets the width of the generated pulse, that means the pulse length. It must be at least 20ns less than the set pulse
		period. \n
			:param width: float Range: 20E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(width)
		self._core.io.write(f'SOURce<HwInstance>:PULM:WIDTh {param}')

	def clone(self) -> 'Pulm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pulm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
