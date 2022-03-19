from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpd:
	"""Dpd commands group definition. 53 total commands, 10 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpd", core, parent)

	@property
	def amam(self):
		"""amam commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_amam'):
			from .Amam import Amam
			self._amam = Amam(self._core, self._cmd_group)
		return self._amam

	@property
	def amPm(self):
		"""amPm commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPm
			self._amPm = AmPm(self._core, self._cmd_group)
		return self._amPm

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def lrf(self):
		"""lrf commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_lrf'):
			from .Lrf import Lrf
			self._lrf = Lrf(self._core, self._cmd_group)
		return self._lrf

	@property
	def measurement(self):
		"""measurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import Measurement
			self._measurement = Measurement(self._core, self._cmd_group)
		return self._measurement

	@property
	def output(self):
		"""output commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def pin(self):
		"""pin commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pin'):
			from .Pin import Pin
			self._pin = Pin(self._core, self._cmd_group)
		return self._pin

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def shaping(self):
		"""shaping commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_shaping'):
			from .Shaping import Shaping
			self._shaping = Shaping(self._core, self._cmd_group)
		return self._shaping

	def get_am_first(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DPD:AMFirst \n
		Snippet: value: bool = driver.source.iq.dpd.get_am_first() \n
		Sets that the AM/AM predistortion is applied before the AM/PM. \n
			:return: am_am_first_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:AMFirst?')
		return Conversions.str_to_bool(response)

	def set_am_first(self, am_am_first_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:AMFirst \n
		Snippet: driver.source.iq.dpd.set_am_first(am_am_first_state = False) \n
		Sets that the AM/AM predistortion is applied before the AM/PM. \n
			:param am_am_first_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(am_am_first_state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:AMFirst {param}')

	# noinspection PyTypeChecker
	def get_lreference(self) -> enums.DpdPowRef:
		"""SCPI: [SOURce<HW>]:IQ:DPD:LREFerence \n
		Snippet: value: enums.DpdPowRef = driver.source.iq.dpd.get_lreference() \n
		Sets whether a dynamic (BDPD|ADPD) or a static (SDPS) adaptation of the range the selected DPD is applied on. \n
			:return: level_reference: BDPD| ADPD| SDPD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:LREFerence?')
		return Conversions.str_to_scalar_enum(response, enums.DpdPowRef)

	def set_lreference(self, level_reference: enums.DpdPowRef) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:LREFerence \n
		Snippet: driver.source.iq.dpd.set_lreference(level_reference = enums.DpdPowRef.ADPD) \n
		Sets whether a dynamic (BDPD|ADPD) or a static (SDPS) adaptation of the range the selected DPD is applied on. \n
			:param level_reference: BDPD| ADPD| SDPD
		"""
		param = Conversions.enum_scalar_to_str(level_reference, enums.DpdPowRef)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:LREFerence {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:PRESet \n
		Snippet: driver.source.iq.dpd.preset() \n
		Sets the default DPD settings (*RST values specified for the commands) . Not affected is the state set with the command
		[:SOURce<hw>]:IQ:DPD:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:PRESet \n
		Snippet: driver.source.iq.dpd.preset_with_opc() \n
		Sets the default DPD settings (*RST values specified for the commands) . Not affected is the state set with the command
		[:SOURce<hw>]:IQ:DPD:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:IQ:DPD:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_scale(self) -> enums.IqOutEnvScale:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SCALe \n
		Snippet: value: enums.IqOutEnvScale = driver.source.iq.dpd.get_scale() \n
		Determines the units used on the x and y-axis. \n
			:return: scale: POWer| VOLTage
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:SCALe?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutEnvScale)

	def set_scale(self, scale: enums.IqOutEnvScale) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SCALe \n
		Snippet: driver.source.iq.dpd.set_scale(scale = enums.IqOutEnvScale.POWer) \n
		Determines the units used on the x and y-axis. \n
			:param scale: POWer| VOLTage
		"""
		param = Conversions.enum_scalar_to_str(scale, enums.IqOutEnvScale)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:SCALe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DPD:STATe \n
		Snippet: value: bool = driver.source.iq.dpd.get_state() \n
		Enabels/disables the generation of digitally pre-distorted signals. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:STATe \n
		Snippet: driver.source.iq.dpd.set_state(state = False) \n
		Enabels/disables the generation of digitally pre-distorted signals. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:STATe {param}')

	def clone(self) -> 'Dpd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
