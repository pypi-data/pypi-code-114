from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Shaping:
	"""Shaping commands group definition. 23 total commands, 6 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shaping", core, parent)

	@property
	def clipping(self):
		"""clipping commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_clipping'):
			from .Clipping import Clipping
			self._clipping = Clipping(self._core, self._cmd_group)
		return self._clipping

	@property
	def coefficients(self):
		"""coefficients commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_coefficients'):
			from .Coefficients import Coefficients
			self._coefficients = Coefficients(self._core, self._cmd_group)
		return self._coefficients

	@property
	def detroughing(self):
		"""detroughing commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_detroughing'):
			from .Detroughing import Detroughing
			self._detroughing = Detroughing(self._core, self._cmd_group)
		return self._detroughing

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def pv(self):
		"""pv commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pv'):
			from .Pv import Pv
			self._pv = Pv(self._core, self._cmd_group)
		return self._pv

	# noinspection PyTypeChecker
	def get_interp(self) -> enums.Interpolation:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:INTerp \n
		Snippet: value: enums.Interpolation = driver.source.iq.output.analog.envelope.shaping.get_interp() \n
		For envelope shaping with shaping tables, enables linear interpolation. \n
			:return: ipart_interpolation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:INTerp?')
		return Conversions.str_to_scalar_enum(response, enums.Interpolation)

	def set_interp(self, ipart_interpolation: enums.Interpolation) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:INTerp \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.set_interp(ipart_interpolation = enums.Interpolation.LINear) \n
		For envelope shaping with shaping tables, enables linear interpolation. \n
			:param ipart_interpolation: OFF| LINear| POWer LINear = Linear (Voltage) POWer = Linear (Power)
		"""
		param = Conversions.enum_scalar_to_str(ipart_interpolation, enums.Interpolation)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:INTerp {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.IqOutEnvShapeMode:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:MODE \n
		Snippet: value: enums.IqOutEnvShapeMode = driver.source.iq.output.analog.envelope.shaping.get_mode() \n
		Enables envelope shaping and selects the method to define the shaping function. \n
			:return: shaping_mode: OFF| LINear| TABLe| POLYnomial| DETRoughing| POWer LINear = Linear (Voltage) POWer = Linear (Power)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutEnvShapeMode)

	def set_mode(self, shaping_mode: enums.IqOutEnvShapeMode) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:MODE \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.set_mode(shaping_mode = enums.IqOutEnvShapeMode.DETRoughing) \n
		Enables envelope shaping and selects the method to define the shaping function. \n
			:param shaping_mode: OFF| LINear| TABLe| POLYnomial| DETRoughing| POWer LINear = Linear (Voltage) POWer = Linear (Power)
		"""
		param = Conversions.enum_scalar_to_str(shaping_mode, enums.IqOutEnvShapeMode)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:MODE {param}')

	# noinspection PyTypeChecker
	def get_scale(self) -> enums.IqOutEnvScale:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:SCALe \n
		Snippet: value: enums.IqOutEnvScale = driver.source.iq.output.analog.envelope.shaping.get_scale() \n
		Determines the units used on the x and y axis. \n
			:return: scale: POWer| VOLTage
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:SCALe?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutEnvScale)

	def set_scale(self, scale: enums.IqOutEnvScale) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:SCALe \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.set_scale(scale = enums.IqOutEnvScale.POWer) \n
		Determines the units used on the x and y axis. \n
			:param scale: POWer| VOLTage
		"""
		param = Conversions.enum_scalar_to_str(scale, enums.IqOutEnvScale)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:SCALe {param}')

	def clone(self) -> 'Shaping':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Shaping(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
