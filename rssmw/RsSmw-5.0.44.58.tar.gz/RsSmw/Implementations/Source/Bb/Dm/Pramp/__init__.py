from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pramp:
	"""Pramp commands group definition. 8 total commands, 1 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pramp", core, parent)

	@property
	def bbOnly(self):
		"""bbOnly commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbOnly'):
			from .BbOnly import BbOnly
			self._bbOnly = BbOnly(self._core, self._cmd_group)
		return self._bbOnly

	def get_attenuation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:ATTenuation \n
		Snippet: value: float = driver.source.bb.dm.pramp.get_attenuation() \n
		Sets the level attenuation for signal ranges that are flagged with level attribute attenuated by the control signal. \n
			:return: attenuation: float Range: 0 to 50, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:ATTenuation?')
		return Conversions.str_to_float(response)

	def set_attenuation(self, attenuation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:ATTenuation \n
		Snippet: driver.source.bb.dm.pramp.set_attenuation(attenuation = 1.0) \n
		Sets the level attenuation for signal ranges that are flagged with level attribute attenuated by the control signal. \n
			:param attenuation: float Range: 0 to 50, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRAMp:ATTenuation {param}')

	def get_fdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:FDELay \n
		Snippet: value: float = driver.source.bb.dm.pramp.get_fdelay() \n
		Sets the delay in the rising edge. \n
			:return: fdelay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:FDELay?')
		return Conversions.str_to_float(response)

	def set_fdelay(self, fdelay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:FDELay \n
		Snippet: driver.source.bb.dm.pramp.set_fdelay(fdelay = 1.0) \n
		Sets the delay in the rising edge. \n
			:param fdelay: float Range: 0 to 4, Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(fdelay)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRAMp:FDELay {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:RDELay \n
		Snippet: value: float = driver.source.bb.dm.pramp.get_rdelay() \n
		Sets the delay in the rising edge. \n
			:return: rdelay: float Range: 0 to 4, Unit: symbol
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:RDELay?')
		return Conversions.str_to_float(response)

	def set_rdelay(self, rdelay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:RDELay \n
		Snippet: driver.source.bb.dm.pramp.set_rdelay(rdelay = 1.0) \n
		Sets the delay in the rising edge. \n
			:param rdelay: float Range: 0 to 4, Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(rdelay)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRAMp:RDELay {param}')

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.RampFunc:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:SHAPe \n
		Snippet: value: enums.RampFunc = driver.source.bb.dm.pramp.get_shape() \n
		Sets the edge shape of the ramp envelope. \n
			:return: shape: LINear| COSine
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.RampFunc)

	def set_shape(self, shape: enums.RampFunc) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:SHAPe \n
		Snippet: driver.source.bb.dm.pramp.set_shape(shape = enums.RampFunc.COSine) \n
		Sets the edge shape of the ramp envelope. \n
			:param shape: LINear| COSine
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.RampFunc)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRAMp:SHAPe {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceA:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:SOURce \n
		Snippet: value: enums.ClockSourceA = driver.source.bb.dm.pramp.get_source() \n
		Sets the source for the power ramp control signals. \n
			:return: source: INTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceA)

	def set_source(self, source: enums.ClockSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:SOURce \n
		Snippet: driver.source.bb.dm.pramp.set_source(source = enums.ClockSourceA.INTernal) \n
		Sets the source for the power ramp control signals. \n
			:param source: INTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRAMp:SOURce {param}')

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:TIME \n
		Snippet: value: float = driver.source.bb.dm.pramp.get_time() \n
		Sets the power ramping rise time and fall time for a burst. \n
			:return: time: float Range: 0.25 to 16, Unit: symbol
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:TIME \n
		Snippet: driver.source.bb.dm.pramp.set_time(time = 1.0) \n
		Sets the power ramping rise time and fall time for a burst. \n
			:param time: float Range: 0.25 to 16, Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRAMp:TIME {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:[STATe] \n
		Snippet: value: bool = driver.source.bb.dm.pramp.get_state() \n
		Enables or disables power ramping. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:[STATe] \n
		Snippet: driver.source.bb.dm.pramp.set_state(state = False) \n
		Enables or disables power ramping. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRAMp:STATe {param}')

	def clone(self) -> 'Pramp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pramp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
