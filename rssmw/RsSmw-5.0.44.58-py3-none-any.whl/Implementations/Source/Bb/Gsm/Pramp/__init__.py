from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pramp:
	"""Pramp commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

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

	def get_fdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:FDELay \n
		Snippet: value: float = driver.source.bb.gsm.pramp.get_fdelay() \n
		The command sets the offset in the Falling edge of the ramp envelope at the end of a slot. A positive value causes a ramp
		delay and a negative value advances the ramp. The setting is expressed in symbols. \n
			:return: fdelay: float Range: -9 to 9, Unit: symbol
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:PRAMp:FDELay?')
		return Conversions.str_to_float(response)

	def set_fdelay(self, fdelay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:FDELay \n
		Snippet: driver.source.bb.gsm.pramp.set_fdelay(fdelay = 1.0) \n
		The command sets the offset in the Falling edge of the ramp envelope at the end of a slot. A positive value causes a ramp
		delay and a negative value advances the ramp. The setting is expressed in symbols. \n
			:param fdelay: float Range: -9 to 9, Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(fdelay)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:PRAMp:FDELay {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:RDELay \n
		Snippet: value: float = driver.source.bb.gsm.pramp.get_rdelay() \n
		The command sets the offset in the Rising edge of the ramp envelope at the start of a slot. A positive value causes a
		ramp delay and a negative value advances the ramp. The setting is expressed in symbols. \n
			:return: rdelay: float Range: -9 to 9, Unit: symbol
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:PRAMp:RDELay?')
		return Conversions.str_to_float(response)

	def set_rdelay(self, rdelay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:RDELay \n
		Snippet: driver.source.bb.gsm.pramp.set_rdelay(rdelay = 1.0) \n
		The command sets the offset in the Rising edge of the ramp envelope at the start of a slot. A positive value causes a
		ramp delay and a negative value advances the ramp. The setting is expressed in symbols. \n
			:param rdelay: float Range: -9 to 9, Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(rdelay)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:PRAMp:RDELay {param}')

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.RampFunc:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:SHAPe \n
		Snippet: value: enums.RampFunc = driver.source.bb.gsm.pramp.get_shape() \n
		The command sets the edge shape of the ramp envelope. \n
			:return: shape: LINear| COSine LINear The transmitted power rises and falls linear fashion. COSine The transmitted power rises and falls in the shape of a cosine.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:PRAMp:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.RampFunc)

	def set_shape(self, shape: enums.RampFunc) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:SHAPe \n
		Snippet: driver.source.bb.gsm.pramp.set_shape(shape = enums.RampFunc.COSine) \n
		The command sets the edge shape of the ramp envelope. \n
			:param shape: LINear| COSine LINear The transmitted power rises and falls linear fashion. COSine The transmitted power rises and falls in the shape of a cosine.
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.RampFunc)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:PRAMp:SHAPe {param}')

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:TIME \n
		Snippet: value: float = driver.source.bb.gsm.pramp.get_time() \n
		The command sets the edge slope of the ramp envelope. This specifies the number of symbols over which the switching
		operation is stretched when the transmitted power is turned on and off. \n
			:return: time: float Range: 0.3 to 16, Unit: symbol
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:PRAMp:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRAMp:TIME \n
		Snippet: driver.source.bb.gsm.pramp.set_time(time = 1.0) \n
		The command sets the edge slope of the ramp envelope. This specifies the number of symbols over which the switching
		operation is stretched when the transmitted power is turned on and off. \n
			:param time: float Range: 0.3 to 16, Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:PRAMp:TIME {param}')

	def clone(self) -> 'Pramp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pramp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
