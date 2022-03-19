from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Graphics:
	"""Graphics commands group definition. 10 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("graphics", core, parent)

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def set_add(self, size: enums.TranRecSize) -> None:
		"""SCPI: [SOURce]:BB:GRAPhics:ADD \n
		Snippet: driver.source.bb.graphics.set_add(size = enums.TranRecSize.MAXimized) \n
		Adds a graphical signal display (according to the current MODE, SOURce, SRATe:* and TRIGger:* settings) . \n
			:param size: MAXimized| MINimized
		"""
		param = Conversions.enum_scalar_to_str(size, enums.TranRecSize)
		self._core.io.write(f'SOURce:BB:GRAPhics:ADD {param}')

	def close(self) -> None:
		"""SCPI: [SOURce]:BB:GRAPhics:CLOSe \n
		Snippet: driver.source.bb.graphics.close() \n
		Closes all graphical signal displays. \n
		"""
		self._core.io.write(f'SOURce:BB:GRAPhics:CLOSe')

	def close_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce]:BB:GRAPhics:CLOSe \n
		Snippet: driver.source.bb.graphics.close_with_opc() \n
		Closes all graphical signal displays. \n
		Same as close, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:BB:GRAPhics:CLOSe', opc_timeout_ms)

	def get_fft_fscale(self) -> bool:
		"""SCPI: [SOURce]:BB:GRAPhics:FFTFscale \n
		Snippet: value: bool = driver.source.bb.graphics.get_fft_fscale() \n
		Defines the normalization of the power values in the power spectrum diagram. \n
			:return: state: 1| ON| 0| OFF 1 Normalized power in dBFS 0 Shows power distribution in dB/Hz
		"""
		response = self._core.io.query_str('SOURce:BB:GRAPhics:FFTFscale?')
		return Conversions.str_to_bool(response)

	def set_fft_fscale(self, state: bool) -> None:
		"""SCPI: [SOURce]:BB:GRAPhics:FFTFscale \n
		Snippet: driver.source.bb.graphics.set_fft_fscale(state = False) \n
		Defines the normalization of the power values in the power spectrum diagram. \n
			:param state: 1| ON| 0| OFF 1 Normalized power in dBFS 0 Shows power distribution in dB/Hz
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:BB:GRAPhics:FFTFscale {param}')

	# noinspection PyTypeChecker
	def get_fft_len(self) -> enums.TranRecFftLen:
		"""SCPI: [SOURce]:BB:GRAPhics:FFTLen \n
		Snippet: value: enums.TranRecFftLen = driver.source.bb.graphics.get_fft_len() \n
		Sets the FFT size. \n
			:return: mode: LEN256| LEN512| LEN1024| LEN2048| LEN4096 | LEN8192
		"""
		response = self._core.io.query_str('SOURce:BB:GRAPhics:FFTLen?')
		return Conversions.str_to_scalar_enum(response, enums.TranRecFftLen)

	def set_fft_len(self, mode: enums.TranRecFftLen) -> None:
		"""SCPI: [SOURce]:BB:GRAPhics:FFTLen \n
		Snippet: driver.source.bb.graphics.set_fft_len(mode = enums.TranRecFftLen.LEN1024) \n
		Sets the FFT size. \n
			:param mode: LEN256| LEN512| LEN1024| LEN2048| LEN4096 | LEN8192
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TranRecFftLen)
		self._core.io.write(f'SOURce:BB:GRAPhics:FFTLen {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.TranRecMode:
		"""SCPI: [SOURce<HW>]:BB:GRAPhics:MODE \n
		Snippet: value: enums.TranRecMode = driver.source.bb.graphics.get_mode() \n
		Selects the graphics mode of the graphical signal display. \n
			:return: mode: IQ| VECTor| CCDF| PSPectrum| CONStellation| EYEI| EYEQ
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GRAPhics:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TranRecMode)

	def set_mode(self, mode: enums.TranRecMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GRAPhics:MODE \n
		Snippet: driver.source.bb.graphics.set_mode(mode = enums.TranRecMode.CCDF) \n
		Selects the graphics mode of the graphical signal display. \n
			:param mode: IQ| VECTor| CCDF| PSPectrum| CONStellation| EYEI| EYEQ
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TranRecMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GRAPhics:MODE {param}')

	def clone(self) -> 'Graphics':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Graphics(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
