from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Am:
	"""Am commands group definition. 16 total commands, 5 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("am", core, parent)

	@property
	def apLayer(self):
		"""apLayer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_apLayer'):
			from .ApLayer import ApLayer
			self._apLayer = ApLayer(self._core, self._cmd_group)
		return self._apLayer

	@property
	def audGen(self):
		"""audGen commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_audGen'):
			from .AudGen import AudGen
			self._audGen = AudGen(self._core, self._cmd_group)
		return self._audGen

	@property
	def audio(self):
		"""audio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_audio'):
			from .Audio import Audio
			self._audio = Audio(self._core, self._cmd_group)
		return self._audio

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	def get_depth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:DEPTh \n
		Snippet: value: float = driver.source.bb.radio.am.get_depth() \n
		Sets the nominal modulation depth. \n
			:return: depth: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:DEPTh?')
		return Conversions.str_to_float(response)

	def set_depth(self, depth: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:DEPTh \n
		Snippet: driver.source.bb.radio.am.set_depth(depth = 1.0) \n
		Sets the nominal modulation depth. \n
			:param depth: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(depth)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:DEPTh {param}')

	# noinspection PyTypeChecker
	def get_input_py(self) -> enums.AudioBcInputSignal:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:INPut \n
		Snippet: value: enums.AudioBcInputSignal = driver.source.bb.radio.am.get_input_py() \n
		Sets the audio source for the AM modulator signal. \n
			:return: input_py: EXTernal| AGENerator| APLayer| OFF EXTernal Uses an external audio signal input at the 'User 2' connector. The audio source is fixed to 'Source S/PDIF', see [:SOURcehw]:BB:RADio:AM:SOURce. AGENerator Uses an internal audio generator as the signal source. APLayer Uses an audio player file, that is saved to the memory of the R&S SMCV100B. OFF Disables the audio source for the AM modulator.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.AudioBcInputSignal)

	def set_input_py(self, input_py: enums.AudioBcInputSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:INPut \n
		Snippet: driver.source.bb.radio.am.set_input_py(input_py = enums.AudioBcInputSignal.AGENerator) \n
		Sets the audio source for the AM modulator signal. \n
			:param input_py: EXTernal| AGENerator| APLayer| OFF EXTernal Uses an external audio signal input at the 'User 2' connector. The audio source is fixed to 'Source S/PDIF', see [:SOURcehw]:BB:RADio:AM:SOURce. AGENerator Uses an internal audio generator as the signal source. APLayer Uses an audio player file, that is saved to the memory of the R&S SMCV100B. OFF Disables the audio source for the AM modulator.
		"""
		param = Conversions.enum_scalar_to_str(input_py, enums.AudioBcInputSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:INPut {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:PRESet \n
		Snippet: driver.source.bb.radio.am.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:AM|FM|FM:RDS:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:PRESet \n
		Snippet: driver.source.bb.radio.am.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:AM|FM|FM:RDS:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:RADio:AM:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.BcInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:SOURce \n
		Snippet: value: enums.BcInputSignalSource = driver.source.bb.radio.am.get_source() \n
		Queries the audio source. \n
			:return: source: SPDif is fixed.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.BcInputSignalSource)

	def set_source(self, source: enums.BcInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:SOURce \n
		Snippet: driver.source.bb.radio.am.set_source(source = enums.BcInputSignalSource.SPDif) \n
		Queries the audio source. \n
			:param source: SPDif is fixed.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.BcInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:STATe \n
		Snippet: value: bool = driver.source.bb.radio.am.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:STATe \n
		Snippet: driver.source.bb.radio.am.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:STATe {param}')

	def clone(self) -> 'Am':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Am(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
