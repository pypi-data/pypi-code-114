from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lora:
	"""Lora commands group definition. 61 total commands, 7 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lora", core, parent)

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def fconfiguration(self):
		"""fconfiguration commands group. 9 Sub-classes, 5 commands."""
		if not hasattr(self, '_fconfiguration'):
			from .Fconfiguration import Fconfiguration
			self._fconfiguration = Fconfiguration(self._core, self._cmd_group)
		return self._fconfiguration

	@property
	def impairments(self):
		"""impairments commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_impairments'):
			from .Impairments import Impairments
			self._impairments = Impairments(self._core, self._cmd_group)
		return self._impairments

	@property
	def setting(self):
		"""setting commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def trigger(self):
		"""trigger commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.LoRaBw:
		"""SCPI: [SOURce<HW>]:BB:LORA:BWIDth \n
		Snippet: value: enums.LoRaBw = driver.source.bb.lora.get_bandwidth() \n
		No command help available \n
			:return: bw: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.LoRaBw)

	def set_bandwidth(self, bw: enums.LoRaBw) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:BWIDth \n
		Snippet: driver.source.bb.lora.set_bandwidth(bw = enums.LoRaBw.BW10) \n
		No command help available \n
			:param bw: No help available
		"""
		param = Conversions.enum_scalar_to_str(bw, enums.LoRaBw)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:BWIDth {param}')

	def get_iinterval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:LORA:IINTerval \n
		Snippet: value: float = driver.source.bb.lora.get_iinterval() \n
		No command help available \n
			:return: iinterval: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:IINTerval?')
		return Conversions.str_to_float(response)

	def set_iinterval(self, iinterval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:IINTerval \n
		Snippet: driver.source.bb.lora.set_iinterval(iinterval = 1.0) \n
		No command help available \n
			:param iinterval: No help available
		"""
		param = Conversions.decimal_value_to_str(iinterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:IINTerval {param}')

	def get_osampling(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:LORA:OSAMpling \n
		Snippet: value: int = driver.source.bb.lora.get_osampling() \n
		No command help available \n
			:return: osampling: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:OSAMpling?')
		return Conversions.str_to_int(response)

	def set_osampling(self, osampling: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:OSAMpling \n
		Snippet: driver.source.bb.lora.set_osampling(osampling = 1) \n
		No command help available \n
			:param osampling: No help available
		"""
		param = Conversions.decimal_value_to_str(osampling)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:OSAMpling {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:PRESet \n
		Snippet: driver.source.bb.lora.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:PRESet \n
		Snippet: driver.source.bb.lora.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:LORA:PRESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:LORA:SLENgth \n
		Snippet: value: int = driver.source.bb.lora.get_slength() \n
		No command help available \n
			:return: slength: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:SLENgth \n
		Snippet: driver.source.bb.lora.set_slength(slength = 1) \n
		No command help available \n
			:param slength: No help available
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:LORA:STATe \n
		Snippet: value: bool = driver.source.bb.lora.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:STATe \n
		Snippet: driver.source.bb.lora.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:STATe {param}')

	def clone(self) -> 'Lora':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lora(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
